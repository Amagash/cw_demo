import os
import sys
import boto3
import json
import pytest
import unittest

from moto import mock_dynamodb
import sys
sys.path.append('.')

import boto3

from ewallet.controller.create_wallet import lambda_handler

class TestCreateWalletLambda(unittest.TestCase):

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

    def test_initialization(aws_credentials):
        event = {}
        context = None

        os.environ['DDB_TABLE'] = ''

        payload = lambda_handler(event, context)

        assert payload['statusCode'] == 500

    def test_empty_event(aws_credentials):
        event = {}
        context = None

        os.environ['WALLETS_TABLE'] = 'wallets'

        payload = lambda_handler(event, context)

        assert payload['statusCode'] == 400

    @mock_dynamodb
    def test_valid_request(self):
        event = { 'body': '{"name": "My Wallet"}' }
        context = None

        os.environ['WALLETS_TABLE'] = 'wallets'

        self.create_mock_table()

        payload = lambda_handler(event, context)
        wallet = json.loads(payload['body'])
        '{"balance": {}, "transactions": [], "id": "c0399676-890d-4750-b413-a508d435661e", "name": "My Wallet"}'

        self.assertEqual(payload['statusCode'], 201)
        self.assertEqual(wallet['name'], 'My Wallet')
        self.assertIsNotNone(wallet['id'])
        self.assertEqual(wallet['balance'], {})
        self.assertEqual(wallet['transactions'], [])
        