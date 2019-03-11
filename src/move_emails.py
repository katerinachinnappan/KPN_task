import initial_setup

#move all emails from processed to inbox for teting purposes
processed_folder  = initial_setup.account.inbox / "Processed"
for email in processed_folder.all():
	email.move(initial_setup.account.inbox)
print("moved all emails from processed to inbox")