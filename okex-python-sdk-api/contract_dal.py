from .base import BaseEthDao

def compile_source_file(file_path):
    with open(file_path, 'rt') as f:
       source = f.read()
    # return compile_source(source)
    return source

class ContractDal(BaseEthDao):
    def __init__(self, contract_addr="", abi="", http_addr=""):
        super().__init__(http_addr)
        self.addr = contract_addr
        self.abi = abi

    def set_addr(self, addr):
        self.addr = addr

    def set_abi(self, abi):
        self.abi = abi

    def get_contract_instance(self, addr="", abi=""):
        if not addr:
            addr = self.addr
        if not abi:
            abi = self.abi
        if not self.check_addr(addr):
            addr = self.to_check_addr(addr)
        try:
            contract_instance = self.web3.eth.contract(address=addr, abi=abi)
            return 0, contract_instance
        except Exception as e:
            return -1, str(e)

    def get_abi(self, file_path):
        # compiled_sol = compile_source_file(sol_path)
        # contract_id, contract_interface = compiled_sol.popitem()
        # return contract_interface["abi"]
        with open(file_path, 'rt') as f:
            source = f.read()
        return source

    def compile_sol(self, file_path):
        compiled_sol = compile_source_file(file_path)
        contract_id, contract_interface = compiled_sol.popitem()
        return contract_id, contract_interface