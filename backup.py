import dropbox

class TransferData:
    def __init__(self, accesstoken):
        self.accesstoken= accesstoken
    def upload(self, source, dest):
        dbx = dropbox.Dropbox(self.accesstoken)
        f = open(source, 'rb')
        dbx.files_upload(f.read(), dest)

def main():
    source = input("Enter source: ")
    dest = input("Enter destination: ")
    access = "GBW_REx5NdAAAAAAAAAAAT5peZAtaaGW5dAhSC6f3Jt_yO3SAIXVwF7yQ5NUY_SX"
    transfer = TransferData(access)
    transfer.upload(source, dest)
    print("All done")

main()