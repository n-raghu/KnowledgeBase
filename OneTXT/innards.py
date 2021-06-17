import re
import sys
from time import sleep

from telethon import TelegramClient, events, sync

from essentials import api_id, api_hash


def power_phrases():
    with open('power_phrases', 'r') as pfile:
        power_phrases = pfile.readlines()
    return[p_.removesuffix('\n') for p_ in power_phrases]


def get_msgs(idi: int, gname: str, client):
    messages = client.get_messages(gname, min_id=idi, limit=100, reverse=True)
    if messages:
        _id = messages[-1].id
    else:
        _id = idi
    return _id, iter([msg_cleanser(msg) for msg in messages])


def msg_cleanser(msg):
    power_phs = power_phrases()
    m_ = msg.raw_text.lower()
    power = next((phs for phs in power_phs if phs in m_), False)
    return {
        'txt': (msg.text).upper() if power else str_cleanser(msg.text),
        'mid': msg.id,
    }


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
        return mlist.total
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
