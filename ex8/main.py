import crypt

file = open('password.txt','r')

temp = file.read().partition(":")
username = temp[0]
password = temp[2].partition(":")[0]

file.close()
file = open('password.txt','r')
salt = file.read().partition("$")[2].partition("$")[2].partition("$")[0]

encryption = "$6$" + str(salt) + "$"
for i in range(1,1000000):
	x = '{0:06d}'.format(i) 
	encrypted = crypt.crypt(x,encryption)
	if encrypted == password :
		print("Password: " + str(i))
		break

