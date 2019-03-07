# Run this on a machine where you want to test connectivity to exchange server
# And to see if python exchangelib works

import logging
import requests
import http.client as http_client
import json

# Below enables a ton of debug output for investigation 

http_client.HTTPConnection.debuglevel = 1
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

from exchangelib import DELEGATE, Account, Credentials, Configuration, ServiceAccount, IMPERSONATION
from exchangelib.protocol import BaseProtocol, NoVerifyHTTPAdapter
BaseProtocol.HTTP_ADAPTER_CLS = NoVerifyHTTPAdapter


#### GET EMAILS FROM INBOX #####
def get_emails(Account):
	file_name_counter = 0 #counter for file names
	for email in account.inbox.all():
		print("Email info")
		print("sender: ", email.sender.email_address, "received: ", 
			email.datetime_received, "subject: ", email.subject, "content: ", email.text_body)
		file_name_counter = file_name_counter + 1
		# create json file for every fetched email 
		create_json_file(email.sender.email_address, email.subject, file_name_counter)



#### CREATE JSON_FILES FOR EVERY EMAIL ####
def create_json_file(sender, subject, file_name_counter):
	file = open(sender+str(file_name_counter)+".json", "a+")
	file.write(json.dumps({"sender": sender, "subject": subject}))
	file.close()
	print(file_name_counter);



#### ACCOUNT & CREDENTIALS SETUP
# If the server doesn't support autodiscover, or you want to avoid the overhead of autodiscover,
# Account & Credentials set up
credentials = Credentials(username='testtask123@outlook.com', password='123testtask')
server = 'autodiscover-s.outlook.com'
config = Configuration(server=server, credentials=credentials)
account = Account(primary_smtp_address='testtask123@outlook.com', config=config, autodiscover=False, access_type=DELEGATE)

#fetch emails
get_emails(account)






