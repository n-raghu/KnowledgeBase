import sys
from random import choice

from telethon import TelegramClient

from essentials import api_id, api_hash
from innards import get_next_msg, get_max


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
    client = TelegramClient(f'ssn_{tg_grp}', api_id, api_hash)
    client.start()

    options: list = []
    mid = get_max(tg_grp)
    print('mid', mid)

    while True:
        doc: dict = {}
        msg = get_next_msg(mid, tg_grp, client)
        print(msg)
        sys.exit()
"""
        dat_str: str = (dat['txt']).lower()
        try:
            idx_start = dat_str.index('buy')
            idx_end = dat_str.index('sl')
            statement = dat_str[idx_start:idx_end]
            doc['statement'] = statement
            doc.update(xtract_option_bid_value(statement))
            doc['target'] = xtract_targets(statement)
            doc['channel'] = tg_grp
            options.append(doc)
        except Exception:
            sys.exit(dat_str)

    for opt in options:
        print(opt)
"""