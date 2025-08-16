# dic={
#     1:'ahmad',
#     24:'waleed',
#     25:'harry'
# }
# # print(dic['ahmad'])
# print(dic[1])


####### get particular value ########

# info={'name':'harry', 'age':20}
# # print(info['name2'])  
# # this key throw error
# print(info.get('name2'))
# #  this key display none
# print(info)
# # print(info.keys())
# # print (info.values())
# # for key in info.keys():
# #     print(info[key])


########### dic method #############

ep1={1:23,2:34,4:67}
ep2={123:23,234:12}
ep1.update(ep2)
print(ep1)