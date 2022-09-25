a_list = [1,2,3,4,5]
print(a_list)
print(a_list[0])
print(a_list[1])
print(a_list[:2])
print(a_list[2:])

b_list = []
b_list.append(1)
b_list.append(2)
b_list.append(3)
print(b_list)

c_list = [1,3.14,"hello",[1,2,3]]
print(c_list)
print(c_list[1:3])

d_list = [1,2,3,4,5]
print(d_list)
d_list[0] = 5
print(d_list)

a_tuple = (1,2,3,4,5)   #tuple은 데이터 변경 불가
print(a_tuple)

a_dic = {'a':1, 'b':2, 'c':'3'}
print(a_dic)
print(a_dic['a'])
print(a_dic['b'])
print(a_dic['c'])

b_dic = {1:'a', 'b':[1,2,3], 'c':3}
print(b_dic[1])
print(b_dic['b'])
print(b_dic['c'])
b_dic['d'] = 4
print(b_dic)

a_set = set([1,2,3,4])
print(a_set)

b_set = set([1,1,2,2,3,3,4,5,6])
print(b_set)

c_set = set("python40s")    #set은 순서가 무작위로 섞임
print(c_set)