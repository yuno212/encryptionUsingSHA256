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
def getString(fileName: str):
    with open(fileExtensionHandler(fileName)) as f:
        output = f.read()
    return output

#Driver code/asking for credentials.
def main():
    output = hashing(userInput)
    userInput = input("Is your content located in a text file or not (y/n)")
    if userInput.lower() == 'y' or 'yes':
        userInput = getStringThroughTextFile(fileName)
        print(output)
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
           
    else:
        userInput = input("Which string do you want to encrypt ? :")
        print(userInput,"/ after encryption string becomes :  ")
        print()
        print(output)
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
