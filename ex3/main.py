
dictionary = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
              'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def encode(string):
    coded_text = []
    for letter in string:
        coded_text.append(dictionary.index(letter))
    return coded_text

def decode(list):
    decoded_text = []
    for i in list:
        decoded_text.append(dictionary[i])
    return decoded_text

def Friedman(newstring):
	k = 2
	found = 0
	while found == 0:
		rows = len(newstring)/k
		columns = k
		temp = [[0 for x in range(columns)] for x in range(rows)]

		for i in range (rows):
			for j in range(columns):
				temp[i][j] = newstring[(i*k)+j] 

		for i in in range(k):
			if IC(temp[][i]) - 0.067 < 0.05:
				found = 1
				return k		
		k++

def IC(column):
	n = 26
	l = n
	k = len(column)

		


file = open('vigenere.txt','r')
string = file.read()

newstring = encode(string)

k = Friedman(newstring)



