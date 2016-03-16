from collections import deque

aDict = dict(zip('abcdefghijklmnopqrstuvwxyz.!?()-ABCDEFGHIJKLMNOPQRSTUVWXYZ', 
                              ['00000','00001','00010','00011','00100',
                              '00101','00110','00111','01000',
                              '01001','01010','01011','01100','01101','01110','01111',
                              '10000','10001','10010','10011',
                              '10100','10101','10110','10111',
                              '11000','11001',
                              '11010','11011','11100','11101','11110','11111',
                              '00000','00001','00010','00011','00100',
                              '00101','00110','00111','01000',
                              '01001','01010','01011','01100','01101','01110','01111',
                              '10000','10001','10010','10011',
                              '10100','10101','10110','10111',
                              '11000','11001'])) 

def list_to_string(l):
    return ''.join(str(e) for e in l)

def string_xor(btext,key): 
    cipher = []
    if len(btext)!=len(key):
        print("key and message must have the same lengths!")
        return 0
    for i in range(len(btext)):
        cipher.append(int(btext[i])^int(key[i])) #xoring bit-bit
    cipher = ''.join(str(e) for e in cipher)
    return cipher

def text_enc(text):
    text = text[::-1]
    length = len(text)
    coded_text = ''
    for i in range(length):
        coded_text = aDict[text[i]]+ coded_text
    return coded_text.lower()

def text_dec(binary_string):
    length = len(binary_string)
    inv_map = {v: k for k, v in aDict.items()}
    decoded_text = ''
    for i in range(0,length,5):
        decoded_text = inv_map[binary_string[i:i+5]] + decoded_text # + in strings is the join function.
    decoded_text = decoded_text[::-1]
    return decoded_text.lower()

def sumxor(l):
    r = 0
    for v in l: 
        r = r^v
    return r


def lfsr(seed,feedback,bits, flag):
    index_of_ones = []
    feedback_new = []
    for i in range(len(feedback)):
        if 1 in feedback:
            index_of_ones.append(feedback.index(1))
            feedback[feedback.index(1)] = 0
    feedback_new = index_of_ones    #this is a list which contains the positions of 1s in feedback list
    seed = deque(seed)              # make a new deque 
    output = []
    if flag==0:
        print('initial seed :',seed)
    for i in range(bits):
        xor = sumxor([seed[i] for i in feedback_new])
        output.append(seed.pop()) #extract to output the right-most bit of current seed
        seed.appendleft(xor)      #insert from left the result of the previous xor 
        if flag==0:
            print('state', i+1, 'of the lfsr :',seed)
    return output

#PART 1
enabled = 1 # turn into 1 in order to short printed messages.

file = open('lfsr1.txt','r')
feedback = [0,0,0,0,0,1,1,0,1,1]

text_encoded = text_enc(file.read()[1:-1])

for i in range(0,1024):
	new_list = list(feedback)

	x = list('{0:010b}'.format(i))#generate all binary combinations and put them in a lis
	x = [int(item) for item in x]#turn strings to integers

	out_list = lfsr(x,new_list,len(text_encoded),1)#do not return internal states    
	out = ''.join(str(n) for n in out_list)

	bin_message = string_xor(text_encoded,out)
	message = text_dec(bin_message)
	if enabled == 0:
		print(message + "	:	" + str(i))
	else:
		if "(" not in message:
			if ")" not in message:
				if"?" not in message:
					if"!" not in message:
						if"." not in message:
							if"-" not in message:
								print(message + "	:	" + str(i))

file.close()
#==========================================================================================================
#PART 2
print("====================================================")
print("Part 2")
file = open('lfsr2.txt','r')
feedback1 = [0,0,0,0,0,1,1,0,1,1]
feedback2 = [0,1,1,0,0,0,1,1,0,0,0,0,0,0,0,1]

new_text_encoded = text_enc(file.read()[1:-1])

for i in range(0,1024):
	for j in range(0,65536):
		new_list1 = list(feedback1)
		new_list2 = list(feedback2)

		x1 = list('{0:010b}'.format(i))
		x2 = list('{0:016b}'.format(j))
		x1 = [int(item) for item in x1]
		x2 = [int(item) for item in x2]

		out_list1 = lfsr(x1,new_list1,len(new_text_encoded),1)
		out_list2 = lfsr(x2,new_list2,len(new_text_encoded),1)
		out1 = ''.join(str(n) for n in out_list1)
		out2 = ''.join(str(n) for n in out_list2)

		result = string_xor(out1,out2)
		new_bin_message = string_xor(new_text_encoded,result)
		new_message = text_dec(new_bin_message)
		if enabled == 0:
			print(message + "	:	" + str(i))
		else:
			if "(" not in message:
				if ")" not in message:
					if"?" not in message:
						if"!" not in message:
							if"." not in message:
								if"-" not in message:
									print(message + "	:	" + str(i))










