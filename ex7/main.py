import zipfile

myFile = open('english.txt','r')
zFile=zipfile.ZipFile('test_zip.zip')

for line in myFile:
	try:
		password = line.strip()
		zFile.extractall(pwd=bytes(password,'UTF-8'))
		print("Password: " + password)
		break
	except:
		pass
		