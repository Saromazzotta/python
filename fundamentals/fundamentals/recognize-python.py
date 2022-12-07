num1 = 42 #variable declaration 
num2 = 2.3 #variable declaration 
boolean = True #boolean
string = 'Hello World' #string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #list initialize 
person = {'name': 'John', 'location': 'Salt Lake', #dictionary initialize 
        'age': 37, 'is_balding': False} #boolean data type, number data type 
fruit = ('blueberry', 'strawberry', 'banana') #tuple initalize
print(type(fruit)) #type check 
print(pizza_toppings[1]) #list access value
pizza_toppings.append('Mushrooms') #list add value 
print(person['name']) #access value 
person['name'] = 'George' #variable declaration 
person['eye_color'] = 'blue' #variable declaration 
print(fruit[2]) #tuple access value 

if num1 > 45:  #if parameter 
    print("It's greater")
else:   #else parameter 
    print("It's lower")

if len(string) < 5: #if parameter 
    print("It's a short word!")
elif len(string) > 15: #else if parameter 
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5): #for loop start
    print(x)
for x in range(2, 5):
    print(x)
for x in range(2, 10, 3):
    print(x)
x = 0
while (x < 5): #while loop start and stop
    print(x)
    x += 1 #increment 

pizza_toppings.pop() #list delete last value 
pizza_toppings.pop(1) #list delete value at index 1

print(person) #dictionary access value 
person.pop('eye_color') #dictionary delete value 
print(person) #dictionary access value 

for topping in pizza_toppings: #for loop start
    if topping == 'Pepperoni': #if statement 
        continue #continue 
    print('After 1st if statement')
    if topping == 'Olives': #if statement 
        break #for loop break 


def print_hello_ten_times():
    for num in range(10):
        print('Hello') #string intialization 


print_hello_ten_times()


def print_hello_x_times(x):
    for num in range(x):
        print('Hello')


print_hello_x_times(4) #argument 


def print_hello_x_or_ten_times(x=10):
    for num in range(x):
        print('Hello')


print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


""" .          #multiline comment 
Bonus section #single line comment 
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)
