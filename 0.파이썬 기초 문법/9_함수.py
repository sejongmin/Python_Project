def func():
    print("안녕하세요")

func()

def funcAdd(a ,b):
    return a + b

c = funcAdd(1,2)
print(c)

def funcMux(a, b):
    mux = a * b
    return mux

c = funcMux(2, 3)
print(c)

def funcAddMux(a, b):
    add = a + b
    mux = a * b
    return add, mux

a, b = funcAddMux(1, 3)
print(a, b)