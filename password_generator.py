import random
length=int(input("please enter the length of the password"))
numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
low_case=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
upper_case=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
symbol= ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')', '<']

com=numbers+low_case+upper_case+symbol

rand_digit = random.choice(numbers)
rand_upper = random.choice(upper_case)
rand_lower = random.choice(low_case)
rand_symbol = random.choice(symbol)

tem=rand_digit+rand_lower+rand_upper+rand_symbol


for x in range(length-4):
    tem= tem+ random.choice(com)
length=str(length)
print("your random  "+length+"  digit password is  "+tem)