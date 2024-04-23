import unittest
from moto import mock_dynamodb

import boto3
import sys
sys.path.append('.')

from ewallet.model.wallet import Wallet
from ewallet.repository.dynamodb_wallet_repository import DynamoDbWalletRepository

class TestDynamoDbWalletRepository(unittest.TestCase):

    @mock_dynamodb
    def create_mock_table(self):
        dynamodb = boto3.client('dynamodb')
        dynamodb.create_table(
            TableName='wallets',
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
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 1,
                'WriteCapacityUnits': 1
            }
        )

    @mock_dynamodb
    def test_save(self):
        self.create_mock_table()

        dynamodb = boto3.client('dynamodb')

        wallet = Wallet("Test Wallet")
        wallet_repository = DynamoDbWalletRepository(dynamodb, 'wallets')
        id = wallet_repository.save(wallet)
        self.assertIsNotNone(wallet.id)
        self.assertEqual(wallet.id, id)
        self.assertEqual(wallet.name, "Test Wallet")
        self.assertEqual(wallet.balance, {})
        self.assertEqual(wallet.transactions, [])

        saved_wallet = dynamodb.get_item(TableName='wallets', Key={'id': {'S': id}})
        self.assertEqual(saved_wallet['Item']['name']['S'], wallet.name)

    @mock_dynamodb
    def test_find(self):
        self.create_mock_table()

        dynamodb = boto3.client('dynamodb')

        wallet = Wallet("Test Wallet")
        wallet_repository = DynamoDbWalletRepository(dynamodb, 'wallets')
        id = wallet_repository.save(wallet)

        found_wallet = wallet_repository.find(id)
        self.assertIsNotNone(found_wallet)
        self.assertEqual(found_wallet.id, id)
        self.assertEqual(found_wallet.name, "Test Wallet")
        self.assertEqual(found_wallet.balance, {})
        self.assertEqual(found_wallet.transactions, [])

    @mock_dynamodb
    def test_wallet_not_found(self):
        self.create_mock_table()

        dynamodb = boto3.client('dynamodb')
        wallet_repository = DynamoDbWalletRepository(dynamodb, 'wallets')
        found_wallet = wallet_repository.find("123")
        self.assertIsNone(found_wallet)