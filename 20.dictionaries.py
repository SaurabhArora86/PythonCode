# Dictionary are key value pair
# Dictionary are mutable
# Dictionary are unordered
# Dictionary are indexed


customer = {
    "Name": "John Smith",
    "Age": 26,
    "Gender": "M"
}

print(customer["Name"])

customer["DOB"] = ["1986", "1987"]
print(customer["DOB"])

# customer["phone"] = input("Please enter phone Number")
# print(customer["phone"])

print(customer)
# Below will print the Dictionary in the form of tuple
print(customer.items())

customer["Country"] = ["India", "London", "New York"]

print(customer)

print(customer.keys())

print("\nUpdating Values**********")
print(customer.values())
customer.update({"Country": "India"})
print(customer)

print("\nPrinting Values**********")
for key in customer.keys():
    print(customer[key])

Dict = {}
print("Empty Dictionary: ")
print(Dict)
Dict[0] = 'Geeks'
Dict[2] = 'For'
Dict[3] = 1
Dict["Name"] = "John"
print("\nDictionary after adding 4 elements: ")
print(Dict)

# Dictionary Methods

# example where values gets added
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

thatdict = {"mileage": 25,
            "sales": 200}

thisdict.update(thatdict)
print(thisdict)


# clear like thatdict.clear() is to clear a dictionary
# del thisdict will delete dictionary
# thatdict.pop("Year")
thisdict.pop("sales")
print(thisdict)


my_dict = {
    "Name": "Arora",
    "Age": 30,
    "Sex": "Male"
}

print(my_dict["Age"])

# Note below, if it is not a part of Dictionary key, get will return None where as [] will throw an error
print(my_dict.get("DOB"))
# print(my_dict["DOB"])
print("\n**********Popping**********")
# pop vs popitem()
# popitem() removes the last inserted item and reutrns the key value pair as tuple
# pop() removes the item with the specified key name
print(my_dict)
print(my_dict.popitem())
print(my_dict)
print(my_dict.pop("Age"))
print(my_dict)
