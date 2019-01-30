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
#protoa.insert(2, 'domain')
#print("This shows item inserted in the list: ", protoa)

#This finds the position of https
#index = proto.index('https')
#proto.indesx(http)
#print("The position for https is: ", index)

#This reverses list in protoa 
#protoa.reverse()
#print("This is the reverse list: ". protoa)

#This show many 22 in the list
proto.count('ssh')
print("This counts how many times ssh repeats on the list", proto)
