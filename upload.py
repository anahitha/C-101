import dropbox
import os

class TransferData:
    def __init__(self, accesstoken):
        self.accesstoken= accesstoken
    def upload(self, source):
        dbx = dropbox.Dropbox(self.accesstoken)
        for roots, dirs, files in os.walk:
            for filename in files:
                path = root + filename
                dest = '/TEST/' + path
                f = open(path, 'rb')
                dbx.files_upload(f.read(), dest, mode = WriteMode('overwrite'))

def main():
    source = input("Enter source: ")
    access = input("Enter access token: ")
    transfer = TransferData(access)
    transfer.upload(source)
    print("All done")

main()