name = input("Enter file:")
if len(name) < 1 : name = "files\mbox-short.txt"
handle = open(name)

words = list()
di = dict()

for line in handle:
	if not line.startswith('From:'):
		continue
	line = line.split()
	words.append(line[1])

for word in words:
	di[word] = di.get(word, 0) + 1

maxval = 0
maxkey = None

for key, val in di.items() :
	if val > maxval:
		maxval = val
		maxkey = key   

print(maxkey, maxval)