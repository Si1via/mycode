#!/usr/bin/env python3

import shutil #to transfer files on secure connection

import os

os.chdir('/home/student/mycode/')

#The file raynor.obj was already created inside dir cep_storage
shutil.move('raynor.obj', 'ceph_storage/')

xname = input('What is the new name for kerrigan.obj? ')

#The file kerrigan.obj was already created inside dir cep_storage
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

#touch ~/mycode/raynor.obj
#touch ~/mycode/ceph_storage/kerrigan.obj

