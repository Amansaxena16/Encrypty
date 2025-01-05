from cryptography.fernet import Fernet

def readKey():
    with open('key.key','rb') as key_file:  # Open the file as binary mode
        key = key_file.read()
        
    return key

def encryptFile(path,key):
    
    with open(path,'rb') as file:  # Open the file to read it in binary mode
        originalFile = file.read()
        
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
        
    
def decryptFile(path,key):
    
    fernet = Fernet(key)
    
    with open(path,'rb') as encryptedFile:
        encrypted_Content = encryptedFile.read()
        
    try:
        fernet.decrypt(encrypted_Content)  # Check if the file is already decrypted
        print('File is already decrypted')
    except Exception as e:
        pass
    
    try:    
        decrypted = fernet.decrypt(encrypted_Content) # Decrypt the file

        with open(path,'wb') as decryptedFile: # Open the file to write it in binary mode
            decryptedFile.write(decrypted)
    except Exception as e:
        print(f"Invalid Key: {e}")
        

def main():
    
    path = '/home/aman/Work/Encrypty/test.txt'
    operation = input('Do you want to Encrypt(e) or Decrypt(d) the file : ').lower()
    
    try:
        if(operation != 'e' and operation != 'd'):
            raise ValueError('Invalid Input')
        if(operation == 'e'):
            key = readKey()
            encryptFile(path,key)
        else:
            key = readKey()
            decryptFile(path,key)   
    except Exception as e:
        print(f"An Error Occured : {e}")
    
    
main()
    