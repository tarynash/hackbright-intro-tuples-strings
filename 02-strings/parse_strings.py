#my_name = "Taryn"
#name_list = list(my_name)
#print name_list

#numbers = "1,2,3,4,5"
#print numbers.split(",")

#i = numbers.split(",")

#for i in numbers:
#	print int(i)

#rhyme = "One fish two fish red fish blue fish"

#my_list = []

#for word in rhyme.split("fish"):
#	if word:
#		my_list.append(word.strip())

#print my_list

#str = "item:apples, quantity:4, price:1.50\n"
#def grocery_bill(str_input):
#	str_split = str_input.split(",")
#	quantity = float(str_split[1].split(":")[1])
#	price = float(str_split[2].split(":")[1])
#	return quantity * price
#print grocery_bill(str)

items = ["item:apples,quantity:4,price:1.50\n", "item:pears,quantity:5,price:2.00\n", "item:cereal,quantity:1,price:4.49\n"]

def grocery_bill(str_input):

	i = 0
	items_total = 0

	while(i<len(items)):
		str_split = items[i].split(",")
		quantity = float(str_split[1].split(":")[1])
		price = float(str_split[2].split(":")[1])
		x = quantity*price
		items_total += x
		i += 1

	return items_total

print grocery_bill(items)



