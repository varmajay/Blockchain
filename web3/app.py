import json
import logging
from pprint import pformat
from web3 import Web3
import requests

from web3.auto import w3
from web3.contract import get_event_data

infura_url = "https://mainnet.infura.io/v3/c71703b7b9734ff68884062db8d377f0"

web3 = Web3(Web3.HTTPProvider(infura_url))

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


## Constants for the smart contract
# This is just for example purposes.
ERC721_ABI_TRANSFER_EVENT = json.loads(
  requests.get(
    url="https://gist.githubusercontent.com/bartcode/0e03bbec375c3de54a49e8bee88ddcf8/raw/65fc003ba0291310a11af99b485946f8ad562a9b/erc721-transfer-abi.json"
  ).content
)
ERC721_KECCAK = web3.keccak(text="Transfer(address,address,uint256)")

## Looping through the blocks (let's take a single one for now)
for block_number in [14188382]:
  block_info = web3.eth.get_block(block_number)

  for transaction in block_info.transactions:
    receipt = web3.eth.get_transaction_receipt(transaction)

    for log in receipt.logs:
      if log.topics and log.topics[0] == ERC721_KECCAK and log.data == "0x":
        logger.info("Found transfer event:\n%s", pformat(dict(get_event_data(web3.codec, ERC721_ABI_TRANSFER_EVENT, log))))