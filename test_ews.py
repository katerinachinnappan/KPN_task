import unittest
import sys
from src import ews, initial_setup
import json
#from ews import get_emails
from exchangelib import Account, Credentials, Folder, Configuration, DELEGATE, ServiceAccount

class TestEWS(unittest.TestCase):
    """
    Our basic test class
    """
    def setUp(self):
        self.server = 'autodiscover-s.outlook.com'
        self.credentials = Credentials(username='testtask123@outlook.com', password='123testtask')
        self.config = Configuration(server=self.server, credentials=self.credentials)
        self.account = Account(primary_smtp_address='testtask123@outlook.com', config=self.config, autodiscover=False, access_type=DELEGATE)
        self.contains_domains = ['cisco', 'mail.onedrive', 'microsoft', 'student.vu', 'ucsc', 'yahoo'] #check all domains in inbox before moving to folders
        #self.contains_domains = []
        self.empty_domains = [] #check that inbox is empty (all emails moved to their respective folders)
        self.expected_output = {'email_info': [{
        'sender': 'abc@xyz.com',
        'subject': 'mock subject',
        'time received': '2019-03-08 15:05:44+00:00',
        'size': 58713
        }]}
        self.expected_folders = ['Processed', 'cisco', 'mail.onedrive', 'microsoft', 'student.vu', 'ucsc', 'yahoo']
        self.folder_names_domains = ['cisco', 'mail.onedrive', 'microsoft', 'student.vu', 'ucsc', 'yahoo']
        self.check_inbox_emails = []

    def test_get_emails(self):
    	email_domains = ews.get_emails(self.account)
    	self.assertEqual(email_domains, self.contains_domains) #check if ==
    	for domain in self.contains_domains: 
    	   self.assertIn(domain, email_domains, msg = None)#check if domain is in domain list


    def test_create_json_file(self):
        actual_output = ews.create_json_file('abc@xyz.com', 'mock subject', '2019-03-08 15:05:44+00:00', 58713, 1)
        self.assertEqual(self.expected_output, actual_output)

    def test_create_folders(self):
        actual_folders = ews.create_folders(self.folder_names_domains,self.account)
        self.assertEqual = (self.expected_folders, actual_folders)
        for folder in self.expected_folders:
            self.assertIn(folder, actual_folders, msg = None)

    def test_copy_and_move_emails(self):
        #inbox is expected to be empty after all emails are moved to their folders
        actual_emails = ews.copy_and_move_emails(self.folder_names_domains, self.account)
        self.assertEqual(self.check_inbox_emails, actual_emails)



if __name__ == '__main__':
    unittest.main()