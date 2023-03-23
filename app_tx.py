from web3 import Web3
UrlRPC = "https://mainnet.infura.io/v3/47b829e7e62f4ccfa9fe9dbd1bde1714"

web3 = Web3(Web3.HTTPProvider(UrlRPC))
print(web3.is_connected())
block = web3.eth.get_block('latest')
print(web3.to_hex(block.hash))


balance = web3.eth.get_balance("0x1f9090aaE28b8a3dCeaDf281B0F12828e676c326")

print(Web3.from_wei(balance, 'ether'))