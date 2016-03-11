#Functions used from https://github.com/AristotleUniversity/python_scripts/blob/master/lfsr_project.py : text_enc text_dec string_xor
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
                              '11000','11001'])) #the function from our alphabet to 5-bit binary strings


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

def string_xor(btext,key): 
    cipher = []
    if len(btext)!=len(key):
        print("key and message must have the same lengths!")
        return 0
    for i in range(len(btext)):
        cipher.append(int(btext[i])^int(key[i])) #xoring bit-bit
    cipher = ''.join(str(e) for e in cipher)
    return cipher

#initializes a vector with elements from 0 to 255
#shuffles these elements according to key
def KSA(key):
      s = []
      for i in range(256):
            s.append(i)

      j=0
      for i in range(256):
            j = (j + s[i] + int(key[i%len(key)]))%256
            s[i],s[j] = s[j],s[i]#swapping values
            
      return s

def PRGA(s,bits):
      i = 0
      j = 0
      import math
      iterations = int(math.ceil(bits/8.))
      output = []
      for k in range(iterations):
            i = (i+1)%256
            j = (j+s[i])%256
            s[i],s[j] = s[j],s[i]
            output.append(s[(s[i]+s[j])%256])#these are octets of bits

      #convert to binary octets
      binary_output = []
      for item in output:
            binary_output.append("{0:08b}".format(item))

      #convert octets to string
      text = ''
      binary_output = binary_output[::-1]
      for i in range(0,len(binary_output)):
            text = binary_output[i]+ text

      #keep as many bits as we need in order to bitwise xor with message
      text = text[:bits]
      return text

#define key
key = 'MATRIX'
#define message
message = 'neversendahumantodoamachinesjob'
#encode message
encoded = text_enc(message)
#encode key
encoded_k = text_enc(key)
#create v vector
v = KSA(encoded_k)
#generate pseudo random bits based on v
generated = PRGA(v,len(message)*5)
#xor message with random bits
encrypted_message_binary = string_xor(encoded,generated)
#decode message
encrypted_message = text_dec(encrypted_message_binary)
print("Encrypted message: " + encrypted_message)

#reverse procedure
var = string_xor(encrypted_message_binary,generated)
var = text_dec(var)
print("Initial message: " + var)

