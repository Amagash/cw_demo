import json
import logging
import os
import boto3

from ewallet.repository.dynamodb_wallet_repository import DynamoDbWalletRepository
from ewallet.repository.base_repository import BaseRepository
from ewallet.model.wallet import Wallet

# create a logger at the INFO level
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# function to get wallet repository using dynamodb client and table name
def get_wallet_repository(dynamodb_client, table_name):
    return DynamoDbWalletRepository(dynamodb_client, table_name)

# function to list wallets using the wallet table name
def list_wallets(table_name):
    # get the wallet repository using the table name
    wallet_repository = get_wallet_repository(boto3.client('dynamodb'), table_name)
    # get all wallets
    wallets = wallet_repository.list_wallets()
    # return the wallets
    return wallets

# create the lambda handler
def lambda_handler(event, context):
    # get the table name from environment variable
    table_name = os.environ['TABLE_NAME']
    # list the wallets
    wallets = list_wallets(table_name)
    # return the wallets
    return {
        'statusCode': 200,
        'body': json.dumps(wallets)
    }