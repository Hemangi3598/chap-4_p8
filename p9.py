# wapp to read a string and count
# number of upper case letters, lowercase letters, digits and other characters
# i/p : k@123MAI 2 2 3 1

string = input(" enter a string ")

uc, lc, dc, oc = 0, 0, 0, 0
for s in string:
	if 'A' <= s and s <= 'Z' :
		uc = uc + 1
	elif 'a' <= s and s<= 'z':	
		lc = lc + 1
	elif '0' <= s and s<= '9':
		dc = dc + 1
	else:
		oc = oc + 1
print(uc, lc , dc, oc)
		