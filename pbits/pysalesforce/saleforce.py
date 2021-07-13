import json
import itertools
from io import BytesIO

import requests as req
from pandas import DataFrame as PDF
from datetime import datetime as dtm
from yaml import safe_load as y_safe_load


# Load from config file
def refresh_config():
    with open('config.yml') as yfile:
        cfg = y_safe_load(yfile)
    return cfg


# Function to fetch token
def gen_sfdc_token(cfg):
    token_params = {
        'grant_type': 'password',
        'client_id': cfg['salesforce']['cid'],
        'client_secret': cfg['salesforce']['secret'],
        'username': cfg['salesforce']['uid'],
        'password': cfg['salesforce']['pwd'],
    }
    access_point_headers = {
        'content-type': 'application/x-www-form-urlencoded'
    }
    r = req.post(
        cfg['salesforce']['domain_url'] + cfg['salesforce']['token'],
        params=token_params,
        headers=access_point_headers,
    )
    if not r.ok:
        print(r.text)
        raise req.RequestException(r.text)
    return json.loads(r.text)['access_token']


# Hit Salesforce
def fetch_sfdc_dat(uri, token, cfg):
    data_point_headers = {
        'accept': cfg['salesforce']['data_ctype'],
        'content-type': cfg['salesforce']['data_ctype'],
        'Authorization': f'Bearer {token}'
    }
    R = req.get(uri, headers=data_point_headers)
    return json.loads(R.text)


# Function to create SOQL
def create_api_query(layout, cfg):
    columns = cfg['layouts'][layout]
    api_resource = cfg['salesforce']['query_point']
    default_start_date = str(cfg['salesforce']['start_date'])
    iso_start_stamp = dtm.fromisoformat(default_start_date).isoformat()
    whereclause = f'where+LastModifiedDate>={iso_start_stamp}Z'
    sql = f'select+{columns}+from+{layout}+{whereclause}'
    return f'{api_resource}/?q={sql}'


# Collect SFDC Layout data
def collect_layout_data(layout, cfg):
    layout_dat = []
    sfdc_token = gen_sfdc_token(cfg)
    api_domain_url = cfg['salesforce']['domain_url']
    sfdc_dat = {
        'nextRecordsUrl': create_api_query(layout, cfg),
        'records': [],
        'done': False,
    }
    while True:
        if not 'nextRecordsUrl' in sfdc_dat:
            break
        next_uri = sfdc_dat['nextRecordsUrl']
        sfdc_dat = fetch_sfdc_dat(
            uri=f'{api_domain_url}/{next_uri}',
            token=sfdc_token,
            cfg=cfg,
        )
        layout_dat = itertools.chain(layout_dat, sfdc_dat['records']) # Chain all the iterations data

    return layout_dat


# Write chained iterate values to parquet
def itr_to_parquet(n, fname, itr_dat):
    records: int = 0
    with open(fname, 'wb') as pfile:
        while True:
            chunk = itertools.islice(itr_dat, n)
            frame = PDF(list(chunk))
            if len(frame) == 0:
                break
            del frame['attributes']
            records += len(frame)
            with BytesIO() as binary_object:
                frame.to_parquet(binary_object, compression='snappy', index=False)
                pfile.write(binary_object.getvalue())

    return records


def tester():
    cfg = refresh_config()
    dat = collect_layout_data('account', cfg)
    print(itr_to_parquet(cfg['chunk']['size'], 'a.parqt', dat))


if __name__ == '__main__':
    tester()
