import unittest
import sys
from ews_test import get_emails
from exchangelib import Account, Credentials, Folder

class TestEWS(unittest.TestCase):
    """
    Our basic test class
    """
    def setUp(self):
    	self.credentials = Credentials(username='testtask123@outlook.com', password='123testtask')
    	self.account = Account(primary_smtp_address='testtask123@outlook.com', credentials=self.credentials, autodiscover=True)

    def test_get_email_domains(self):

    	email_domains = get_emails(self.account)
    	check_domains = []
    	self.assertEqual(email_domains, check_domains)


if __name__ == '__main__':
    unittest.main()