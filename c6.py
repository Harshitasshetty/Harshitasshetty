#Tules and sets
genders=("male" , "female" ,"others", (1,2,3))
print(genders)
print(type(genders))
print(genders[1:3])
print(genders.index("male"))

s = {20,2,123}# set is unordered
print(s)
s2 = set((1,2,3))
print(s2)
print(type(s2))

s3={1,2,3}
s4={3,4,5}
print(s3|s4) # union
print(s3&s4) #intersection
print(s3-s4) #difference
s.add(4)

a = s.pop()
print(a)

