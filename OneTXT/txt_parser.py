import sys
from random import choice

from telethon import TelegramClient

from point import get_msg
from essentials import api_id, api_hash


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


idi = 20525
parse_dat = []
tg_grp = 'banknifty_nifty_WOLFCALLS'
client = TelegramClient('parse_ssn', api_id, api_hash)
client.start()

parse_dat.append(
    get_msg(
        client,
        idi,
        gname=tg_grp
    )
)

parse_dat.append(
    get_msg(
        client,
        idi+1,
        gname=tg_grp
    )
)

options: list = []

for dat in parse_dat:
    doc: dict = {}
    dat_str: str = (dat['txt']).lower()
    try:
        idx_start = dat_str.index('buy')
        idx_end = dat_str.index('sl')
        statement = dat_str[idx_start:idx_end]
        idx_trg = statement.index('trg')
        doc['statement'] = statement
        doc.update(xtract_option_bid_value(statement))
        doc['target'] = xtract_targets(statement)
        doc['channel'] = 'BANKNIFTY'
        options.append(doc)
    except Exception:
        sys.exit(dat_str)

for opt in options:
    print(opt)
