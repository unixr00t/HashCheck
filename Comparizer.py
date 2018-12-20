import hashlib

hasher1 = hashlib.md5()							#File1
afile1 = open(r'C:/blah/blah/app.apk','rb')
buf1 = afile1.read()
a = hasher1.update(buf1)
md5_a = (str(hasher1.hexdigest()))
print("MD5 Hash for file1=" +md5_a)

hasher2 = hashlib.md5()							#file2
afile2 = open(r'C:/blah/blah/app.apk','rb')
buf2 = afile2.read()
b = hasher2.update(buf2)
md5_b = (str(hasher2.hexdigest()))
print("MD5 Hash for file2=" +md5_b)

if(md5_a==md5_b): 								#compare
	print("Matched")
else:
	print("Not Matched!")

#end