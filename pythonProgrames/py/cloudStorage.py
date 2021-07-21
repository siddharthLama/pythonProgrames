import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token
       
    def upload_file(self,file_from, file_to):
        """upload a file to DropBox using Api v2 
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from,'rb') as f:
            dbx.files_upload(f.read(),file_to)

def main():
    access_token = 'A-6BvMN99AgAAAAAAAAAAbfsPJhXX1vpsW9sNmXZErTpxIqfvtTpGo9LyKZgDnQj'
    transferData = TransferData(access_token)

    file_from = input("Enter the file to upload")
    file_to = input("Enter the dropbox path") # the full path to upload the file to , including file name

    # ApI v2
    transferData.upload_file(file_from,file_to)

if __name__ == "__main__":
    main()