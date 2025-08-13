# s={'ahmad','waleed','harry','ahmad','waleed','harry','ahmad','waleed','harry','ahmad','waleed','harry'}
# print(s)

# name=set()
# print(type(name))


####### union set #####################

# s1={1,2,3,4}
# s2={3,4,5,6}
# print(s1.union(s2))
# s1.update(s2)
# print(s1,s2)


########## intersection set ##################

s1={1,2,3,4}
s2={3,4,5,6}
print(s1.intersection(s2))
s1.intersection_update(s2)
print(s1,s2)