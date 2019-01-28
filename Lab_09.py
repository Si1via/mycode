#!/usr/bin/env  python3

#ASCII characters are used to represent letters, punctuation, numbers

#Python actually uses Unicod, which is numeric

print("The ORD function...")
########################################################################################################################
#ORD function ##ordinal=numeric value, converts character to integer
#To get a numeric code for a character, use the Python ord fuction
########################################################################################################################
#Loop through this character string
#This will convert each character in this string to a numeric value (in this case is using lower case)
##for loop, indent
for myChar in 'abcdefgh':
    myNum = ord(myChar)
    print(myChar, myNum)


print()
print("The CHR function...")

########################################################################################################################
#CHR function ## character converts integer to character
#Here you can loop through as ASCII numeric code back to a character form
#To get a character from a numeric code, use the Python chr function
########################################################################################################################
#Loop through the integers 65-74
#Convert each integer to its character form, in this case this displays cap letters
for i in range(65, 75):
    myChar=chr(i)
    print(i,myChar)


print()
print("The HEX fuction...")
########################################################################################################################
#HEX function...0x denotes that the value is in hexadecimal format
########################################################################################################################
#Loop through the integers 1-16
for j in range(1, 17):
    myHexValue=hex(j)
    print(j,myHexValue)



