
class ConfigStaging():
    env = 'staging'
    testnet = True

    # 节点url
    web3_url = 'http://172.31.40.203:8545' #'https://kovan.infura.io/v3/9ae1dea879574029b2dca7aed72599aa'  #kovan
    chainId = 1337  ## kovan 42
    # usdt-erc20合约地址
    usdt_contract_address = '0x60797581c14f6d4c8395aecb9d12dd88adccac6b'  # 0x264901c98188e65a9b8b26a7ba023ee9b122fc94 # kovan
    # ETH/ERC20-USDT 普通地址扫币接收地址
    #collection_address = '0xbe425B2A990dE7280bD52c3aF225Df57566D9ba8'
    # ERC20-USDT 普通地址扫币矿工费代付地址
    #miner_fee_address = '0xbe425B2A990dE7280bD52c3aF225Df57566D9ba8'
    # ERC20-USDT 普通地址扫币的gas
    gas_limit = 50000
    # ERC20-USDT 合约地址扫币的gas
    contract_gas_limit = 140000
    # 链上交易费单价
    #gas_price = 10
    # 最大归集金额(单位:USDT)
    #max_collection_amount = 9999999
    # 被归集地址中最小金额
    #threshold = 0
    # 生成地址个数,普通地址扫币需要
    count = 13
    # ETH/ERC20-USDT 普通地址需要扫币的地址，为空时默认从数据库读取已充值的地址
    # configuration_address = [('0x21c3d3e9147e72a729ba510e715b761886817458',), ('0xbe425b2a990de7280bd52c3af225df57566d9ba1',)]
    #configuration_address = []

    #  ETH/ERC20-USDT 普通地址主私钥文件路径
    master_private_key_filename = "/Users/gts/workspace/mobi/wallet_gather/master_private_key.txt"
    # ERC20-USDT 普通地址扫币矿工费代付地址私钥文件路径
    miner_fee_address_key_filename = "/Users/gts/workspace/mobi/wallet_gather/miner_fee_address_key.txt"
    # 未签名文件存放的目录
    sign_file_dir = "/data/wallet_gather/gather"

    db_user = 'mobime'
    db_password = 't8TpwP6dufajwCGLgk8qhUCT'
    db_name = 'stagingmobi'
    db_new_admin_name = 'mobi_new_admin'
    db_host = 'staging-rds.c4ryivjbggn7.ap-east-1.rds.amazonaws.com'
    db_port = 5432

    ### 用于usdt-erc20合约地址第二阶段的扫币, user_proxy_invoker 调用 user_proxy_contract 扫币到热钱包地址
    user_proxy_contract = '0xd199a4d73a0af5533346ee8957649315c3bfa6fc'
    user_proxy_invoker = '0x2d33694f8cfad9e9cff55145af72264e779e6daf'
    I_user_config_contract_list = [
        ##  [I-user config contract,invoker,version,H-user proxy contract]
        ## 每修改一次I中的H,I中对应的version会 +1 ,erc20扫币签名时需要传入对应version值
        ["0xe3a71bd127637e5a116d246a2af8a3499a1f7539", "", 0, ""],
        ["0x70e331711b3af478c248ecac2c83fcf850a6a9ca", "", 0, ""],
    ]
    ## F-invoker地址对应私钥的存放路径,键无须修改,只需修改值
    invoker_private_key_filename = {
        "0x83b6e54985664e7ecc03210ae2a86c4c9fb7e4c0" : "/Users/gts/workspace/mobi/wallet_gather/0x83b6e54985664e7ecc03210ae2a86c4c9fb7e4c0.txt",
        "0x2d33694f8cfad9e9cff55145af72264e779e6daf" : "/Users/gts/workspace/mobi/wallet_gather/0x2d33694f8cfad9e9cff55145af72264e779e6daf.txt"
    }
    user_proxy_invoker_private_key_filename = {
        user_proxy_invoker: "/Users/gts/workspace/mobi/wallet_gather/0x2d33694f8cfad9e9cff55145af72264e779e6daf.txt"
    }

    btc = "btc"
    ltc = "ltc"
    bcc = "bcc"
    btg = "btg"
    dash = "dash"
    zec  = "zec"
    bcd = "bcd"
    eth = "eth"
    usdt_erc20 = "usdt-erc20"
    usdt = "usdt"

    currencies = {btc, ltc, bcc, btg, dash, zec, bcd,eth,usdt_erc20,usdt}

    gather_file_dir = "/Users/wujinquan/workspace/mobi/wallet_gather/gather"

    unsigned_erc20_general_tx_file = "unsigned_erc20_general_transaction.json"
    unsigned_erc20_general_fee_file = "unsigned_erc20_general_fee_transaction.json"
    unsigned_eth_general_tx_file = "unsigned_eth_general_transaction.json"

    fee_unit = {
        btc: "sat",
        ltc: "sat",
        bcc: "sat",
        btg: "sat",
        zec: "sat",
        bcd: "sat",
        eth: "gwei",
        usdt_erc20: "gwei",
        usdt: "sat"
    }

    celery_broker = 'amqp://mobi:123456@127.0.0.1:5672/dev-broker'
    celery_backend = 'redis://127.0.0.1/1'


