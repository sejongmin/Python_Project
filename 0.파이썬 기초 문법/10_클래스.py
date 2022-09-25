class Greet():
    def hello(self):
        print("hello")
    def hi(self):
        print("hi")
    
human1 = Greet()    #Greet라는 클래스로 human 객체를 찍어 생성
human2 = Greet()

human1.hello()  #클래스로 객체 생성후 메서드 이용
human1.hi()
human2.hello()
human2.hi()

class Student():
    def __init__(self, name, age, like):
        self.name = name
        self.age = age
        self.like = like
    def studentInfo(self):
        print(f"이름:{self.name}, 나이:{self.age}, 좋아하는것:{self.like}")

김철수 = Student("김철수", 17, "축구")
장다인 = Student("김다인", 5, "헬로카봇")
김철수.studentInfo()
장다인.studentInfo()

class Mother():
    def characteristic(self):
        print("키가 크다.")
        print("공부를 잘한다.")

class Daugher(Mother):
    def characteristic(self):   #Mother클래스를 상속받음
        super().characteristic()
        print("운동을 잘한다.")

엄마 = Mother()
딸 = Daugher()
print("엄마는")
엄마.characteristic()
print("딸은")
딸.characteristic()

class Mother1():
    def __init__(self):
        print("키가 크다.")
        print("공부를 잘한다.")

class Daughter1(Mother1):
    def __init__(self):
        super().__init__()
        print("운동을 잘한다.")
    
print("엄마는")
엄마 = Mother1()
print("딸은")
딸 = Daughter1()