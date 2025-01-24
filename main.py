from cryptography.fernet import Fernet

def readKey():
    with open('key.key','rb') as key_file:  # Open the file as binary mode
        key = key_file.read()
        
    return key

def encryptFile(path):
    
    with open(path,'rb') as file:  # Open the file to read it in binary mode
        originalFile = file.read()
    key = readKey()
    fernet = Fernet(key)
    
    try:
        fernet.decrypt(originalFile) # Check if the file is already encrypted
        print('File is already encrypted')
        return
    except Exception as e:
        pass
        
    encrypt = fernet.encrypt(originalFile)  # Encrypt the file
    
    with open(path,'wb') as encryptedFile:   # Open the file to write it in binary mode
        encryptedFile.write(encrypt)
        
    
def decryptFile(path):
    
    with open(path,'rb') as file:
        file_Content = file.read()
    
    try:    
        key = readKey()
        fernet = Fernet(key)
        decrypted = fernet.decrypt(file_Content) # Decrypt the file

        with open(path,'wb') as decryptedFile: # Open the file to write it in binary mode
            decryptedFile.write(decrypted)
            print("File decrypted successfully.")
            
    except Exception as e:
        print(f"Invalid Key: {e}")
        return
    