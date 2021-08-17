import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'BFauLcu_q5IAAAAAAAAAATnUVQWKSumYYlkxsYicbAWDYrKFJGs0LAYBeBmCtsYL'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to be transferred to dropbox: ")
    file_to = input("Enter the full file path to be transferred in dropbox: ")  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)
    print("File has been moved")

#if __name__ == '__main__':
main()