#importing hashlib for the sha256 encryption method and pyperclip to copy output into clipboard.
import hashlib, pyperclip
from time import sleep

#String converter into bytes because .sha256() method takes bytes as parameter.
def stringToBytes(string: str):
    stringBytes = str.encode(string)
    return stringBytes

#Hashing function using sha256 encryption.
def hashing(string: str):
    shaEncryption = hashlib.sha256(stringToBytes(string))
    encryptedString = shaEncryption.hexdigest()
    return encryptedString

#Method in case user input isn't correct.
def fileExtensionHandler(fileName):
    extension = fileName[-4:]
    if extension == '.txt':
        return fileName
    else:
        fileName += '.txt'
        return fileName

#Method to get string through a .txt file.
def getString(fileName):
    with open(fileExtensionHandler(fileName)) as f:
        output = f.read()
    return output

#Driver code/asking for credentials.
def main():
    userInput = input('text file or not, (y/n) : ')
    if userInput == 'y':
        fileName = input(' name ? : ')
        userInput = getString(fileName)
        output = hashing(userInput)
        print(output)
        print()
        copying = input('wanna copy the encryption ? (y/n) : ')
        if copying.lower()=='y' or 'yes':
            pyperclip.copy(output)
            print('Copied to clipboard ! ')
            sleep(3)
            print()
        if copying.lower()== 'n' or 'no':
            print('bye ! ')
            print()
    if userInput.lower() == 'n':
        userInput = input("What's the string u wanna encryt ? : ")
        output = hashing(userInput)
        print()
        print(output)
        print()
        copying = input("wanna copy it ? (y/n) : ")
        if copying == 'y' or 'yes':
            pyperclip.copy(output)
            print()
            print('Copied')
            print()
            sleep(3)
        if copying == 'n' or 'no':
            print('bye')

main()
