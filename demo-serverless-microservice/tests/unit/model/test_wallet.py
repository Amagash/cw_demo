import unittest
import sys
sys.path.append('.')

import boto3
from ewallet.model.wallet import Wallet
from ewallet.model.transaction import TransactionType, TransactionStatus

class WalletTest(unittest.TestCase):

    def test_wallet_creation(self):
        wallet = Wallet('test_wallet')
        self.assertDictEqual(wallet.balance, {})
        self.assertCountEqual(wallet.transactions, [])
        self.assertEqual(wallet.id, None)
        self.assertEqual(wallet.name, 'test_wallet')

    def test_list_balance(self):
        wallet = Wallet('test_wallet')
        wallet.add_transaction(100, 'USD', TransactionType.TOP_UP)
        wallet.add_transaction(300, 'EUR', TransactionType.TOP_UP)
        wallet.add_transaction(50, 'GBP', TransactionType.TOP_UP)
        wallet.withdraw(50, 'GBP')

        balance = wallet.list_balance()

        self.assertListEqual(balance, ['USD 100.00', 'EUR 300.00', 'GBP 0.00'])

    # TASK 1: Enhancing E-wallet functionality with CodeWhisperer
    def test_get_total_transactions(self):
        wallet = Wallet('test_wallet')
        wallet.add_transaction(100, 'USD', TransactionType.TOP_UP)
        wallet.add_transaction(200, 'EUR', TransactionType.TOP_UP)
        wallet.add_transaction(300, 'GBP', TransactionType.TOP_UP)
        total_transactions = wallet.get_total_transactions()
        self.assertEqual(total_transactions, 3)
  
    def test_filter_transactions(self):
        wallet = Wallet('test_wallet')
        wallet.add_transaction(100, 'USD', TransactionType.TOP_UP)
        wallet.add_transaction(200, 'EUR', TransactionType.TOP_UP)
        wallet.add_transaction(300, 'GBP', TransactionType.TOP_UP)
        wallet.add_transaction(-15, 'USD', TransactionType.PAYMENT)
        wallet.add_transaction(-20, 'EUR', TransactionType.PAYMENT)
        wallet.add_transaction(-25, 'GBP', TransactionType.PAYMENT)
        wallet.withdraw(50, 'GBP')
        wallet.add_transaction(100, 'USD', TransactionType.TRANSFER)
        wallet.add_transaction(200, 'EUR', TransactionType.TRANSFER)
        wallet.add_transaction(300, 'GBP', TransactionType.TRANSFER)
        filtered_transactions = wallet.filter_transactions(TransactionType.TOP_UP)
        self.assertEqual(len(filtered_transactions), 3)
        self.assertEqual(filtered_transactions[0].type, TransactionType.TOP_UP)

 
    # TASK 3: Generating E-wallet test cases