from collections import deque
import lfsr_project

#PART 1
enabled = 1 # turn into 1 in order to short printed messages.

myFile = open('lfsr1.txt','r')

feedback1 = [0,0,0,0,0,1,1,0,1,1]
tf1 = list(feedback1)#temporal variable for feedback

text_encoded = lfsr_project.text_enc(myFile.read()[1:-1])

string1 = 'ab'
string1_encoded = lfsr_project.text_enc(string1)

string2 = 'sq'
string2_encoded = lfsr_project.text_enc(string2)

xored = lfsr_project.string_xor(string1_encoded,string2_encoded)
xored = [int(item) for item in xored]

internal_state = xored[::-1]#inverse xored is the 10nth internal state

seed = lfsr_project.lfsr(internal_state,tf1,1023,1)
seed = seed[-10:]#Period is 1023 . seed is located at 1013-1023
seed = seed[::-1]#we inverse bits in order to take proper seed

tf1 = list(feedback1)
out = lfsr_project.lfsr(seed,tf1,len(text_encoded),1)#bit stream
out = ''.join(str(n) for n in out)
binary_message = lfsr_project.string_xor(out,text_encoded)
message = lfsr_project.text_dec(binary_message)

print(message)
print("======================\n")

myFile.close()

#PART 2

myFile = open('lfsr2.txt', 'r')

feedback2 = [0,1,1,0,0,0,1,1,0,0,0,0,0,0,0,1]


tf2 = list(feedback2)

text_encoded = lfsr_project.text_enc(myFile.read()[1:-1])

string1 = 'abcd'
string1_encoded = lfsr_project.text_enc(string1)

string2 = '!c.)'
string2_encoded = lfsr_project.text_enc(string2)

xored = lfsr_project.string_xor(string1_encoded,string2_encoded)
xored = [int(item) for item in xored]

internal_state = xored[::-1]
internal_state = ''.join(str(n) for n in internal_state)

for i in range(1024):
	tf1 = list(feedback1)

	#generate random seed for small lfsr
	small_out = list('{0:010b}'.format(i))#generate binary number with given i
	small_out = [int(item) for item in small_out]#turn strings to integers

	out_list = lfsr_project.lfsr(small_out,tf1,30,1)#do not return internal state
	out_list = out_list[-20:]#keep last 20 bits of small lfsr

	#find big lfsr's stream
	out = ''.join(str(n) for n in out_list)
	bin_big_out = lfsr_project.string_xor(internal_state,out)
	bin_big_out_cropped = bin_big_out[::-1]
	bin_big_out_cropped = [int(item) for item in list(bin_big_out[-16:])]

	#find seed for big lfsr
	tf2 = list(feedback2)
	seed = lfsr_project.lfsr(bin_big_out_cropped,tf2,65537,1)#65536 is 2^16 = period + 2 because 2 seed bits are contained in bin big cropped
	seed = seed[-16:]
	seed = seed[::-1]

	#find the decrypted text executing lfsr process
	tf1 = list(feedback1)
	temp1 = lfsr_project.lfsr(small_out,tf1,len(text_encoded),1)

	tf2 = list(feedback2)
	temp2 = lfsr_project.lfsr(seed,tf2,len(text_encoded),1)

	temp_xor = lfsr_project.string_xor(temp1,temp2)
	print(temp_xor[10:30])
	print(internal_state)
	print("\n")
	bin_message = lfsr_project.string_xor(text_encoded,temp_xor)
	message = lfsr_project.text_dec(bin_message)

	#prune messages
	if "(" not in message:
		if ")" not in message:
			if "?" not in message:
				if "!" not in message:
					if "." not in message:
						if "-" not in message:
							print (message)

myFile.close()