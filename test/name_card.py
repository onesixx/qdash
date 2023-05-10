name = "kimyuna"
email = "yunakim@naver.com"
addr = "seoul"

name2 = "DusanBack"
email2 = "dusan.back@naver.com"
addr2 = "Kyunggi"

# https://wikidocs.net/1076
def print_biz_card(name, email, addr):
    print("------------------------------")
    print(f"Name: {name}")
    print(f"E-mail: {email}")
    print(f"Addr: {addr}")
    print("------------------------------")

print_biz_card(name, email , addr)
print_biz_card(name2, email2 , addr2)

class BizCard:
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