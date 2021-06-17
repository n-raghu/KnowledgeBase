import sys
from time import sleep
from random import choice

from telethon import TelegramClient

from essentials import api_id, api_hash
from innards import get_msg, get_max


def xtract_option_bid_value(stmt: str) -> dict:
    trg: int = stmt.index('trg')
    nustm = stmt[4:trg-1]
    nustm_parts = nustm.split()
    bid = nustm_parts.pop()
    mode = nustm_parts.pop()
    return {
        'bid': bid,
        'mode': mode,
        'option': ''.join(nustm_parts)
    }


def xtract_targets(stmt: str):
    trg: int = stmt.index('trg')
    low_high = (stmt[trg+3:]).strip()
    return {
        'safe': int(low_high.split('-')[0]) - choice([1,2,3]),
        'aggresive': int(low_high.split('-')[1]) - choice(range(1, 16))
    }


def stream(pid, api_id=api_id, api_hash=api_hash):
    tg_grp = 'banknifty_nifty_WOLFCALLS'
    posted_msg_id = set()
    client = TelegramClient(f'ssn_{tg_grp}', api_id, api_hash)
    client.start()

    options: list = []
    mid = get_max(client, tg_grp) - 36
    print('mid', mid)

    while True:
        doc: dict = {}
        msg = get_msg(mid, tg_grp, client)
        if msg['mid'] in posted_msg_id:
            mid += 1
            sleep(1.1)
            continue

        posted_msg_id.add(msg['mid'])
        dat_str: str = (msg['txt']).lower()

        if 'promo' in dat_str:
            print('PROMO')
            mid += 1
            continue
        elif 'sell' in dat_str:
            print('SELL')
            mid += 1
            continue

        try:
            idx_start = dat_str.index('buy')
            idx_end = dat_str.index('sl')
            statement = dat_str[idx_start:idx_end]
            doc['statement'] = statement
            doc.update(xtract_option_bid_value(statement))
            doc['target'] = xtract_targets(statement)
            doc['channel'] = tg_grp
            options.append(doc)
            print(doc)
            mid += 1
        except Exception:
            sys.exit(msg)
