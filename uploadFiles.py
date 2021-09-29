import os
import dropbox

class TransferData:
    def __init__(self,access_Token):
     self.access_Token = access_Token

    def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_Token)
        
        file = open(file_from,'rb')
        dbx.files_upload(file.read(),file_to)

 
def name():
    access_Token = 'sl.A5RbU9_PmLHlG_WnMXOgUUvpj04nP9n5o-VAD7ea9_3oOV_h_TtGWKhZTon3piMZk9qyh5BlYn5m771WKlfHy6IOZpapWRX2WqkLHpDxLdJBUBs0-bBwT4dpQye42mKJAJwVehm5Rn8'
    transferdata = TransferData(access_Token)

    file_from = input('ENTER THE FILES THAT YOU WANT TO TRANSFER') 
    file_to = input("ENTER THE FULL PATH TO UPLOAD TO THE DROPBOX")
    transferdata.upload_file(file_from,file_to)
    print('File Has Been Moved')

name()