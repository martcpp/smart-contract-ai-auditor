import requests
from decouple import config

api_key = config('ETHERSCAN_API_KEY')


def fectch_contract_source_code(contract_address):
    url = f"https://api.etherscan.io/api?module=contract&action=getsourcecode&address={contract_address}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    contract_code = data['result'][0]['SourceCode']
    contract_name = data['result'][0]['ContractName']
    contract_ABI = data['result'][0]['ABI']
    
    return contract_name, contract_code, contract_ABI


if __name__ == "__main__":
    contract_address = "0x06012c8cf97bead5deae237070f9587f8e7a266d"
    contract_name, contract_code, contract_abi = fectch_contract_source_code(contract_address)
    print(contract_name)
    print(contract_code)
    print (contract_abi)    





