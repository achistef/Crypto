import zipfile

file = open('english.txt','r')
zFile=zipfile.ZipFile('test_zip.zip')

for line in file:
	try:
		password = line.strip()
		zFile.extractall(pwd=password)
		print("Password: " + password)
		break
	except:
		pass
	