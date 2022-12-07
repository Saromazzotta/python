#Exercise 1
x = [[5, 2, 3], [10, 8, 9]]
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]

#1
x[1][0] = 15
print(x)

#2
students[0]['last_name'] = "Bryant"
print(students)

#3
sports_directory['soccer'][0] = "Andres"
print(sports_directory)

#4
z[0]['y'] = 30
print(z)



#Exercise 2
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

def iterateDictionary(students):
    for i in range (0, len(students)):
        for key, val in students[i].items():
                print(key, "=", val) 

iterateDictionary(students)

#Exercise 3
def iterateDictionary2(value, students):
    for i in range(0, len(students)):
        print(students[i][value])

iterateDictionary2('first_name', students)



#Exercise 4
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(list):
    for key, val in dojo.items():
        print(len(val), key, val)
        # for i in range(0, len(dojo[val])):
            # print(dojo['locations'])


printInfo(dojo)





# # output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank

# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon
