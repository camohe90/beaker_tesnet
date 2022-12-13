import contract
from pyteal import *
from beaker import *
from beaker.client import ApplicationClient, Network
from beaker.client.api_providers import AlgoNode
import os
from dotenv import load_dotenv
from algosdk.atomic_transaction_composer import AccountTransactionSigner
from algosdk import mnemonic

load_dotenv()

PASSPHRASE = os.environ.get("PASSPHRASE")


# Open the file where we're saving the app ID
text_file = open("./artifacts/app_id", "r")
app_id = int(text_file.read())
text_file.close()

# Get the accounts trough the sandbox client
user = AccountTransactionSigner(mnemonic.to_private_key(PASSPHRASE))

# Create the Application Client
app_client = ApplicationClient(
  client = AlgoNode(Network.TestNet).algod(),
  app = contract.MyApplication(version=7),
  app_id = app_id,
  signer = user,
)

## Call a method
result = app_client.call(contract.MyApplication.hello, name="Camilo")
print(result.return_value)