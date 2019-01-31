#!/usr/bin/env python3

## Collect input from user
hostname = input("What value should we set for hostname?")

## Use the upper method, to test if input value matches expected value
if hostname.upper() == "MTG":
    print('The hostname was found to be MTG')
    print('hostname matches expected config')

## Always print out to the user a message
print('Exiting the script')