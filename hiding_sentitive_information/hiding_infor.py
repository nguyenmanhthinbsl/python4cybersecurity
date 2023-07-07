import json
from pathlib import Path

path = Path(__file__).with_name('credentials.json')

with path.open('r') as credentials_file:
    data = json.load(credentials_file)
    credentials_file.close()
    
email = data['email_credentials']['email']
password = data['email_credentials']['password'] 

print(email, password)   