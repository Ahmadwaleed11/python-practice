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

# s1={1,2,3,4}
# s2={3,4,5,6}
# print(s1.intersection(s2))
# s1.intersection_update(s2)
# print(s1,s2)

########## symmetric difference set ##################

# s1={1,2,3,4}
# s2={3,4,5,6}
# # print(s1.symmetric_difference(s2))
# # print(s1.symmetric_difference_update(s2))
# print(s1.difference(s2))



######### isdisjoint set ################

# s1={1,2,}
# s2={3,4,5,6}
# print(s1.isdisjoint(s2))

########### issuperset set ################

# s1={1,2,3,4}
# s2={1,2,3,4}
# s3={3,4,5,6}
# print(s1.issuperset(s2))
# print(s1.issuperset(s3))

########### issubset set ################


# s1={1,2,3,4}
# s2={1,2,3,4}
# s3={3,4,5,6}
# print(s2.issubset(s1))
# print(s3.issubset(s1))


######### add / update / remove / discard / pop / del / clear set ##################

# s1={1,2,3,4,5,6}
# item=s1.pop()
# print(item)

# s1.add(5)
# s1.remove(5)
# s1.discard(3)
# s1.update({5,6})
# s2={3,4,5,6}
# s2.clear()
# print(s2)
# print(s1)


###### check itenm ################


info={'name','ahmad','age',20}
if 20 in info:
    print('yes')
else:
    print('no')    
