message = "Coding Factory"

print(message[0],message[7])
print(message[1],message[8])
print(message[2],message[9])
print(message[3],message[10])
print(message[4],message[11])
print(message[5],message[12])
print(message[6],message[13])

# message[0] = 'c
# message = 'New Message

 # len()
print(f"Length of {message} = {len(message)}")
print()

for char in message:
    print(char, end="")
print()    

# enchanced for
for i in range(10 + 1):
    print(i)

print("-----------")
print(i)

# for indexing based
for i in range(len(message)):
    print(message[i], sep = "")

my_num = 12345679
print()
# result: the addition of the 1st and the last digit -> 1 + 9 = 10
str_num = str(my_num)
first_digit = int(str_num[0])
last_digit = int(str_num[-1])
# result = 
result = first_digit + last_digit
print(result)

print()

print(f"Result = {int(str_num[0]) + int(str_num[-1])}")