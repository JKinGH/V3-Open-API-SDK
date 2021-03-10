# -*- coding: utf-8 -*-
from decimal import Decimal
from collections import namedtuple
from common.enum import CurrencyCode
# from .db import SummarizeRecord
import datetime

OMNI_NETWORK = 'omnilayer'
OMNI_USDT_COIN = 'usdt'

COLORED_CURRENCIES = (OMNI_USDT_COIN,)

CURRENCY_CODE = OMNI_USDT_COIN
CURRENCY_DECIMAL_PLACE = 8

BIP39 = 'bip39'
BIP32 = 'bip32'

ONCHAIN_NETWORKS = {
    'usdt': ('BTC', 'XTN'),
}

MIN_FEE_UNIT = 5000
DUST_THRESHOLD = 546
SATOSHI_PER_COIN = Decimal(int(1e8))

# pycoin.BUILT_IN_NETWORKS
NETCODE_MAP = {
    'btc': 'BTC',
    'ltc': 'LTC',
    'bcc': 'BTC',
    'bsv': 'BSV',
    'zec': 'ZEC',
    'bcd': 'BTC'}

NetworkValues = namedtuple('NetworkValues',
                           ('mainnet_code', 'testnet_code', 'hash_type', 'tx_version', 'block_interval'))

# btc and bch use different tx version
NETWORK_MAP = {
    CurrencyCode.btc.name: NetworkValues('BTC', 'XTN', 1, 1, 10 * 60),
    CurrencyCode.bcc.name: NetworkValues('BCH', 'tBCH', 65, 2, 10 * 60),
    CurrencyCode.bsv.name: NetworkValues('BSV', 'tBSV', 65, 2, 10 * 60),
    CurrencyCode.ltc.name: NetworkValues('LTC', 'XLT', 1, 2, round(2.5 * 60)),
    CurrencyCode.btg.name: NetworkValues('BTG', 'tBTG', 20289, 2, 10 * 60),
    CurrencyCode.dash.name: NetworkValues('DASH', 'tDASH', 1, 1, round(2.5 * 60)),
    CurrencyCode.zec.name: NetworkValues('ZEC', 'tZEC', 1, 4, round(2.5 * 60)),
    CurrencyCode.bcd.name: NetworkValues('BCD', 'tBCD', 1, 12, 10 * 60),
}


class Setting:

    id = 0
    ######-----后台传入参数-----######
    # 币种
    currency = ''
    # 扫币类型，1: 常规扫所有地址，2：特殊扫个别地址
    gather_type = 0
    #转出地址，即用户地址
    output_addr = ""
    #转入地址，即扫到某个地址
    input_addr = ""
    #矿工费代付地址: omni-usdt、ERC20扫币用
    paid_addr = None #omni-usdt：字典，ERC20：字符串
    #找零地址：omni-usdt专用
    dispenser_addr = ""
    #扫币时间范围：只扫区间有充币的地址
    start_at = "'2019-01-01 00:00:00'"
    end_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #扫币的最小金额：阈值,最小单位
    min_amount = 0
    ##矿工费: ETH: gasprice
    fee = 0
    ##币种精度
    decimal = 0
    ##调用时的时间戳
    ts = ""
    ##扫币地址数量
    addr_count = 0
    ##扫币总额
    total_amount = 0

    def str(self) -> str:
        info = ""
        info += "id:     " + str(self.id) + "\n"
        info += "currency:     " + self.currency + "\n"
        info += "gather_type:    " + str(self.gather_type) + "\n"
        info += "output_addr:     " + str(self.output_addr) + "\n"
        info += "input_addr:     " + str(self.input_addr) + "\n"
        info += "paid_addr:     " + str(self.paid_addr) + "\n"
        info += "dispenser_addr:      " + str(self.dispenser_addr) + "\n"
        info += "start_at:     " + str(self.start_at) + "\n"
        info += "end_at:      " + str(self.end_at) + "\n"
        info += "min_amount:      " + str(self.min_amount) + "\n"
        info += "fee:      " + str(self.fee ) + "\n"
        info += "decimal:      " + str(self.decimal ) + "\n"
        info += "ts:      " + str(self.ts ) + "\n"
        info += "total_amount:      " + str(self.total_amount ) + "\n"
        return info




