import lfsr_project

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
encoded = lfsr_project.text_enc(message)
#encode key
encoded_k = lfsr_project.text_enc(key)
#create v vector
v = KSA(encoded_k)
#generate pseudo random bits based on v
generated = PRGA(v,len(message)*5)
#xor message with random bits
encrypted_message_binary = lfsr_project.string_xor(encoded,generated)
#decode message
encrypted_message = lfsr_project.text_dec(encrypted_message_binary)
print("Encrypted message: " + encrypted_message)

#reverse procedure
var = lfsr_project.string_xor(encrypted_message_binary,generated)
var = lfsr_project.text_dec(var)
print("Initial message: " + var)

