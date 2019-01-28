#!/usr/bin/env python3

#This creates a list (List are made with square brackets)
my_list = ["192.168.0.5", 5060, "UP"]

#This returns the IP Address from the list. (List always begin at zero).
print("The first item in the list (IP): " + my_list[0])

#Now return the port 5060. The problem is 5060 is an integer, not a string. 
#Strings are surrounded with quotes. We may not combine unlike data types withinPython. So, below is the solution. We can force an integer value to be a string with the str() function.
print("The second item in the list(port): " + str(my_list[1]))

#Now return the last item on the list. this a string value "UP"
print("The last item in the list (state): " + my_list[2])

#This is a new list
new_list = [5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh"]

#This 
print("When I " + new_list[5], "into IP address " +  new_list[3], "or " + new_list[4])

#This prints the ports
print("I am unable to ping ports " + str(new_list[0])+", " + new_list[1]+", or " + str(new_list[2]))

 
#This is the resullt
#The first item in the list (IP): 192.168.0.5
#The second item in the list(port): 5060
#The last item in the list (state): UP
#When I ssh into IP address 10.0.0.1 or 10.20.30.1
#I am unable to ping ports 5060, 80, or 55