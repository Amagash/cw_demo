import unittest

from ewallet.model.wallet import Wallet
from ewallet.model.transaction import TransactionType, TransactionStatus, Transaction
import os

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

    def test_export_transactions(self):
         wallet = Wallet('test_wallet')
         wallet.add_transaction(100, 'USD', TransactionType.TOP_UP)
         wallet.add_transaction(200, 'EUR', TransactionType.TOP_UP)
         wallet.add_transaction(300, 'GBP', TransactionType.TOP_UP)
         wallet.export_transactions()
         self.assertTrue(os.path.exists('transactions.csv'))
         os.remove('transactions.csv')
         self.assertFalse(os.path.exists('transactions.csv'))

    # TASK 3: Generating E-Wallet Test Cases

    # create a function that tests top_up
    def test_top_up(self):
        wallet = Wallet('test_wallet')
        wallet.top_up(100, 'USD')
        self.assertEqual(wallet.balance['USD'], 100)
        self.assertEqual(len(wallet.transactions), 1)
        self.assertEqual(wallet.transactions[0].amount, 100)
        self.assertEqual(wallet.transactions[0].currency, 'USD')
        self.assertEqual(wallet.transactions[0].type, TransactionType.TOP_UP)
        self.assertEqual(wallet.transactions[0].status, TransactionStatus.PENDING)

    def test_transfer_balances(self):
        # Arrange 
        wallet1 = Wallet('wallet1')
        wallet2 = Wallet('wallet2')  

        wallet1.top_up(100, 'USD')

        # Act
        wallet1.transfer(50, 'USD', wallet2)

        # Assert balances
        self.assertEqual(wallet1.balance['USD'], 50)
        self.assertEqual(wallet2.balance['USD'], 50)
