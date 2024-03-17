from trivium import Trivium
from trivium import hex_to_bits, bits_to_hex
import os
import random
import time

def randomIV():
    result = ""
    for i in range(20):
        result += hex[random.randint(0, 15)]
    return result

def encrypt(file):
    rIV = randomIV()
    IV = hex_to_bits(rIV)[::-1]

    # Read plaintext file
    f = open(testData + file, "rb")
    lines = f.readlines()
    content = ""
    for line in lines:
        content += line.decode("latin-1")

    # Create ciphertext and save it
    trivium_encoder = Trivium(KEY, IV)
    cipher = trivium_encoder.encrypt(content)
    f = open(encryptData + file, "w")
    f.write(rIV + bits_to_hex(cipher))
    f.close()

def decrypt(file):
    f = open(encryptData + file, "r")
    content = f.readline()

    IV = hex_to_bits(content[:20])[::-1] # The first 20 hexa numbers are IV

    # Create plaintext and save it
    trivium_decoder = Trivium(KEY, IV)
    f = open(decryptData + file, "w")
    f.write(trivium_decoder.decrypt(hex_to_bits(content[20:])))
    f.close()

def solution(file):
    startTime = time.time()
    
    encrypt(file)
    decrypt(file)

    t = time.time() - startTime
    print(file, ":", t, "sec")
    return t

if __name__ == "__main__":
    hex = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    
    KEY = hex_to_bits("0F62B5085BAE0154A7FA")[::-1]

    testData = "TestData/"
    encryptData = "EncryptData/"
    decryptData = "DecryptData/"

    totalTime = 0.0
    listFile = os.listdir(os.path.expanduser(testData)) # TestData contains only file 
    for file in listFile:
        totalTime += solution(file)

    print("TOTAL TIME:", totalTime, "sec")