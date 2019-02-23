# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# Create dict
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}


# Use constructor
person2 = dict(first_name='Sara', last_name="Connors")

print(person['first_name'])
print(person.get('last_name'))

#Add key/value
person['phone'] = '555-555-5555'

#get dict keys
print(person.keys())