# from pymysql import *
import datetime
import hashlib
from decimal import Decimal
from common.db import postgres_session

session = postgres_session()


def concat(*values):
    s = ''
    for v in values:
        if v is None:
            pass
        elif isinstance(v, bool):
            s += 't' if v else 'f'
        elif isinstance(v, int) or isinstance(v, Decimal):
            s += str(v)
        elif isinstance(v, str):
            s += v
        elif isinstance(v, datetime.datetime):
            s += v.strftime('%Y-%m-%d %H:%M:%S')
        else:
            raise Exception('not supported type')
    return s


def calculate_hash(value, salt, version):
    hash_str = ''
    if version == 1:
        salt = concat(salt, 'P@ss!odk')
        hash_str = hashlib.md5(concat(value, '@', salt).encode()).hexdigest()
    else:
        return hash_str
    hash_str = concat('{:04d}'.format(version), hash_str)
    return hash_str


def calculate_tx_hash(tx, salt, version):
    hash_str = ''
    if version == 1:
        value = concat(tx.currency_code,
                       tx.type,
                       tx.status,
                       tx.SN,
                       tx.create_customer_id,
                       tx.payer_customer_id,
                       tx.payer_wallet_id,
                       tx.payer_mobile,
                       tx.payer_platform,
                       tx.payee_customer_id,
                       tx.payee_wallet_id,
                       tx.payee_email,
                       tx.payee_mobile,
                       tx.payee_address,
                       tx.payee_platform,
                       tx.platform_SN,
                       tx.amount,
                       tx.fee,
                       tx.extra_fee,
                       tx.description,
                       tx.created_at,
                       tx.cancel_at,
                       tx.received_at,
                       tx.completed_at,
                       tx.tx_hash,
                       tx.block_hash,
                       tx.block_height,
                       tx.confirmations,
                       tx.confirmations_required,
                       tx.target_currency_code,
                       tx.target_amount,
                       tx.standard_amount)
        hash_str = calculate_hash(value, salt, version)
    else:
        pass
    return hash_str
