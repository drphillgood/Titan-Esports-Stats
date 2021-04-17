import googleapiclient
from GoogleSheetsAPI import DOCUMENT
import csv
import os

# league = (os.environ["league"])
league = 'Divinity'

if league == "Divinity":
    code = ''
    path = f'../{league}/{league}_merged.csv'
elif league == "Olympian":
    code = ''
    path = f'../{league}/{league}_merged.csv'
else:
    print(f"{league} is not a correct input. Try 'Divinity' or 'Olympian'")

DOCUMENT = DOCUMENT(code)
DOCUMENT.writeRange("source", "A:BK", list(csv.reader(open(path))))
print(f"Document successfully sent to {league}'s Google Sheet.")
