# KPN - Technical Task

Extend python script. Using credentials from a Microsoft Outlook account, fetch all emails from the inbox. Create a folder "processed". When fetching emails, watch for the domain names in the sender-email and create folders for each specific domain-email with the domain as the folder name. Copy all emails (read/unread) from inbox and place in folder processed. Move all emails from inbox to their specific domain-name folders.

## Getting Started

These instructions will get you a copy of the script up and running on your local machine for development and testing purposes. 

### Prerequisites

Before running the script, make sure to have python3.x.x installed on your machine. This can be easily done with help of pip,

```
sudo easy_install pip
```

Install required packages (requests, exchangelib) using pip3
```
sudo pip3 install requests
```

```
sudo pip3 install exchangelib
```
### Run Script

To start and run the script:

```
python3 ews_test.py
```

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

## Authors

**Katerina Chinnappan** 

