import initial_setup
from exchangelib import DELEGATE, Account, Credentials, Folder, Configuration, ServiceAccount, IMPERSONATION

#start cleanup
for folder in initial_setup.account.inbox.walk():
	folder.delete()
print("deleted all subfolders from inbox")