
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
	mean_values = []
	while k < 20:#a random key size
		rows = len(newstring)/k
		columns = k
		temp = [[0 for x in range(columns)] for x in range(rows)]

		for i in range (rows):
			for j in range(columns):
				temp[i][j] = newstring[(i*k)+j]


		summary = 0.0
		for i in range (k):
			summary = summary + IC(column(temp,i))

		mean_values.append(summary/columns)
		k = k+1
	return mean_values.index(max(mean_values)) + 2

def IC(column):
	n = 26
	k = len(column)
	summary = 0.0
	for i in range(26):
		x = column.count(i)
		summary = summary + x*(x-1)/float(k*(k-1))
	return summary

def column(matrix, i):
    return [row[i] for row in matrix]


file = open('vigenere.txt','r')
string = file.read()

newstring = encode(string)

k = Friedman(newstring)
print(k)
