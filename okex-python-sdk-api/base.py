# -*- coding:utf8 -*-
from web3 import Web3, HTTPProvider


class BaseEthDao(object):
    def __init__(self, http_addr=''):
        self.web3 = self.get_web3(http_addr)

    def get_web3(self, http_addr):
        if not http_addr:
            http_addr = 'https://kovan.infura.io/v3/a2c0328ef48c495da2a911a3ceef3917'
        return Web3(HTTPProvider(http_addr))

    def to_check_addr(self, addr):
        return Web3.toChecksumAddress(addr)

    def check_addr(self, addr):
        return Web3.isChecksumAddress(addr)

    def get_balance(self, addr):
        try:
            balance = self.web3.eth.getBalance(addr)
            return 0, balance
        except Exception as e:
            return -1, str(e)