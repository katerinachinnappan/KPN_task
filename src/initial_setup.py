from exchangelib import DELEGATE, Account, Credentials, Folder, Configuration, ServiceAccount, IMPERSONATION

#INITIAL SET UP
credentials = Credentials(username='testtask123@outlook.com', password='123testtask')
server = 'autodiscover-s.outlook.com'
config = Configuration(server=server, credentials=credentials)
account = Account(primary_smtp_address='testtask123@outlook.com', config=config, autodiscover=False, access_type=DELEGATE)