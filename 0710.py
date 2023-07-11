# ar = ["김구", "김좌진", "안중근", "윤봉길", None]
#
# print(None in ar)
#
# #이름이 3자 이상인 데이터만 출력
# #None 확인 및 제거
#
#
# #한줄 함수를 lambda로 변경
# ar = list(filter(lambda x : x != None , ar))
# print(ar)
#
# result = list(filter(lambda x : len(x) >= 3, ar))
# print(result)
#
# result = list(filter(lambda x : x[0] >= "아" and x[0]< "자" , ar))
# print(result)
#
# #데이터가 collection에 포함되어 있는지 확인 : in(반대는 not in)
#
# ar = ["1", "2", "3"]
#
# kwlist = ["2"]
#
# #ar 에서 kwlist에 있는 것은 제외하고 list로 생성
# for i in ar :
#     if i not in kwlist :
#         print(i)

# key = ["국민학교", "중학교", "고등학교"]
# value = ["만재국민학교", "광주서중", "명덕고등학교"]
#
# print(list(zip(key, value)))
# # print(dict(zip(key, value)))
#
# def outer() :
#     outer_data = "외부 함수의 데이터"
#
#     def inner () :
#         nonlocal outer_data #함수 완전 밖에 변수가 존재할 시, global로 바꾸면 됨
#         print(outer_data) #nonlocal.outer_data
# #
# #         print(outer_data) #nonlocal.outer_data
# #
# #     inner()
# #     print(outer_data)
# #
# # outer()
# # a = outer()
#
# def outer() :
#     amore = "아모르"
#     #자신을 감싸고 있는 함수의 데이터를 수정하는 함수
#     def inner() :
#         nonlocal amore
#         amore = amore + "파티 아모르"
#         print(amore)
#     #함수 내부의 데이터를 수정하는 함수를 리턴하는 함수를 closure 라고 한다.
#     return inner
#
# closure = outer() #함수를 호출해, 리턴하는 함수를 변수에 저장
# closure()
# closure()
# closure()
# closure()

"""
def commonConcern1():
    print("공통 관심 사항_1")

def deco(func):
    print("공통관심사항")
    func()

@deco
def businessLogic():
    print("비지니스 로직")



#이제부터 businessLogic 이라는 함수를 호출하면 deco 라는 함수를 수행합니다.
#개발자가 작성한 코드 대신에 다른 코드를 불러내는 방식을 프록시 패턴이라고 합니다.
#deco 에게 businessLogic이라는 함수가 대입됨.
def commonConcern2():
    print("공통 관심 사항_2")
"""

#고객의 니즈가 변경
# -> 업무로직과는 관계가 없는 로깅을 출력하는 코드를 추가하기를 원하는 방향으로 변경
# 유지보수 과정이나 업무 로직과 관련이 없는 코드를 추가하거나 삭제하는 경우
# 업무 로직을 직접 수정하는 것은 예상치 못한 결과를 만들어 낼 수 있다.
# 이런 경우에는 업무 로직은 손을 대지 않고 가능하도록 만드는 것이 좋습니다.


# def amore(func) :
#     func()
#     print("로깅")
# @amore
# def businessLogic():
#     print("비지니스 로직")
#
# businessLogic()
#
# import time
#
# def clock(func) :
#     #decorator 가 적용된 함수가 호출되면 수행될 실제 함수
#
#     def clocked(*args) :
#         #업무 로직 함수를 호출
#
#         start = time.time() #현재 시간을 기록
#
#         result = func(*args)
#
#         end = time.time()
#         elapsed = end - start #함수의 수행시간
#         print("수행시간 :", elapsed)
#
#         #매개변수 확인
#         print("매개변수 :", args)
#
#         #리턴값
#         print("리턴값 :", result)
#
#         return result
#     return clocked
#
#
# import functools
#
# @functools.lru_cache()
# @clock
# def fibonacci(n) :
#     if n == 1 or n == 2:
#         return 1
#     else :
#         return fibonacci(n-1) + fibonacci(n-2)
#
# print(fibonacci(15))

# class Student :
#     #인스턴스가 있어야만 호출되는 메서드
#     def disp(self):
#         print("인스턴스 생성")
#
#     def setName(self, name):
#         self.name = name #self.name은 인스턴스의 속성으로 만들어진다.
#
# stu = Student()
# stu.setName("파이터")
# print(stu.name)
#
# stu.score = 94 # 인스턴스에 score 이라는 속성이 있으면 수정, 없으면 생성
# print(stu.score)
# # #인스턴스 생성
# student = Student()   #오른쪽이 인스턴스임.
#
# #메서드 호출 - bound 호출
# student.disp()
# Student().disp()
# #메서드 호출 - Unbound 호출
# Student.disp(student)

