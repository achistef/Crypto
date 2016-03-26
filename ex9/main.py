from collections import deque
import lfsr_project

#PART 1
enabled = 1 # turn into 1 in order to short printed messages.

file = open('lfsr1.txt','r')
f = open('decrypted.txt','w')
feedback = [0,0,0,0,0,1,1,0,1,1]

text_encoded = lfsr_project.text_enc(file.read()[1:-1])

string1 = 'ab'
string1_encoded = lfsr_project.text_enc(string1)

string2 = 'sq'
string2_encoded = lfsr_project.text_enc(string2)

xored = lfsr_project.string_xor(string1_encoded,string2_encoded)
xored = [int(item) for item in xored]

print(xored)

seed = lfsr_project.lfsr(xored,feedback,1024,1)
print(seed)
print("\n")
seed = seed[-10:]
print("\n")
print(seed)
out = lfsr_project.lfsr(seed,feedback,10,1)
print(out)
#out = lfsr_project.lfsr(seed,feedback,len(text_encoded),1)#bit stream

#binary_message = lfsr_project.string_xor(out,text_encoded)
#message = lfsr_project.text_dec(binary_message)
#print(message)
