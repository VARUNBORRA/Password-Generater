import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',     'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print('Welcome to the HI5 CODING Password Generater!')

nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

List_password = []
                                                                   
#suppose you give input 1 is add with 1 (1+1) so the range between(1,2)(so there is only one value in between range(1,2) and 2 in not included ex:- print(range(1,5)) output:- 1,2,3,4)
for char1 in range(1,nr_letters + 1):
    List_password.append(random.choice(letters))



for char2 in range(1, nr_symbols + 1):
     List_password += random.choice(symbols)


for char3 in range(1, nr_numbers + 1):
    List_password += random.choice(numbers)

#By using random.shuffle() it shuffle the values.
#Example:- a = ["HI",5,"CODING"]
#print(random.shuffle(a))
#output:-["CODING","HI",5]
random.shuffle(List_password)


final_password = ""

#by this for loop char4 convert iteam in a list into string and add to final_password = ""(string)
for char4 in List_password:
    final_password += char4




print(final_password)     