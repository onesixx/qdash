name  = "kimyuna"
email = "yunakim@naver.com"
addr  = "seoul"

name2  = "DusanBack"
email2 = "dusan.back@naver.com"
addr2  = "Kyunggi"

# https://wikidocs.net/1076
def print_card(name, email, addr):
    print("------------------------------")
    print(f"Name: {name}")
    print(f"E-mail: {email}")
    print(f"Addr: {addr}")
    print("------------------------------")

print_card(name, email , addr)
print_card(name2, email2 , addr2)


#-------------------------------------------------------------------

class BizCard:
    # self
    def set_info(self, name, email, addr):
        self.name = name
        self.email = email
        self.addr = addr
    def print_info(self):
        print("------------------------------")
        print(f"Name: {self.name}")
        print(f"E-mail: {self.email}")
        print(f"Addr: {self.addr}")
        print("------------------------------")

member1 = BizCard()
member1.set_info("Yuna Kim", "yunakim@naver.com", "Seoul")
member1.print_info()

member2 = BizCard()
member2.set_info("Sarang Lee", "sarang.lee@naver.com", "Kyunggi")
member2.print_info()

#---클래스에 메서드 추가---------------------------------------------------------
# 붕어빵 틀(클래스)을 이용해
# 팥소를 넣지 않은 상태로 붕어빵을 구운 후(인스턴스생성)
# 나중에 다시 붕어빵 안으로 팥소를 넣는 것과 비슷

class BizCard:
    def __init__(self, name, email, addr):
    #def set_info(self, name, email, addr):
        self.name = name
        self.email = email
        self.addr = addr

    def print_info(self):
        print("------------------------------")
        print(f"Name: {self.name}")
        print(f"E-mail: {self.email}")
        print(f"Addr: {self.addr}")
        print("------------------------------")
# https://wikidocs.net/1742
member3 = BizCard("Sarang Lee", "sarang.lee@naver.com", "Kyunggi")
member3.print_info()


#--- 생성자 활용 __init__ (self) -----------------------------------------------
# 어떻게 하면, 팥소를 넣으면 붕어빵을 구워낼수 있을까?
# 어떻게 하면, 초기값 입력과 인스턴스 생성을 한 번에 처리할 수 있을까?

class BizCard:
    def __init__(self, name, email, addr):
        self.name = name
        self.email = email
        self.addr = addr
    # 메서드의 첫번째인자는 항상 self
    def print_info(self):
        print("------------------------------")
        print(f"Name: {self.name}")
        print(f"E-mail: {self.email}")
        print(f"Addr: {self.addr}")
        print("------------------------------")

# 생성되는 인스턴스 그 자체를 의미하는 self는  자동으로 값이 전달
member1 = BizCard("Yuna Kim", "yunakim@naver.com", "Seoul")
member1.print_info()

class Foo:
    def func1():
            print("function 1")
    def func2(self):
            print(id(self))
            print("function 2")
f = Foo()

f.func1()  # [E] takes 0 positional arguments but 1 was given
Foo.func1() #클래스 직접호출, 클래스는 그 자체가 하나의 네임스페이스이기 때문에

f.func2()   # 140200315396832
Foo.func2() # [E] missing 1 required positional argument: 'self'
id(f)       # 140200315396832

g = Foo()
g.func2()     # 140200318246576
Foo.func2(g)  # 140200318246576

#### --- NameSpace ----------------
class Stock:
    market = "kospi"


Stock.__dict__
Stock.market

ins1 = Stock()
id(ins1)
ins1.__dict__
