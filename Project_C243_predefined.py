from web3 import Web3 #import the Web3 module from Web3 library

url = 'https://mainnet.infura.io/v3/cded6e6690d04259b05137dd10b170c3'

web3=Web3(Web3.HTTPProvider(url))

latest_block=web3.eth.getBlock('latest')

print("\nLatest Block of ethereum blockchain : ",latest_block)

block_transaction_count=web3.eth.get_block_transaction_count(14098206)

print("\nNumber of transactions happened in the block : ",block_transaction_count)

Transaction_fee=web3.eth.fee_history(block_count=396,newest_block='latest',reward_percentiles=None)

print("\nNumber of transactions happened in the block : ",Transaction_fee)