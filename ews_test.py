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
	file_name_counter = 0
	for email in account.inbox.all():
		print("Email info")
		print("sender: ", email.sender.email_address, "received: ", 
			email.datetime_received, "subject: ", email.subject, "content: ", email.text_body)
		file = open(email.sender.email_address+str(file_name_counter)+".json", "a+")
		file.write(json.dumps({"sender": email.sender.email_address, "subject": email.subject}))
		file.close()
		file_name_counter = file_name_counter + 1
	# dummy_json = open("dummy_json.json", "a+")
	# dummy_json.write(json.dumps({"sender": email.sender.email_address, "received": email.datetime_received, "subject": email.subject}))
	# dummy_json.close()



#def create_json_file(Account)



#### ACCOUNT & CREDENTIALS SETUP
# If the server doesn't support autodiscover, or you want to avoid the overhead of autodiscover,
# Account & Credentials set up
credentials = Credentials(username='testtask123@outlook.com', password='123testtask')
server = 'autodiscover-s.outlook.com'
config = Configuration(server=server, credentials=credentials)
account = Account(primary_smtp_address='testtask123@outlook.com', config=config, autodiscover=False, access_type=DELEGATE)

#fetch emails
get_emails(account)