class ConfigProduction():
    env = 'prod'
    testnet = False

    # 节点url
    web3_url = 'https://mainnet.infura.io/v3/9ae1dea879574029b2dca7aed72599aa'
    chainId = 1  ## mainnet
    # usdt-erc20合约地址
    usdt_contract_address = '0xdac17f958d2ee523a2206206994597c13d831ec7'
    # ETH/ERC20-USDT 普通地址扫币接收地址
    # 9/F
    # collection_address = '0x847f9346196BDf1c68dF08765331F40dB681A812'
    # hotwallet
    #collection_address = '0x68c5508d598b72d69bd84707a37a1227c42eb70f'
    # ERC20-USDT 普通地址扫币矿工费代付地址
    #miner_fee_address = '0x1bfbfb5b61ebea0626465e1afad1c82bda4b110a'
    # ERC20-USDT 普通地址扫币的gas
    gas_limit = 50000
    # ERC20-USDT 合约地址扫币的gas
    contract_gas_limit = 140000
    # 链上交易费单价
    #gas_price = 42
    # 最大归集金额(单位:USDT)
    #max_collection_amount = 9999999
    # 被归集地址中最小金额
    #threshold = 499
    # 生成地址个数,普通地址扫币需要
    count = 100000
    # ETH/ERC20-USDT 普通地址需要扫币的地址，为空时默认从数据库读取已充值的地址
    # configuration_address = [('0x21c3d3e9147e72a729ba510e715b761886817458',), ('0xbe425b2a990de7280bd52c3af225df57566d9ba1',)]
    #configuration_address = []

    #  ETH/ERC20-USDT 普通地址主私钥文件路径
    master_private_key_filename = "/Volumes/Mobi ETH Normal/private key(main).txt"
    # ERC20-USDT 普通地址扫币矿工费代付地址私钥文件路径
    miner_fee_address_key_filename = "/Volumes/Mobi ETH Normal/miner private key.txt"
    # 未签名文件存放的目录
    sign_file_dir = "/data/wallet_gather/gather"

    # 数据库
    db_user = 'admin'
    db_password = 'jTTgkDrCd2yq&O7'
    db_name = 'mobime-pre'
    db_new_admin_name = 'mobiadmin'
    db_host = 'mobi-prod.clrbcuxwdzhx.ap-northeast-1.rds.amazonaws.com'
    db_port = 5432

    ### 用于usdt-erc20合约地址第二阶段的扫币, user_proxy_invoker 调用 user_proxy_contract 扫币到热钱包地址
    user_proxy_contract = '0xcca10e6bb18a311514f30d7ac9efecb9f4482b7b'
    user_proxy_invoker = '0x800bcd39cd5b7136f12e0d6c26628e737d67b956'
    I_user_config_contract_list = [
        ##  [I-user config contract,invoker,version,H-user proxy contract]
        ## 每修改一次I中的H,I中对应的version会 +1 ,erc20扫币签名时需要传入对应version值
        ["0x136dcab229c9620532ef5122b98bef4f2d1583e4","", 0 , ""],
        ["0xa483faf9c651984f2e36fa39acdf3fe9637931f8","", 0 , ""],
        ["0x0f3d6a8386ef951a4fe5c7d72fc6405bd365a8d8","", 0 , ""],
        ["0x08119014da8a284310381fa41ea489d692f76b09","", 0 , ""],
        ["0x4af0aea55754C7F8e4Eefe23D4Ab1B2fb509C21F","", 0 , ""],
        ["0xd725aadadc5f7cf4896db9dc5930d335155af2f8","", 0 , ""],
    ]
    ## F-invoker地址对应私钥的存放路径,键无须修改,只需修改路径
    invoker_private_key_filename = {
        "0xd9ac7ec3c3f535a30b874dfc3a63a45708adfb62": "/Volumes/xxx/key1.txt",
        "0x8489b2de35147dee89995ea160696317fbcac34f": "/Volumes/xxx/key2.txt",
        "0x40045ea095dcdb7c0301aaeb8de011e2607979c4": "/Volumes/xxx/key3.txt",
        "0xb81b992acf8ddc521ace3324644cb8fcdaf6b350": "/Volumes/xxx/key4.txt",
        "0x7ecf4935a0672e8e372a0e20f9f16686cc606b63": "/Volumes/xxx/key5.txt",
    }
    user_proxy_invoker_private_key_filename = {
        user_proxy_invoker: "/Volumes/xxx/key6.txt"
    }

    btc = "btc"
    ltc = "ltc"
    bcc = "bcc"
    btg = "btg"
    dash = "dash"
    zec = "zec"
    bcd = "bcd"
    eth = "eth"
    usdt_erc20 = "usdt-erc20"
    usdt = "usdt"
    currencies = {btc, ltc, bcc, btg, dash, zec, bcd, eth, usdt_erc20, usdt}

    gather_file_dir = "/data/wallet_gather/gather_dir"
    unsigned_erc20_general_tx_file = "unsigned_erc20_general_transaction.json"
    unsigned_erc20_general_fee_file = "unsigned_erc20_general_fee_transaction.json"
    unsigned_eth_general_tx_file = "unsigned_eth_general_transaction.json"

    fee_unit = {
        btc: "sat",
        ltc: "sat",
        bcc: "sat",
        btg: "sat",
        zec: "sat",
        bcd: "sat",
        eth: "gwei",
        usdt_erc20: "gwei",
        usdt: "sat"
    }

    pairs = {
        'eth_veth': '0x50969C5B74AB455B3A35225cf5CB9BcefDB92559',
    }

    erc20_toekn_addr = {
        'weth': '0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2',
        'veth': '0xc3d088842dcf02c13699f936bb83dfbbc6f721ab',
    }

### change config for diff env
deploy_config = ConfigProduction
#deploy_config = ConfigStaging()