def GenGatherInfo(setting:Setting):

    GatherInfo = {
        "id" : setting.id,
        ######-----后台传入参数-----######
        # 币种
        "currency" : setting.currency,
        # 扫币类型，1: 常规扫所有地址，2：特殊扫个别地址
        "gather_type" :setting.gather_type,
        # 转出地址，即用户地址
        "output_addr" :setting.output_addr,
        # 转入地址，即扫到某个地址
        "input_addr" :setting.input_addr,
        # 矿工费代付地址: omni-usdt、ERC20扫币用
        "paid_addr" :setting.paid_addr,
        # 找零地址：omni-usdt专用
        "dispenser_addr" :setting.dispenser_addr,
        # 扫币时间范围：只扫区间有充币的地址
        "start_at" :setting.start_at,
        "end_at" :setting.end_at,
        # 扫币的最小金额：阈值,最小单位
        "min_amount" :setting.min_amount,
        ##矿工费: ETH: gasprice
        "fee" :setting.fee,
        ##币种精度
        "decimal" :setting.decimal,
        ##调用时的时间戳
        "ts" :setting.ts,
        ##扫币地址数量
        "addr_count": setting.addr_count,
        #扫币总额
        "total_amount": setting.total_amount
    }

    return GatherInfo

class BroadcastInfo(Setting):
    # 币种
    # 扫币类型
    # 广播时间，以点击广播时间为准，
    # 扫币地址数量，以扫币结果地址数量为准
    # 扫币最小金额，自定义 / 默认
    # 矿工费，自定义 / 默认
    # 矿工费总额，总和
    total_fee = 0
    # 找零地址，币种为ETH / USDT - ERC20，XRP，EOS，无显示
    # 代付地址，币种为USDT - OMNI, USDT - ERC20，其他无显示
    # 转入地址，常规扫币类型显示为热钱包地址，特殊扫币显示为自定义地址
    # 转出地址，常归扫币类型显示为默认，特殊扫币显示为自定义地址
    #状态: 0:正常，1:# 失败(广播中断)，2:异常
    status = -1
    #是否需要写广播记录表
    need_write = False
    #广播错误信息
    err_msg = ""

    class Status:
        success = 1  # 正常
        fail = -1      # 失败(广播中断)

    def str(self) -> str:
        info = ""
        info += "currency:     " + self.currency + "\n"
        info += "gather_type:    " + str(self.gather_type) + "\n"
        info += "ts:    " + str(self.ts) + "\n"
        info += "addr_count:    " + str(self.addr_count) + "\n"
        info += "total_amount:    " + str(self.total_amount) + "\n"
        info += "min_amount:      " + str(self.min_amount) + "\n"
        info += "fee:      " + str(self.fee ) + "\n"
        info += "total_fee:      " + str(self.total_fee ) + "\n"
        info += "dispenser_addr:      " + str(self.dispenser_addr) + "\n"
        info += "paid_addr:     " + str(self.paid_addr) + "\n"
        info += "input_addr:     " + str(self.input_addr) + "\n"
        info += "output_addr:     " + str(self.output_addr) + "\n"
        info += "status:     " + str(self.status) + "\n"
        info += "need_write:      " + str(self.need_write) + "\n"
        info += "err_msg:      " + str(self.err_msg ) + "\n"
        return info

# 解析ETH/ERC20普通地址/ERC20合约地址的转账金额
# 返回 金额，精度，币种
def get_transfer_amount(transaction):

    method_len = 10 #0xa9059cbb
    param_len = 64
    ##ETH
    if transaction["value"] > 0 :
        return transaction["value"]
    ##ERC20普通地址/ERC20合约地址
    elif transaction["value"] == 0 and (len(transaction["data"]) == method_len + param_len*2 or len(transaction["data"]) == method_len + param_len*3 ):
        return eval('0x' + transaction["data"][method_len + param_len : method_len + param_len + param_len])
    else:
        return 0