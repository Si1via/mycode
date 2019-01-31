#!/usr/bin/env python3

#This is the vendor lost 
vendors = ['cisco', 'juniper', 'big_ip', 'f5', 'arista', 'alta3', 'zach', 'stuart']

#This is the approved vendor list
approved_vendors = ['cisco', 'juniper', 'big_ip']

for x in vendors:
    print("\nThe vendors is " + x, end="")
    if x not in approved_vendors:
        print(" - NOT AN APPROVED VENDOR!", end="")
print("\nOur loop has ended.")