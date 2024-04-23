import unittest
from moto import mock_dynamodb
import sys
sys.path.append('.')

import boto3
import uuid

from ewallet.model.wallet import Wallet
from ewallet.model.transaction import Transaction, TransactionType, TransactionStatus
from ewallet.repository.dynamodb_transaction_repository import DynamoDbTransactionRepository

class TestDynamoDbTransactionRepository(unittest.TestCase):

    @mock_dynamodb
    def create_mock_table(self):
        dynamodb = boto3.client('dynamodb')
        dynamodb.create_table(
            TableName='transactions',
            KeySchema=[
                {
                    'AttributeName': 'id',
                    'KeyType': 'HASH'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'id',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'wallet_id',
                    'AttributeType': 'S'
                }
            ],
            # add index for wallet id
            GlobalSecondaryIndexes=[
                {
                    'IndexName': 'transactions_wallet_index',
                    'KeySchema': [
                        {
                            'AttributeName': 'wallet_id',
                            'KeyType': 'HASH'
                        }
                    ],
                    'Projection': {
                        'ProjectionType': 'ALL'
                    },
                    'ProvisionedThroughput': {
                        'ReadCapacityUnits': 1,
                        'WriteCapacityUnits': 1
                    }
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 1,
                'WriteCapacityUnits': 1
            }
        )

    @mock_dynamodb
    def test_find(self):
        self.create_mock_table()

        dynamodb = boto3.client('dynamodb')

        wallet = Wallet("Test Wallet")
        wallet.id = str(uuid.uuid4())
        transaction = Transaction(wallet, 100, 'USD', TransactionType.TOP_UP)

        transaction_repository = DynamoDbTransactionRepository(dynamodb, 'transactions', 'transactions_wallet_index')
        id = transaction_repository.save(transaction)

        found_transaction = transaction_repository.find(id)
        self.assertIsNotNone(found_transaction)
        self.assertEqual(found_transaction.amount, 100)
        self.assertEqual(found_transaction.currency, 'USD')

    @mock_dynamodb
    def test_transaction_not_found(self):
        self.create_mock_table()

        dynamodb = boto3.client('dynamodb')
        transaction_repository = DynamoDbTransactionRepository(dynamodb, 'transactions', 'transactions_wallet_index')
        found_transaction = transaction_repository.find("123")
        self.assertIsNone(found_transaction)

    @mock_dynamodb
    def test_list_transactions_by_wallet(self):
        self.create_mock_table()

        dynamodb = boto3.client('dynamodb')

        wallet = Wallet("Test Wallet")
        wallet.id = str(uuid.uuid4())
        # print wallet id
        print(wallet.id)

        transaction = Transaction(wallet, 100, 'USD', TransactionType.TOP_UP)
        transaction2 = Transaction(wallet, 200, 'USD', TransactionType.TOP_UP)

        transaction_repository = DynamoDbTransactionRepository(dynamodb, 'transactions', 'transactions_wallet_index')
        transaction_repository.save(transaction)
        transaction_repository.save(transaction2)

        # Call method under test
        transactions = transaction_repository.list_transactions_by_wallet(wallet)

        # Assert results  
        self.assertEqual(len(transactions), 2)
        self.assertEqual(transactions[0].amount, 100)
        self.assertEqual(transactions[1].amount, 200)