# class Student :
#     class_data = "클레스의 속성"
#
# student = Student()
# print(Student.class_data) #클래스로 인스턴스 부르기
# print(student.class_data)
# (student.class_data) #인스텈스를 이용해서 클래서 데이터 수정
# print(Student.class_data)
# print(student.class_data)

# class Student:
#     class_data = "클래스의 속성"
#
# #인스턴스 생성해서 대입
# stu1 = Student()
# #인스턴스 생성해서 대입
# stu2 = Student()
# #stu1 의 데이터를 대입 : stu1 이 참조하고 있는 데이터의 참조를 stu3가 참조합니다.
# stu3 = stu1
#
# print(stu1 == stu2) #내부의 데이터가 같은지 확인
# print(stu1 is stu2) #id가 같은지 확인
# print(stu1 is stu3)# true
# print(stu1 == stu3)# true
#
#

#이름과 점수를 갖는 객체를 여러 개 필요

# class Student :
#
#     def getName(self): #매개변수 없음
#         return self.name
#
#     def setName(self, name): #자료형과 동일한 매개변수 1개
#         self.name = name
#
#     def getScore(self):
#         return self.score
#
#     def setScore(self, score):
#         self.score = score
#
# #인스턴스 생성
# stu1 = Student() #메서드 호출
#
# #setter를 이용한 속성 생성과 설정
# stu1.setName("애니")
# stu1.setScore(98)
#
# #getter를 이용한 속성 사용
# print(stu1.getName())
# print(stu1.getScore())
#
# #최근 등장 IDE는 대부분 getter 와 setter를 만드는 유틸을 제공합니다


# class Student :
#     # 이 메서드에서 속성을 생성해서 속성을 처음부터 소유하도록 만들어주는 것이 좋습니다.
#     # 생성자 - 인스턴스를 생성할 때 호출하는 메서드
#     # 매개변수를 이용해서 초기화하면 만들어질 때 다양한 값으로 초기화가 가능
#     # 매개변수를 이용해서 초기화 할 때 매개변수에 기본값을 설정하지 않으면
#     # 인스턴스를 생성할 때 반드시 매개변수에 값을 대입해야 합니다.
#
#     # def __init__(self, name="anonymous"):
#     #     print("인스턴스 생성")
#     #     # 특정한 상수로 생성하고자 하는 경우는 생성자 내부에서 직접 설정
#     #     #self.name = "기본값"
#     #
#     #     self.name = name
#     #
#     # #소멸자 - 인스턴스가 소멸될 때 호출되는 메서드
#     #
#     # def __del__(self):
#     #     print("인스턴스 소멸")
#     def disp(self):
#         print("학생입니까")
#     def getName(self): #매개변수 없음
#         return self.name
#
#     def setName(self, name): #자료형과 동일한 매개변수 1개
#         self.name = name
#
#     def getScore(self):
#         return self.score
#
#     def setScore(self, score):
#         self.score = score
#
# stu1 = Student()
#
#
#
# class Student :
#     #클래스 속성 - 클래스에 1개만 생성
#     auto_increment = 0
#
#     #클래스 속성 과 생성자를 이용한 일련번호 만들기
#     def __init__(self, noame="noname"):
#
#         Student.auto_increment += 1
#         self.no = Student.auto_increment
#         #print(Student.auto_increment)
#
#
#     def __del__(self):
#         print("인스턴스 소멸")
#
#     @staticmethod
#     def method():
#         print("매개변수가 없는 static method") #인스턴스에 매개변수가 필요가 없음.
#
#
#
# stu1 = Student() #인스턴스 생성 및 참조 카운트가 1이 됨
# stu1 = None #참조를 가리키는 변수에 None을 대입하면 참조 카운트가 1 감소
# # 참조 카운트가 0이면 인스턴스가 소멸됩니다.
# Student.method()
#
# stu2 = Student() #참조 카운트 1
# stu3 = stu2 #다른 변수에 참조를 대입하므로 참조 카운트는 1 증가 2
# stu2 = None #참조 카운트가 1 줄어들어도 1 - 인스턴스는 소멸되지 않는다.
# print("프로그램 종료")

# class Student :
#     #name 과 age 속성만 사용하도록 제한
#     __slots__ = ["name", "age"]
#     pass
#
# stu1 = Student()
# stu1.name = "adam"
# stu1.age = 35
# stu1.job = "Singer"

# class Student :
#     def __init__(self):
#         self.name = "adam"
#         self.__no = 1 #속성을 만들 때 __로 시작하면 인스턴스(함수)는 속성에 직접 접근 불가
#
# stu1 = Student()
# print(stu1.name)
# print(stu1.__no)

#속성은 직접 접근 하지 말아야 한다.

