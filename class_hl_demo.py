# 封装

"""class Car:

    def __init__(self, brand, money, year, owner):
        self.brand = brand
        self.money = money
        self.year = year
        self.__owner = owner

    def running(self):
        return self.brand, self.money, self.year

    def total_cost(self, discount):
        return self.money * (1 + discount)

    def get_owner(self):
        return self.__owner[0:1] + "**"

"""

# 继承

"""class Car:
    def __init__(self, c_color, c_brand, c_model, owner):
        self.color = c_color
        self.brand = c_brand
        self.model = c_model
        self.__owner = owner

    def start(self):
        print(f"{self.brand}{self.model}正在启动...")

    def stop(self):
        print(f"{self.brand}{self.model}停止行驶...")

    def run(self):
        print(f"{self.brand}{self.model}正在行驶...")

    # 要重写的方法
    def charge(self):
        print(f"{self.brand}{self.model}正在补充燃料...")


class FuelCar(Car):
    # 重写
    def charge(self):
        super().charge()
        print(f"{self.brand}{self.model}正在加油...")

    pass


class ElectricCar(Car):
    # 重写
    def charge(self):
        super().charge()
        print(f"{self.brand}{self.model}正在充电...")

    pass"""

# 多态

"""def handle_charge(car: Car):
    car.charge()"""

## 多态-鸭子类型

"""class Duck:
    def __init__(self, name):
        self.name = name

    def swimming(self):
        print(self.name + "正在游泳......")


class Dog:
    def __init__(self, name):
        self.name = name

    def swimming(self):
        print(self.name + "正在游泳......")


class Pig:
    def __init__(self, name):
        self.name = name

    def swimming(self):
        print(self.name + "正在游泳......")


def handle_swimming(duck):
    duck.swimming()"""

"""
案例
某社区图书馆需要开发一个简单的图书管理系统。系统需要支持会员登录、图书借阅、图书归还等功能。系统中有两种类型的会员：普通会员和VIP会员，他们的借书权限不同。你需要使用面向对象编程的思想，设计并实现这个图书管理系统。
核心功能：
1.会员登录：会员通过卡号和密码登录系统
2.借书：会员可以借阅库存中有余量的图书
3.还书：会员可以归还借阅的图书
4.查看我的借阅：展示当前会员已经借阅的图书列表
5.退出系统
借阅规则：
1.普通会员最多可借3本
2.VIP会员最多可借 6+VIP等级 本（VIP等级，默认为1）
注意：
登录成功（卡号和密码均正确）后，才可以访问该系统
图书库存不足，或当前会员借书数量达到最大借书数量，不能再借新书
"""

from abc import ABC, abstractmethod


class People(ABC):

    def __init__(self, username, password):
        self.username = username
        self.__password = password
        self.__book_list = []

    def get_password(self):
        return self.__password

    @abstractmethod
    def borrow_book_max(self):
        return 3

    def borrow_book(self, book):
        if len(self.__book_list) < self.borrow_book_max():
            self.__book_list.append(book)
            print(f'借阅成功,还可以借{self.borrow_book_max() - len(self.__book_list)}本')
        else:
            print('当前用户借书已达上限')

    def back_book(self, book):
        self.__book_list.remove(book)
        print('归还成功～')

    def show_book(self):
        for book in self.__book_list:
            print(book)


class VIP(People):
    def __init__(self, username, password, level=1):
        super().__init__(username, password)
        self.level = level

    def borrow_book_max(self):
        return 6 + self.level


class Book:
    def __init__(self, name, count):
        self.name = name
        self.__count = count

    def __str__(self):
        return f"图书名称：{self.name},图书存量：{self.__count}"

    def borrow(self):
        if self.__count <= 0:
            print('借阅失败，当前图书数量不足')
            return False
        else:
            self.__count -= 1
            return True

    def back(self):
        self.__count += 1


class System:
    __book_List = []
    people: People

    def __init__(self, login_state=False):
        self.login_state = login_state
        print('系统初始化成功～')

    def update_book(self, book_List):
        self.__book_List = book_List

    def login(self):
        username = input('请输入登录账号：')
        password = input('请输入密码：')
        if username == "xiaoming" and password == "123":
            self.people = People(username, password)
            self.login_state = True
        elif username == "xiaohong" and password == "123":
            self.people = VIP(username, password, 4)
            self.login_state = True
        elif username == "xiaogang" and password == "123":
            self.people = VIP(username, password, 1)
            self.login_state = True
        else:
            print("账户或密码错误～")
            self.login_state = False

    def check(self):
        print("库存：")
        for book in self.__book_List:
            if book.count > 0:
                print(f"图书名字：{book.name}, 图书数量：{book.count}")

    def borrow(self):
        book_name = input('请输入要借阅的图书名字:')
        for book in self.__book_List:
            if book.name == book_name:
                if book.borrow():
                    self.people.borrow_book(book)

    def back(self):
        book_name = input('请输入要归还的图书名字:')
        for book in self.__book_List:
            if book.name == book_name:
                book.back()
                self.people.back_book(book)

    def show_book(self):
        self.people.show_book()

    def run(self):
        while True:
            if self.login_state:
                print(f"当前登录账户 {self.people.username},可借图书 {self.people.borrow_book_max()}")
            print('欢迎来到图书管理系统～')
            print('1.会员登录')
            print('2.借书')
            print('3.还书')
            print('4.查看我的订阅')
            print('5.退出系统')
            try:
                operation = int(input('请选择要进行的操作：'))
                match operation:
                    case 1:
                        self.login()
                    case 2:
                        if not self.login_state:
                            print('请先登录～')
                            continue
                        self.borrow()
                    case 3:
                        if not self.login_state:
                            print('请先登录～')
                            continue
                        self.back()
                    case 4:
                        if not self.login_state:
                            print('请先登录～')
                            continue
                        self.show_book()
                    case 5:
                        print('退出成功～')
                        break
            except Exception as e:
                print(e)


if __name__ == "__main__":
    """
    car = Car('宝马', 3000, "1924", "灰太狼")
    print(car.money)
    print(car.year)
    print(car.money)
    print(car.running())
    print(car.total_cost(0.95))
    print(car.get_owner())
    # print(car.__owner) 报错 外部不能直接访问类私有对象
    print(car.__dict__)
    """

    """fuelCar = FuelCar('红色', 'X5', "宝马", "灰太狼")
    fuelCar.run()
    fuelCar.stop()
    fuelCar.charge()

    ## 多态调用
    print("=" * 60)
    handle_charge(FuelCar('红色', 'X5', "宝马", "灰太狼"))
    handle_charge(ElectricCar('白色', '**', "特斯拉", "红太狼"))

    ## 多态——鸭子类型
    print("=" * 60)
    handle_swimming(Duck('鸭子'))
    handle_swimming(Dog('狗'))
    handle_swimming(Pig('猪'))"""

    system = System()
    book1 = Book('xiaowangzi', 5)
    book2 = Book('c++', 1)
    book3 = Book('c', 2)
    system.update_book([book1, book2, book3])
    system.run()
