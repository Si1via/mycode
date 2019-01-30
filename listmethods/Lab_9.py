#!/usr/bin/env python3
proto = ['ssh','http','https']
protoa = ['ssh','http','https']
print(proto)
proto.append('dns') #This line will add 'dns' to the end of our list
protoa.append('dns') #This line will add 'dns' to the end of our list
print(proto)
proto2 = [22, 88,443,53] #A list of common ports
proto.extend(proto2) # Pass proto2 as an argument to the extend method
print(proto)
protoa.append(proto2) # Pass proto as an argument to the append method
print (protoa)

###############################################################################
#RESULT
#['ssh', 'http', 'https']
#['ssh', 'http', 'https', 'dns']
#['ssh', 'http', 'https', 'dns', 22, 88, 443, 53]
#['ssh', 'http', 'https', 'dns', [22, 88, 443, 53]]

#This inserts a an item to the list on position 3
#protoa.insert(2,'domain')
#print("This shows item inserted in the list: ", protoa)

protoa = ['ssh','http','https']
#This finds the position of https
#index = proto.index('https')
i = protoa.index('http')  # This returns a value
print("The position for https is: ", i)

#This reverses list in protoa 
print(protoa)
protoa.reverse()  # This is not returning a value
print("This is the reverse list: ", protoa)


#This show how many 22 are in the list
b = proto.count('ssh')
print("This counts how many times ssh repeats on the list", b)

#pop command, this removes https
proto.pop(2)
print(proto)

proto.insert(0,"TCP")
print(proto)
