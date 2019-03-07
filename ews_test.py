# Run this on a machine where you want to test connectivity to exchange server
# And to see if python exchangelib works

import logging
import requests
import http.client as http_client

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

# If the server doesn't support autodiscover, or you want to avoid the overhead of autodiscover,
credentials = Credentials(username='testtask123@outlook.com', password='123testtask')
server = 'autodiscover-s.outlook.com'

config = Configuration(server=server, credentials=credentials)
account = Account(primary_smtp_address='testtask123@outlook.com', config=config, autodiscover=False, access_type=DELEGATE)

# for msg in account.inbox.all():
# 	print("The email address of the sender is: ")
# 	print(msg.sender.email_address)

#print(account.root.tree())

print('fetching emails from inbox')
for item in account.inbox.all().order_by('-datetime_received')[:100]:
    print(item.subject, item.sender, item.datetime_received)