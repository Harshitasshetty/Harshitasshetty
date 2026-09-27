#dictionary
birthday={
    "harshita": "18-02-2008",
    "ashmita": "02-05-2009",
    "uma": "31-05-1981",
    "pavi": "21-03-1989"
}

meanings={
    "bat":"used to hit",
    "ball":"used is hit",
    "wicket":"to e protected"
}

print(type(birthday))
print(birthday["harshita"])
print(birthday.get("ashmita","not found"))
print(birthday.get("ridhi","not found"))

print("adding sudeep to the list")
birthday["sudeep"]="02-09-1973"
print(birthday)

print("Updating...")
birthday["pavi"]="21-03-1990"
print(birthday)

birthday.pop("pavi")
print(birthday)

print(birthday.keys())
print(birthday.values())

print(birthday.items())
d ={
    "str":"str",
    "st": 123,
    "f":10.12,
    "is":True,
    (1):"get"
}

item1 = {
    "name":"milk",
    "weight":1,
    "price": 50
}

item2 = {
    "name":"sugar",
    "weight":2,
    "price": 99.9
}

items = [item1, item2]
print(items)



