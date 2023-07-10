
# For this assignment, I came up with my own variable anmes/function names on a few problems. I apologize if that makes it harder to understand. All of the answers should be correct. 



x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#Start of the assignment
x[1][0] = 15
print(x)

students[0]["last_name"] = "Bryant"
print(students)

sports_directory['soccer'][0] = "Andres"
print(sports_directory)

z[0]['y'] = 30
print(z)


#Second Section of Assignment
students2 = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def problem_two_iteration(second_list):
    for index in range(len(second_list)):
        for key in second_list[index]:
            print(second_list[index][key])
print(problem_two_iteration(students2))
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel
def problem_three_iteration(key_name,second_list):
    for index in second_list:
        print(index[key_name])
# print(problem_three_iteration('first_name',students2))
# print(problem_three_iteration('last_name',students2))
problem_three_iteration('first_name',students2)
problem_three_iteration('last_name',students2)

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for keys, vals in some_dict.items():
        print(len(vals), keys)
        for i in range(len(vals)):
            print(vals[i])
printInfo(dojo)

# printInfo(dojo)
# output:
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