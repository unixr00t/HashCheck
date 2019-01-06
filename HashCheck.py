#!/bin/python2

import hashlib
import sys
import os

print("""
##     ##    ###     ######  ##     ##  ######  ##     ## ########  ######  ##    ## 
##     ##   ## ##   ##    ## ##     ## ##    ## ##     ## ##       ##    ## ##   ##  
##     ##  ##   ##  ##       ##     ## ##       ##     ## ##       ##       ##  ##   
######### ##     ##  ######  ######### ##       ######### ######   ##       #####    
##     ## #########       ## ##     ## ##       ##     ## ##       ##       ##  ##   
##     ## ##     ## ##    ## ##     ## ##    ## ##     ## ##       ##    ## ##   ##  
##     ## ##     ##  ######  ##     ##  ######  ##     ## ########  ######  ##    ## 
		Version v1.4
	Made by Vijay Chari (UnixR00t)
""")

try:
	path1 = str(sys.argv[1])
	path2 = str(sys.argv[2])
except IndexError:
	print "[+] Usage Example : python %s path1 path2" % sys.argv[0]
	sys.exit()

hasher1 = hashlib.md5()							#File1
afile1 = open(path1,'rb')
buf1 = afile1.read()
a = hasher1.update(buf1)
md5_a = (str(hasher1.hexdigest()))
print("\nMD5 Hash for file1=" +md5_a)

hasher2 = hashlib.md5()							#file2
afile2 = open(path2,'rb')
buf2 = afile2.read()
b = hasher2.update(buf2)
md5_b = (str(hasher2.hexdigest()))
print("MD5 Hash for file2=" +md5_b)

if(md5_a == md5_b): 								#compare
	print("\Matched!")
else:
	print("\nNot matched!")

#end