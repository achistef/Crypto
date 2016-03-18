
dictionary = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
              'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

frequencies = ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'R', 'H', 'D', 'L', 'U','C', 'M', 'F', 'Y', 'W', 'G',
				'P', 'B', 'V', 'K', 'X', 'Q', 'J', 'Z']

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

		for i in range(rows):
			for j in range(columns):
				temp[i][j] = newstring[(i*k)+j]


		summary = 0.0
		for i in range (k):
			summary = summary + IC(column(temp,i))

		mean_values.append(summary/columns)
		k = k+1
	return mean_values.index(max(mean_values)) + 2

def IC(aColumn):
	n = 26
	k = len(aColumn)
	summary = 0.0
	for i in range(26):
		x = aColumn.count(i)
		summary = summary + x*(x-1)/float(k*(k-1))
	return summary

def column(matrix, i):
    return [row[i] for row in matrix]


file = open('vigenere.txt','r')
string = file.read()

newstring = encode(string)

key_length = Friedman(newstring)

row_size = (len(string)/key_length)
sets = [[0 for x in range(key_length)] for i in range(row_size)]

k = 0
for x in range(row_size):
	for i in range(key_length):
		sets[x][i] = newstring[k]
		k += 1

shift=[]
for i in range(key_length):
	col = column(sets,i)
	counts = [0 for x in range(26)]	 
	for j in col:
		counts[j] += 1
	maximum = counts.index(max(counts))
	temp = maximum - dictionary.index(frequencies[0])
	if  temp < 0 :
		shift.append(temp + 26)
	else:
		shift.append(temp)


real_string_num = []
for i in range(len(newstring)):
	temp_i = newstring[i] - shift[i%key_length]
	if temp_i < 0:
		real_string_num.append(temp_i + 26)
	else:
		real_string_num.append(temp_i)
real_key = decode(shift)
real_string = decode(real_string_num)
print("Key:" + ''.join(real_key))
print (''.join(real_string))