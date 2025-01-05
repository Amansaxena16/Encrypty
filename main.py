from cryptography.fernet import Fernet


def takePath():
    path = input('Enter the Path of the File : ')  # Take the path of the file from the user
    return path
    
    
def encryptFile(path):
    with open('key.key','rb') as key_file:  # Open the file as binary mode
        key = key_file.read()
        
    fernet = Fernet(key)  # Create the Fernet Object
    
    with open(path,'rb') as file:  # Open the file to read it in binary mode
        originalFile = file.read()
        
    encrypt = fernet.encrypt(originalFile)  # Encrypt the file
    
    with open(path,'wb') as encryptedFile:   # Open the file to write it in binary mode
        encryptedFile.write(encrypt)
    
    
def decryptFile(path):
    pass

def main():
    path = takePath()
    encryptFile(path)
    
    
main()
    