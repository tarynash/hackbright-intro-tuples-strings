#my_name = "Taryn"
#name_list = list(my_name)
#print name_list

#numbers = "1,2,3,4,5"
#print numbers.split(",")

#i = numbers.split(",")

#for i in numbers:
#	print int(i)

rhyme = "One fish two fish red fish blue fish"

my_list = []

for word in rhyme.split("fish"):
	if word:
		my_list.append(word.strip())

print my_list