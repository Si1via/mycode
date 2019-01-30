#!/usr/bin/env python3
proto = ['ssh', 'http','https']
print(proto)
print(proto[1])
proto.extend('dns') #This line will add 'd', 'n', 's' to the end of of the list. This extends the list.
print(proto)


#########################################
#RESULT
#['ssh', 'http', 'https']
#http
#['ssh', 'http', 'https', 'd', 'n', 's']
