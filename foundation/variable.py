
# Variables in Python

first_name = 'Venkata sai'
last_name = 'Makani'
country = 'India'
city = 'Nellore'
age = 30
is_married = True
skills = ['Python','Sql']

person_info = {
    'firstname': 'Venkata sai',
    'lastname': 'Makani',
    'country': 'India',
    'city': 'Nellore'
}

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', 'not_married')
print('Skills: ', skills)
print('Person information: ', person_info)

# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'Venkata sai','makani', 'India', 30, 'Not_married'

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)