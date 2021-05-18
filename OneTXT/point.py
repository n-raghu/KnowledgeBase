import re
import sys
from time import sleep

from telethon import TelegramClient, events, sync

from essentials import api_id, api_hash

with open('power_phrases', 'r') as pfile:
    power_phrases = pfile.readlines()
power_phrases = [p_.removesuffix('\n') for p_ in power_phrases]


def get_msg(client, idi, gname, power_phs=power_phrases):
    mlist = client.get_messages(gname, offset_id=idi)
    try:
        m_ = mlist[0].raw_text.lower()
        power = next((phs for phs in power_phrases if phs in m_), False)
        return {
            'txt': (mlist[0].text).upper() if power else str_cleanser(mlist[0].text),
            'idi': mlist[0].id,
        }
    except Exception:
        return 'hitNext'


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


def get_max(client, gname: str) -> int:
    mlist = client.get_messages(gname)
    try:
        return mlist.total
    except Exception:
        return 0


if __name__ == '__main__':
    try:
        tg_grp = sys.argv[1]
    except Exception:
        tg_grp = 'GoldFlints'

    print('Group name: ', tg_grp)

    client = TelegramClient('ssn_1', api_id, api_hash)
    client.start()
    idi = get_max(client, tg_grp) - 10
    print(f'Total messages identified in {tg_grp} are {idi+10}, Replying from {idi}.')
    received_msg_id = set()

    while True:
        msg = get_msg(client, idi, tg_grp)
        if msg == 'hitNext':
            print('hitNext ', end='')
        elif msg and not msg['idi'] in received_msg_id:
            print(f"{idi} - #{msg['idi']} - {msg['txt']}", flush=True)                
            received_msg_id.add(msg['idi'])
        else:
            sleep(1.5)

        idi += 1
