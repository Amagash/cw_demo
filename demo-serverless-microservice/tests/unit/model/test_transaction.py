import unittest

import sys
sys.path.append('.')

import boto3

from ewallet.model.transaction import Transaction, TransactionType
from ewallet.model.wallet import Wallet

class TestTransaction(unittest.TestCase):

    def test_is_valid_currency_code(self):
        valid_currency_codes = ['EUR', 'USD', 'GBP']
        invalid_currency_codes = ['EURO', 'US', 'GB']

        for currency_code in valid_currency_codes:
            self.assertTrue(Transaction.is_valid_currency_code(currency_code))

        for currency_code in invalid_currency_codes:
            self.assertFalse(Transaction.is_valid_currency_code(currency_code))
        
    def test_formatted_amount(self):
        wallet = Wallet('EUR')

        transaction_1 = Transaction(wallet, 123.56, 'EUR', TransactionType.TOP_UP)
        self.assertEqual(transaction_1.formatted_amount, '123.56 EUR')

        transaction_2 = Transaction(wallet, 90, 'USD', TransactionType.PAYMENT)
        self.assertEqual(transaction_2.formatted_amount, '90.00 USD')
