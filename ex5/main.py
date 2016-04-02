from Crypto.Cipher import AES
from random import randint

key = "LoveCryptography"
message = "WeNeedPerfectTen"
#ECB MODE
obj = AES.new(key,AES.MODE_ECB)
ciphertext1=obj.encrypt(message)
#CBC MODE
obj2 = AES.new(key,AES.MODE_CBC,"WorksLikeACharm!")
encryptedtext1=obj2.encrypt(message)

def flip(message):
	m1 = binascii.hexlify(bytes(message,'UTF-8'))#bytes method for python3 compatibility
	m2 = bin(int(m1, 16))[2:]
	#change random bit
	random = randint(0,len(m2)-1)
	if m2[random] == '0':
		randomBit = '1'
	else:
		randomBit = '0'
	return m2[:random] + randomBit + m2[random+1:]

def encrypt(m):
	new = []
	i = 0
	#encrypt changed message
	while i < len(m):
		newint = int(m[i:i+8], 2)
		if newint < 100:
			new.append('0'.join(str(newint)))
		else:
			new.append(str(newint))
		i = i + 8

	return ''.join(new)

def summary(ciphertext,c):
	results = []
	count = 0
	for i in range(len(ciphertext)):
		if ciphertext[i] != c[i]:
			count = count + 1
	results.append(count)

	return results

import binascii

ciphertext2=binascii.hexlify(ciphertext1)
ciphertext = bin(int(ciphertext2, 16))[2:]

encryptedtext2=binascii.hexlify(encryptedtext1)
encryptedtext = bin(int(encryptedtext2, 16))[2:]

resultsECB = []
resultsCBC = []
#try for 50 repetitions
for i in range(50):

	flipped = flip(message)#flip a random bit
	newstring = encrypt(flipped)#encrypt flipped message

	encryptedECB = obj.encrypt(newstring)
	encryptedCBC = obj2.encrypt(newstring)

	hexadecimalECB = binascii.hexlify(encryptedECB)
	hexadecimalCBC = binascii.hexlify(encryptedCBC)

	binaryECB = bin(int(hexadecimalECB, 16))[2:]
	binaryCBC = bin(int(hexadecimalCBC, 16))[2:]

	resultsECB = summary(ciphertext,binaryECB)
	resultsCBC = summary(encryptedtext,binaryCBC)

resultECB = sum(resultsECB[::])
resultCBC = sum(resultsCBC[::])

print("Mean number of different bits for ECB : " + str(float(resultECB)/len(resultsECB)))
print("Mean number of different bits for CBC : " + str(float(resultCBC)/len(resultsCBC)))