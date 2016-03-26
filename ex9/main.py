from collections import deque
import lfsr_project

#PART 1
enabled = 1 # turn into 1 in order to short printed messages.

file = open('lfsr1.txt','r')
f = open('decrypted.txt','w')
feedback = [0,0,0,0,0,1,1,0,1,1]
feedback1 = list(feedback)

text_encoded = lfsr_project.text_enc(file.read()[1:-1])

string1 = 'ab'
string1_encoded = lfsr_project.text_enc(string1)

string2 = 'sq'
string2_encoded = lfsr_project.text_enc(string2)

xored = lfsr_project.string_xor(string1_encoded,string2_encoded)
xored = [int(item) for item in xored]

internal_state = xored[::-1]#inverse xored is the 10nth internal state

seed = lfsr_project.lfsr(internal_state,feedback1,1023,1)
seed = seed[-10:]#Period is 1023 . seed is located at 1013-1023
seed = seed[::-1]#we inverse bits in order to take proper seed


out = lfsr_project.lfsr(seed,feedback,len(text_encoded),1)#bit stream
out = ''.join(str(n) for n in out)
binary_message = lfsr_project.string_xor(out,text_encoded)
message = lfsr_project.text_dec(binary_message)

print(message)

file.close()