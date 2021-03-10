from enum import Enum, IntEnum, unique

'''
默认情况下，不同的成员值允许相同。但是两个相同值的成员，第二个成员的名称被视作第一个成员的别名
'''


@unique
class BtcKeyName(IntEnum):
    vincent = 1
    # 隔离见证
    segregated_witness = 2
    legacy = 3


class CurrencyCode(Enum):
    btc = 'BTC'
    ltc = 'LTC'
    bcc = 'BCH'
    bsv = 'BSV'
    zec = 'ZEC'
    bcd = 'BCD'
    btg = 'BTG'
    dash = 'DASH'
    usdt = "USDT"



class BchDiverged(Enum):
    normal = 0
    # 分叉前
    before_diverged = 1
    # 分叉后
    after_diverged = 2


class SighHashType(Enum):
    SIGHASH_ALL = 1
    SIGHASH_NONE = 2
    SIGHASH_SINGLE = 3
    SIGHASH_FORKID = 0x40
    SIGHASH_ANYONECANPAY = 0x80


class TxType(Enum):
    """ 交易类型 """
    PAYMENT = 3  # 3, 支付(目前只有商城订单支付)
    REFUND = 4  # 4, 系统退款
    OFFCHAIN = 5  # 5, offchain转账
    ONCHAIN = 6  # 6, onchain转账
    ONCHAIN_DEPOSIT = 7  # 7, onchain充值（付款人非平台用户，区块同步而来）
    PLATFORM = 9  # 9, 平台转账（pro,exc,justpay,mobi之间相互转账）
    EXCHANGE = 11  # 11,兑换
    EXCHANGE_UNDO = 12  # 12,兑换撤销
    WAVECREST = 13  # 13,wave crest 消费交易
    MONTHLY_FEE = 14  # 14,monthly fee 月费
    TWITTER_SEND = 15  # 15,twitter 转账
    TWITTER_REFUND = 16  # 16,twitter 退款
    WITHDRAW = 17  # 17,payment withdraw
    WAVECREST_DEPOSIT = 18  # 18,wavecrest deposit
    OTC_SEND = 19  # OTC send (seller to system account/system account to buyer)
    OTC_REFUND = 20  # OTC Refund(system account refund seller)


class TxStatus(Enum):
    PENDING = 1  #: 1,  用户创建交易（还未付款）
    PAID = 2  #: 2,  用户创建交易（已经付款）
    HANDING = 3  #: 3,  用户创建交易（已经付款-SPV钱包已发出币）
    COMPLETE = 4  #: 4,  交易完成
    CANCELED = 5  #: 5,  交易关闭/取消
    WAIT_SIGNUP = 6  #: 6,  用户创建交易（已经付款-收款人尚未注册）
    INVALID = 7  #: 7,  交易无效
    UNCONFIRMED = 8  #: 8,  未确认的交易（0个确认）
    CONFIRMING = 9  #: 9,  确认中的交易（1~3个确认）
    REJECTED = 10  #: 10, 拒绝的交易
    DELAYED = 11  #: 11, 用户创建交易（交易被受理，余额+确认中余额足够，等待余额足够时，自动完成）


class FeatureType(Enum):
    GATHER_USDT = 1
    GATHER_BTC = 2
    GATHER_BTC_CALC_FEE = 3
    GATHER_LTC = 4
    GATHER_BCC = 5
    GATHER_BCC_BEFORE_DIVERGED = 6
    GATHER_BCC_AFTER_DIVERGED = 7
    GATHER_ZEC = 8
    GATHER_BCD = 9
    GATHER_BSV = 10
    GATHER_DASH = 11
    GATHER_ZEC_CALC_FEE = 18

    ASSET_DASH = 20
    ASSET_USDT = 21
    ASSET_BSV = 22
    ASSET_BCC = 23

    UTXO_BTC = 30
    UTXO_BCC = 31
    UTXO_LTC = 32
    UTXO_ZEC = 33
    UTXO_BSV = 34
    UTXO_BTG = 35

    CALC_HASH_BY_SN = 100
