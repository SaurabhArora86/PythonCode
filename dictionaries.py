# Dictionary are key value pair

customer = {
    "Name": "John Smith",
    "Age": 26,
    "Gender": "M"
}

print(customer["Name"])

customer["DOB"] = ["1986", "1987"]
print(customer["DOB"])

customer["phone"] = input("Please enter phone Number")
print(customer["phone"])

print(customer)

customer["Country"] = ["India", "London", "New York"]

print(customer)

Dict = {}
print("Empty Dictionary: ")
print(Dict)
Dict[0] = 'Geeks'
Dict[2] = 'For'
Dict[3] = 1
print("\nDictionary after adding 3 elements: ")
print(Dict)
