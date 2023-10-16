"""Sudoku email script"""

from base64 import b64encode
from os import environ

from dotenv import load_dotenv
from mailjet_rest import Client


with open("random_letters.csv", "rb") as file:
    base64_content = b64encode(file.read()).decode("utf-8")

load_dotenv()
mailjet_v3 = Client(auth=(environ["API_KEY"], environ["API_SECRET_KEY"]), version="v3")
contacts_data = mailjet_v3.contactslistsignup.get()
emails = [data["Email"] for data in contacts_data.json()["Data"] if data["ListID"] == 10368497]

mailjet_v3_1 = Client(auth=(environ["API_KEY"], environ["API_SECRET_KEY"]), version="v3.1")

data = {
"Messages": [{
    "From": {
        "Email": "sudokusubscription@gmail.com",
        "Name": "SudokuSubscription"
            },
    "To": [ {"Email": email, "Name": "Sudoku Subscriber"} for email in emails],
    "Subject": "",
    "TextPart": "",
    "HTMLPart": "",
    "Attachments": [{
        "ContentType": "application/vnd.ms-excel",
        "Filename": "random_letters.csv",
        "Base64Content": base64_content
                    }],
        "CustomID": "subscription #4"
              }]
        }

result = mailjet_v3_1.send.create(data=data)
print(result.status_code)
print(result.json())
