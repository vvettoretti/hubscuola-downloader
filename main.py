import sys, unicodedata
from hubyoung_lib import HubYoung

print("*" * 10, "HubYoung downloader by @vvettoretti", "*" * 10)

try:
    username = sys.argv[1]
    password = sys.argv[2]
except:
    username = input("Enter email\n")
    password = input("Enter password\n")
h = HubYoung(username, password)

print("Logged in successfully")

library = h.get_library()
books_to_download = []
for book in library:
    print(book["title"])
    print("ID -", book["id"])
    if input("Download? (y/n)\n").lower() == "y":
        books_to_download.append(book)

for book in books_to_download:
    print(f"Downloading {book['title']}... (this may take a while)")
    book["title"] =  unicodedata.normalize('NFD', book["title"].lower().replace(' ', '_')).encode('ascii', 'ignore')
    h.download_book(str(book["id"]), str(book["id"]) + "_" + book["title"] + ".pdf")
