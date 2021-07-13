from time import sleep
from random import choice

from telethon import TelegramClient

from essentials import api_id, api_hash, BROADCAST_PROMO, BROADCAST_RAW_STMT
from innards import get_msgs, grp_max


def xtract_option_bid_value(stmt: str) -> dict:
    options = ['ce', 'pe']
    trg: int = stmt.index('trg')
    nustm = stmt[4:trg-1]
    nustm_parts = nustm.split()
    bid = nustm_parts.pop()
    mode = nustm_parts.pop()
    if mode not in options:
        mode = nustm_parts.pop()
    return {
        'bid': bid,
        'mode': mode,
        'option': ''.join(nustm_parts)
    }


def fix_targets(stmt: str):
    trg: int = stmt.index('trg')
    low_high = (stmt[trg+3:]).strip()
    return {
        'safe': int(low_high.split('-')[0]) - choice([1,2,3]),
        'aggresive': int(low_high.split('-')[1]) - choice(range(1, 16))
    }


def analyse_messages(Q, msgs_):
    for msg in msgs_:
        try:
            doc: dict = {}
            doc['src'] = 'BWC'
            raw_stmt = (msg['txt']).lower()
            if BROADCAST_RAW_STMT:
                doc['stmt'] = raw_stmt
            if '--- Promo' in raw_stmt:
                if BROADCAST_PROMO:
                    Q.put(msg)
                continue
            elif 'sell' in raw_stmt:
                doc['msg'] = 'SELL MESSAGE'
                Q.put(doc)
                continue

            idx_start = raw_stmt.index('buy')
            idx_end = raw_stmt.index('sl')
            statement = raw_stmt[idx_start:idx_end]
            doc.update(xtract_option_bid_value(statement))
            doc['target'] = fix_targets(statement)
            Q.put(doc)
        except Exception as err:
            Q.put({
                'err': str(err),
                'stmt': raw_stmt
            })


def stream(Q, api_id=api_id, api_hash=api_hash):
    tg_grp = 'banknifty_nifty_WOLFCALLS'
    client = TelegramClient(f'ssn_{tg_grp}', api_id, api_hash)
    client.start()

    options: list = []
    mid = max(grp_max(client, tg_grp) - 500, 1)
    max_mid = 0
    print('mid', mid)

    while True:
        doc: dict = {}
        mid, messages = get_msgs(mid, tg_grp, client)
        if messages and mid > max_mid:
            analyse_messages(Q, messages)
            max_mid = mid
        else:
            sleep(1.1)
            continue
