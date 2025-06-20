my_num = 10

my_float = 3.14

my_str = "Hello there"

print("Printing comma separated values")
print(my_num, my_float, my_str)

print("-----------------------")

# separator becomes a tab (=4 spaces) length
print(my_num, my_float, my_str, sep="\t")
print("===========================")
#the print ends in *** and not with \n
print(my_num, my_float, my_str, sep="\t", end="***")