# Dictionary are key value pair

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

customer["Country"] = ["India", "London", "New York"]

print(customer)

print(customer.keys())

print(customer.values())


custInfo = []
for key in customer.keys():
    print(customer[key])

Dict = {}
print("Empty Dictionary: ")
print(Dict)
Dict[0] = 'Geeks'
Dict[2] = 'For'
Dict[3] = 1
print("\nDictionary after adding 3 elements: ")
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