# class Student :
#
#     auto_increment = 0
#
#     @classmethod
#     def method(self):
#         Student.auto_increment = 100
#
# #static method 로 만들려면 method(self)가 아닌 method()로 해야한다.
# Student.method() #인스턴스를 만들지 않고 초기화가 가능했다. (속성을 0에서 100으로 바꾸기)

# class Student :
#
#     def __init__(self, name="noname"):
#         self.__name = name #속성 이름이 __로 시작하므로 인스턴스로 접근 불가
#
#     #접근자 메서드
#     @property #getter 설정
#     def name(self):
#         print("name의 getter 호출")
#         return self.__name
#
#     @name.setter #setter 설정
#     def name(self, name):
#         print("name 의 setter 호출")
#         self.__name = name
#
#     #프로퍼티 생성
#     #name을 호출하면 getName 메서드가 호출되고 name에 값을 대입하면 setName 메서드가 호출된다.
#     name = property(fget=name, fset=name)
#
#
# stu = Student()
# #setter, getter를 직접 호출
# #
#
# #property를 이용한 getter와 setter 호출
#
# stu.name = "나이트"
# print(stu.name)
#
# print(help(property))

# class Student :
#
#     def __init__(self, name="noname"):
#         self.name = name
#
#
#     #add 연산 오버로딩
#     def __add__(self, other):
#         return self.name + other.name
#
#     #== 연산자 오버로딩 (name으로 id확인을 대신함)
#     def __eq__(self, other):
#         return self.name == other.name
#
#
# stu1 = Student("강진구")
# stu2 = Student("강진구")
# stu3 = stu1
# print(stu1 + stu2) #add 오버로딩을 이용해 안되던 연산을 수행
# print(stu1.name + stu2.name)
# print(stu1 == stu2) #id를 비교하는게 일반적인데, class호출시 각각의 메모리를 사용하므로, id가 달라짐
# print(stu1 is stu2) #id가 다름
# print(stu1 == stu2) #내용이 같으므로 true가 나옴.
#
#내용 비교는 ==, id 비교는 is

# class Student :
#
#     def __init__(self, name="noname", count = 0):
#         self.name = name
#         self.count = count
#
#     def __add__(self, other):
#         return self.count + other.count
#
# stu1 = Student("사과", 3)
# stu2 = Student("과자", 2)
# print(stu1 + stu2)

# class Sup :
#
#     def __init__(self):
#         self.score = 80
#     def superMethod(self):
#         print("상위 클래스의 메서드")
#
# #Sup 클래스를 상속받는 Sub 클래스
#
# class Sub(Sup):
#     #하위 클래스에서 __init__ 를 생성하면, 상위 클래스의 __init__ 을 호출하지 않는다.
#     #하위 클래스에 __init__을 만들 때는 상위 클래스의 __init__을 호출해 주어야 한다.
#
#     def __init__(self):
#         super().__init__() #하위 클래스의 init에서 중요한 포인트
#         self.name = "noname"
#     def subMethod(self):
#         print("하위 클래스의 메서드")
#
# #Sub의 인스턴스를 생성해서 필요한 메서드 호출
# s = Sub()
# s.subMethod()
# s.superMethod() #Sub 클래스에는 없지만 Sup를 상속받았기 때문에 호출 가능
#
# print(s.score)
#
# class Sup :
#
#     def method(self):
#         print("상위 클래스의 메서드")
#
# #Sup 클래스를 상속받는 Sub 클래스
#
# class Sub(Sup):
#     #상위 클래스에 존재하는 메서드를 하위 클래스에서 다시 정의 - overriding
#     #목적은 기능 확장
#     def method(self):
#         print("하위 클래스의 메서드")
#
#
# #Sub의 인스턴스를 생성해서 필요한 메서드 호출
# s = Sub()
# s.method()
# s.method()

# import abc #absctract class 의 약자 abc
#
# #추상 클래스 - 자신의 인스턴스(동작)을 생성할 수 없음
#
# class AbstractClass(metaclass=abc.ABCMeta) :
#     #추상 메서드 - 내용이 없는 메서드로 하위 클래스에서 구현해서 사용해야 합니다.
#     @abc.abstractmethod
#     def method(self):
#         pass
#
# class Sub(AbstractClass) :
#     def __init__(selfself) :
#         print("인스턴스 생성")
#     #추상 클래스를 상속받는 경우 추상 메서드를 반드시 implementation 해주어야 한다.
#     #만들어주지 않으면 에러
#
#     def method(self):
#         print("추상 메서드 구현")
#
# #instance = AbstractClass() #Can't instantiate abstract class AbstractClass with abstract method method
# #추상 클래스를 추상 메서드로 인스턴스를 만들수 없다. 오로지 상속으로만!
#
# instance = Sub() #에러 why? 하위 클래스에서 메서드를 구현해주어야 함.

