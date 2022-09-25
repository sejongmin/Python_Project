for i in range(7):
    print(i)
print()
for i in range(5, 10):  #끝 - 1 까지 반복
    print(i)
print()
for i in range(10, 5, -1):  #끝 + 1 까지 반복
    print(i)
print()

a_str = "hello python"
for i in a_str:
    print(i)
print()

name_list = ["홍길동", "장다인", "김철수"]
age_list = [500, 5, 12]
for i, k in enumerate(name_list):   #길이와 내용 가져오기
    print("i=",i,end=' ')
    print("k=",k)
for i, k in enumerate(name_list):
    print(name_list[i], end=' ')
    print(age_list[i])
print()

test_list = [i for i in range(10)]
print(test_list)

test2_list = []
for i in range(10):
    test2_list.append(i)
print(test2_list)
print()

test_list = [5 * i for i in range(10)]
print(test_list)
test2_list = [0 * i for i in range(10)]
print(test2_list)
print()


