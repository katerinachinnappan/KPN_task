# Run this on a machine where you want to test connectivity to exchange server
# And to see if python exchangelib works

import logging
import requests
import http.client as http_client
import json
import collections
from collections import OrderedDict

# Below enables a ton of debug output for investigation 

http_client.HTTPConnection.debuglevel = 1
logging.basicConfig()
#logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
#requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

from exchangelib import DELEGATE, Account, Credentials, Folder, Configuration, ServiceAccount, IMPERSONATION
from exchangelib.protocol import BaseProtocol, NoVerifyHTTPAdapter
BaseProtocol.HTTP_ADAPTER_CLS = NoVerifyHTTPAdapter


#### GET EMAILS FROM INBOX #####
def get_emails(Account):
	file_name_counter = 0 #counter for file names
	start = '@'
	end = '.'
	domains = []
	for email in account.inbox.all():
		print("Email info")
		print("sender: ", email.sender.email_address, "received: ", 
		email.datetime_received, "subject: ", email.subject, "content: ", email.text_body)
		domains.append(email.sender.email_address[email.sender.email_address.find(start)+len(start):email.sender.email_address.rfind(end)])
		file_name_counter = file_name_counter + 1
		# create json file for every fetched email 
		#create_json_file(email.sender.email_address, email.subject, str(email.datetime_received), email.size, file_name_counter)
	#print (domains)
	#remove all duplicate domains from the domains list.
	domains_no_duplicate = list(OrderedDict.fromkeys(domains))
	return domains_no_duplicate



#### CREATE JSON_FILES FOR EVERY EMAIL ####
def create_json_file(sender, subject, time_received, email_size, file_name_counter):
	#construct email dict object
	data = {}  
	data['email_info'] = []  
	data['email_info'].append({  
    'sender': sender,
    'subject': subject,
    'time received': time_received,
    'size': email_size
	})

	file = open(sender+str(file_name_counter)+".json", "a+")
	file.write(json.dumps(data))
	file.close()


#### CREATE FOLDER ####
def create_folders(domains):

	# fetch all folders from the inbox and append to a list
	folders = []
	for f in account.inbox.walk():
		folders.append(f.name)
	print (folders)

	#check if folder Processed is in the inbox. 
	#If not, create it otherwise return message to console.
	if not "Processed" in folders:
		print("Creating Processed Folder")
		processed_folder = Folder(name='Processed', parent=account.inbox)
		print(processed_folder)
		processed_folder.save()
	else:
		print("Processed folder already exists.")

	# iterate through domain list and check if the folder with domain as the name already exists in inbox.
	#If not, create it, otherwise, return message to console.
	for domain in domains:
		if not domain in folders:
			print("Creating "+domain+" Folder")
			domain_folder = Folder(name=domain, parent=account.inbox)
			domain_folder.save()
		else:
			print(domain+" folder already exists")


#### COPY EMAIL TO PROCESSED FOLDER ####
def copy_and_move_emails(domains):
	# list to store new emails from inbox
	email_copies = []
	for email in account.inbox.all():
		email_copies.append(email)

	# copy emails from list to processed folder
	processed_folder  = account.inbox / "Processed"
	for email in email_copies:
			email.copy(processed_folder)

	#move all emails from inbox to their domain-name folders
	for email in account.inbox.all():
		for domain in domains:
			domain_folder = account.inbox / domain
			if domain in email.sender.email_address:
				print(email.sender.email_address)
				email.move(domain_folder)


#### ACCOUNT & CREDENTIALS SETUP
# If the server doesn't support autodiscover, or you want to avoid the overhead of autodiscover,
# Account & Credentials set up
credentials = Credentials(username='testtask123@outlook.com', password='123testtask')
server = 'autodiscover-s.outlook.com'
config = Configuration(server=server, credentials=credentials)
account = Account(primary_smtp_address='testtask123@outlook.com', config=config, autodiscover=False, access_type=DELEGATE)

#fetch emails & get domains
domains = get_emails(account)
print (domains)
#create folders
create_folders(domains)
#copy email to processed folder, move emails from inbox to respective domain-name folders
copy_and_move_emails(domains)







