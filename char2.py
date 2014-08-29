import string
import random

def stringGenerator(size=10, chars=string.printable):
	return ''.join(random.choice(chars) for _ in range(size))

out = open("randomChar.txt", "w")

for i in range(100, 0, -1):
	string = stringGenerator();
	string = repr(string);
	#string.encode('string-escape');
	out.write(string);
	out.write("\n");
