
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
	k = 7
	found = 0
	while found == 0:
		rows = len(newstring)/k
		columns = k
	    temp = [[0 for x in range(columns)] for x in range(rows)]

		for i in range (rows):
			for j in range(columns):
                temp[i][j] = newstring[(i*k)+j]


        axi = 0
		for i in range (k):
            axi = axi + IC(column(temp,i))
			#if IC(column(temp,i)) - 0.067 < 0.05:
				#found = 1
				#return k

        print(axi/columns)
		k = k+1
		found = 1
    return k

def IC(column):
	n = 26
	k = len(column)
    sum = 0.0
    for i in range(26):
        x = column.count(i)
        sum = sum + (double(x*(x-1)/k*(k-1))
    return sum

def column(matrix, i):
    return [row[i] for row in matrix]


file = open('vigenere.txt','r')
string = file.read()

newstring = encode(string)

k = Friedman(newstring)
