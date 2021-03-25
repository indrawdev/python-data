name = input("Enter file:")
if len(name) < 1 : name = "files\mbox-short.txt"
handle = open(name)

di = dict()
lst = list()

for line in handle:
	words = line.split()
	if len(words) > 2 and words[0] == 'From':
		hour = words[5].split(':')
		di[hour[0]] = di.get(hour[0], 0) + 1
	else :
		continue

for key, value in di.items():
	lst.append((key, value))

result = sorted(lst, reverse=False)
for key, value in result:
	print(key, value)