#importing hashlib for the sha256 encryption method and pyperclip to copy output into clipboard.
import hashlib, pyperclip
from time import *

#String converter into bytes because .sha256() method takes bytes as parameter.
def stringToBytes(string):
    stringBytes = str.encode(string)
    return stringBytes

#Hashing function using sha256 encryption.
def hashing(string):
    shaEncryption = hashlib.sha256(stringToBytes(string))
    encryptedString = shaEncryption.hexdigest()
    return encryptedString

def getText(txtFile):
    with open('file.txt') as f:
    contents = f.read()
    return contents
     
        
#Driver code/asking for credentials.
def main():
    userInput = input('Which string do you want to encrypt ? :')
    print(userInput,"/ after encryption string becomes :  ")
    print()
    print(hashing(userInput))
    print()
    copyOrNot = input('do you want to copy the encrypted string yes/no ? : ')

    if copyOrNot.lower() == 'y' or 'yes':
        #Method to actually copy the encrypted string.
        pyperclip.copy(hashing(userInput))
        print()
        print('Copied to clipboard ! ')
        sleep(3)
    elif copyOrNot.lower() == 'n' or 'no':
        print("It's Ok, goodbye")
        sleep(3)

    print()
    print('Thanks for using this program !')

#Calling main() function to start the program
main()
