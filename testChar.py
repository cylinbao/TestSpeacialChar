fin = open("randomChar.txt","r")

#print fin.readline()
for line in fin:
	#for i in range(1,len(line)-1,1):
		print r"'%c%c%c%c%c%c%c%c%c%c'" % (line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9], line[10])
#	print

print fin.tell()

fin.close()
