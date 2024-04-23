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

from ewallet.controller.withdraw import validate_payload

class TestWithdraw(unittest.TestCase):

  def test_missing_iban(self):
    payload = {'amount': '10.00', 'currency': 'EUR'}
    errors = validate_payload(payload)
    self.assertEqual(errors, ['iban is missing'])

  def test_missing_amount(self):  
    payload = {'iban': 'IBAN123', 'currency': 'EUR'}
    errors = validate_payload(payload)  
    self.assertEqual(errors, ['amount is missing'])

  def test_invalid_amount_format(self):
    payload = {'iban': 'IBAN123', 'amount': '10', 'currency': 'EUR'} 
    errors = validate_payload(payload)
    self.assertEqual(errors, ['Invalid amount'])

  def test_missing_currency(self):
    payload = {'iban': 'IBAN123', 'amount': '10.00'}
    errors = validate_payload(payload)
    self.assertEqual(errors, ['currency is missing'])

  def test_valid_payload(self):
    valid_payload = {'iban': 'IBAN123', 'amount': '10.00', 'currency': 'EUR'}
    errors = validate_payload(valid_payload)
    self.assertEqual(errors, [])

if __name__ == '__main__':
  unittest.main()
