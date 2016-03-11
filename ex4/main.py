import codecs
# -*- coding: utf-8 -*-
dictionary = [u'Α', u'Β', u'Γ', u'Δ', u'Ε', u'Ζ', u'Η', u'Θ', u'Ι', u'Κ', u'Λ', u'Μ', u'Ν', u'Ξ', u'Ο', u'Π', u'Ρ', u'Σ',
              u'Τ', u'Υ', u'Φ', u'Χ', u'Ψ', u'Ω']

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

file = codecs.open('thema4.txt','r','cp1253')
string = file.read()
print(string)
newstring = encode(string)
print(newstring)
for i in range(24):
    temp = [(x+i)%24 for x in newstring]#permutation list
    print(''.join(decode(temp)))
