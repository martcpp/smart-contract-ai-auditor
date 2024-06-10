import re
import contract_extractor import fectch_contract_source_code



def preprocess_source_code(source_code):
    # Remove comments and extra whitespace
    source_code = re.sub(r'/\*.*?\*/', '', source_code, flags=re.DOTALL)  # Remove block comments
    source_code = re.sub(r'//.*', '', source_code)  # Remove line comments
    source_code = re.sub(r'\s+', ' ', source_code)  # Remove extra whitespace
    return source_code



contract_address = "0x06012c8cf97bead5deae237070f9587f8e7a266d"

source_code = fectch_contract_source_code(contract_address)

cleaned_code = preprocess_source_code(source_code)
print(cleaned_code)
