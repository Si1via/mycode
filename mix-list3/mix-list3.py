#!/usr/bin/env python3
list1 = ['cisco_nxos', 'arista_eos', 'cisco_ios']
print(list1)  
#Result
#['cisco_nxos', 'arista_eos', 'cisco_ios']

print(list1[1])
#Result
#arista_eos

list1.extend(['juniper'])
print(list1)
#Result 
#['cisco_nxos', 'arista_eos', 'cisco_ios', 'juniper']

list1.append(['10.10.1','10.2.0.1','10.3.0.1'])
print(list1)
#Result
#['cisco_nxos', 'arista_eos', 'cisco_ios', 'juniper', ['10.10.1', '10.2.0.1', '10.3.0.1']]

print(list1)
print(list1[4])
#Result
#['10.10.1', '10.2.0.1', '10.3.0.1']

print(list1[4])
print(list1[4][0])
#Result
#10.10.1


