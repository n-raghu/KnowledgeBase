import re
import sys
from time import sleep
from glob import iglob
from itertools import tee

from telethon import TelegramClient, events, sync

from essentials import api_id, api_hash, BROADCAST_PROMO


_files = iglob('phrases/**')
_phrases: dict = {}

for _f in _files:
    with open(_f, 'r') as _file:
        _kwords = _file.readlines()
    _file_parts = _f.split('/')
    _grp = _file_parts[-1]
    _phrases[_grp] = iter([_kw.strip() for _kw in _kwords])


def repo_phrases(grp, phs=_phrases):
    dat, dat_bkp = tee(phs[grp])
    phs[grp] = dat
    return dat_bkp


def get_msgs(idi: int, gname: str, client):
    messages = client.get_messages(gname, min_id=idi, limit=100, reverse=True)
    if messages:
        _id = messages[-1].id
    else:
        _id = idi
    if BROADCAST_PROMO:
        return _id, iter([msg_cleanser(msg, gname) for msg in messages])
    else:
        cleansed_messages = iter([msg_cleanser(msg, gname) for msg in messages])
        return _id, iter([m for m in cleansed_messages if m])


def msg_cleanser(msg, gname):
    power_phs = repo_phrases(gname)
    try:
        m_ = msg.raw_text.lower()
    except Exception:
        return None
    power = next((phs for phs in power_phs if phs in m_), False)
    if BROADCAST_PROMO:
        return {
            'txt': (msg.text).upper() if power else str_cleanser(msg.text),
            'mid': msg.id,
        }
    elif power:
        return {
            'txt': (msg.text).upper(),
            'mid': msg.id,
        }
    else:
        return None


def str_cleanser(_str):
    bad_chars = ['\r', '\t', '\n', ]
    for char in bad_chars:
        _str = _str.replace(char, '')
    if len(_str) > 36:
        nustr = _str[:36].lower()
        nustr = nustr + '...<TRUNCATED>...'
    else:
        nustr = _str.lower()
    nustr = ''.join([i if ord(i) < 500 else ' ' for i in nustr])
    return f"--- Promo({re.sub(' +', ' ', nustr)}) ---"


def grp_max(client, gname: str) -> int:
    mlist = client.get_messages(gname)
    try:
        return mlist[0].id
    except Exception:
        return 0


def tester(grp = 'GoldFlints'):
    print('Group name: ', grp)

    client = TelegramClient('ssn_tst', api_id, api_hash)
    client.start()
    idi = max(grp_max(client, grp) - 100, 1)
    print(f'Replying from {idi}.')
    max_mid: int = 0

    while True:
        try:
            idi, messages = get_msgs(idi, grp, client)
            if messages and idi > max_mid:
                for msg in messages:
                    print(f"{idi} - #{msg['mid']} - {msg['txt']}", flush=True)
                max_mid = idi
            else:
                sleep(1.5)
        except Exception as err:
            print(err)


if __name__ == '__main__':
    tester()
