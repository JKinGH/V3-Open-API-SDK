# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,scoped_session
from sqlalchemy.ext.declarative import declarative_base
from config.conf import postgres
import settings
import warnings,json
from contextlib import contextmanager
from sqlalchemy import (BigInteger, Column, DateTime, Integer, SmallInteger, String, Text, text)
from config.config import deploy_config as config
from .const import BroadcastInfo
import decimal

db_path = settings.data_path + '/foo.db'

with warnings.catch_warnings(record=True):
    postgres_engine = create_engine(postgres.uri, echo=False, pool_size=postgres.pool_size, pool_recycle=30)
    sqlite_engine = create_engine('sqlite:///' + db_path, echo=True)
    pass

postgres_session = sessionmaker(bind=postgres_engine)

@contextmanager
def pg_session():
    session = postgres_session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


sqlite_session = sessionmaker(bind=sqlite_engine)

Base = declarative_base()
# Base.metadata.create_all(engine)

class SummarizeRecord(Base):
    __tablename__ = 'summarize_record'

    id = Column(Integer, primary_key=True)
    currency_code = Column(String, nullable=False)
    type = Column(SmallInteger, default=1)
    status = Column(SmallInteger, default=0)
    path = Column(String)  # 扫币文件路径
    errmsg = Column(Text, nullable=True) #错误信息,扫币出错时有值
    created_at = Column(DateTime(True), nullable=False, server_default=text("now()"))

    class Type:
        normal = 1  # 常规扫币
        abnormal = 2  # 非常规扫币
        broadcast = 3  # 广播

    class Status:
        handing = 0  # 处理中
        fail = -1  # 失败
        success = 1  # 成功

    class Msg:
        success = ""

class BroadcastRecord(Base):
    __tablename__ = 'broadcast_record'

    id = Column(Integer, primary_key=True)
    currency_code = Column(String, nullable=False)
    type = Column(SmallInteger, default=1)
    addr_count = Column(Integer)
    total_amount = Column(BigInteger)
    min_amount = Column(BigInteger)
    fee = Column(BigInteger)
    total_fee = Column(BigInteger)
    paid_addr = Column(String)
    dispenser_addr = Column(String)
    input_addr = Column(String)
    output_addr = Column(String)
    created_at = Column(DateTime(True), nullable=False, server_default=text("now()"))

class AdminSetting(Base):
    __tablename__ = 'admin_setting'

    id = Column(Integer, primary_key=True)
    key = Column(String(32), nullable=False, unique=True)
    value = Column(Text, nullable=False)

class Currency(Base):
    __tablename__ = 'currency'

    id = Column(Integer, primary_key=True)
    code = Column(String)
    decimal_place = Column(Integer)

def CreateSession(picasso_url):

    engine = create_engine(picasso_url, echo=False, pool_size=5, pool_recycle=30)
    db_session = scoped_session(sessionmaker(bind=engine))

    return db_session

def UpdateSummarizeRecord(id,status,path,msg):
    picasso_url = 'postgresql://' + config.db_user + ':' + config.db_password + '@' + config.db_host + ':' + str(
        config.db_port) + '/' + config.db_new_admin_name
    db_session = CreateSession(picasso_url)
    data = db_session.query(SummarizeRecord).filter_by(id=id).scalar()
    if status:
        data.status = status
    if path:
        data.path = path
    if msg:
        data.errmsg = msg
    db_session.commit()

def AddBroadcastRecord(bcinfo:BroadcastInfo):
    picasso_url = 'postgresql://' + config.db_user + ':' + config.db_password + '@' + config.db_host + ':' + str(
        config.db_port) + '/' + config.db_new_admin_name
    db_session = CreateSession(picasso_url)

    record = BroadcastRecord()
    record.currency_code = bcinfo.currency
    record.type = bcinfo.gather_type
    record.addr_count = bcinfo.addr_count
    record.total_amount = bcinfo.total_amount
    record.min_amount = bcinfo.min_amount
    record.fee = bcinfo.fee
    record.total_fee = bcinfo.total_fee
    record.paid_addr = bcinfo.paid_addr
    record.dispenser_addr = bcinfo.dispenser_addr
    record.input_addr = bcinfo.input_addr
    record.output_addr = bcinfo.output_addr

    db_session.add(record)
    db_session.commit()


class SystemSetting(Base):
    __tablename__ = 'system_setting'

    id = Column(Integer, primary_key=True)
    key = Column(String(32), nullable=False, unique=True)
    value = Column(Text, nullable=False)

def BlockExplorerSetting():
    picasso_url = 'postgresql://' + config.db_user + ':' + config.db_password + '@' + config.db_host + ':' + str(
        config.db_port) + '/' + config.db_name
    db_session = CreateSession(picasso_url)
    block_explorer_type = 'bitcoind'
    block_explorer_setting = db_session.query(SystemSetting).filter_by(key=block_explorer_type).scalar()
    if block_explorer_setting is None:
        raise Exception('there is no key {config} in system_setting table'.format(config=block_explorer_type))
    else:
        explorer_config = json.loads(block_explorer_setting.value)
        db_session.close()

        return explorer_config

def AddMinerFeeAddress(new_miner_fee_address):
    picasso_url = 'postgresql://' + config.db_user + ':' + config.db_password + '@' + config.db_host + ':' + str(
        config.db_port) + '/' + config.db_name
    db_session = CreateSession(picasso_url)
    key = 'miner_fee_address'
    miner_fee_address = db_session.query(SystemSetting).filter_by(key=key).scalar()
    if miner_fee_address is None:
        raise Exception('there is no key {key} in system_setting table'.format(key=key))
    else:
        miner_fee_address_tmp = json.loads(miner_fee_address.value)
        if new_miner_fee_address not in miner_fee_address_tmp:
            miner_fee_address_tmp.append(new_miner_fee_address)
            miner_fee_address.value = json.dumps(miner_fee_address_tmp)
            db_session.commit()

    db_session.close()

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        super(DecimalEncoder, self).default(o)