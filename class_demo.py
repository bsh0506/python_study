# 面向对象
class Car:
    def __init__(self, brand, money, year):
        self.brand = brand
        self.money = money
        self.year = year

    def running(self):
        return self.brand, self.money, self.year

    def total_cost(self, discount):
        return self.money * (1 + discount)

    # 魔法方法
    def __str__(self):
        return f"{self.brand} {self.money} {self.year}"

    def __eq__(self, other):
        return self.money == other.money

    def __lt__(self, other):
        return self.money < other.money

    def __call__(self, *args, **kwargs):
        return "call"


car = Car('宝马', 3000, "1924")
car1 = Car('奔驰', 4000, "1930")
print(car.money)
print(car.year)
print(car.money)
print(car.running())
print(car.total_cost(0.95))
print(car.__dict__)
print(car < car1)
print(car == car1)
print(car)
print(car())

# 单例
"""class Agent:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, brand):
        self.brand = brand


a1 = Agent('宝马')
a2 = Agent('奔驰')
print(a1 == a2)
print(a1.brand)


def singleton(cls):
    instances = {}

    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper


@singleton
class Car:
    def __init__(self, brand):
        self.brand = brand


c1 = Car('宝马')
c2 = Car('奔驰')
print(c1 == c2)"""

"""
    采用面向对象编程思想完成如下需求
    采用面向对象的编程思想，完成教务管理系统的开发。教务管理系统可以管理在校学生的成绩信息，通过控制台菜单与用户交互，具体的功能如下：
    1.添加学生成绩：根据输入的学生姓名、语文成绩、数学成绩、英语成绩，记录在系统中
    2.修改学生成绩：根据输入的学生姓名，修改对应的学生成绩
    3.删除学生成绩：根据输入的学生姓名，删除对应的学生成绩
    4.查询指定学生成绩：根据输入的学生姓名，查找对应的学生成绩，并输出
    5.展示全部学生成绩：展示出系统中所有学生的成绩
"""

"""class Student:
    def __init__(self, name, chinese_score, math_score, english_score):
        self.name = name
        self.chinese_score = chinese_score
        self.math_score = math_score
        self.english_score = english_score

    def __str__(self):
        return f"学生姓名:{self.name} 语文成绩:{self.chinese_score} 数学成绩:{self.math_score} 英语成绩:{self.english_score}"


class System:
    __instance = None
    __students: list[Student] = []

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls._instance

    def __str__(self):
        return ""

    def add_student(self, student):
        self.__students.append(student)
        print(f"添加成功～{student}")

    def update_student(self, student):
        for __student in self.__students:
            if __student.name == student.name:
                # 重点：修改原对象属性，不要 _student = student
                __student.chinese_score = student.chinese_score
                __student.math_score = student.math_score
                __student.english_score = student.english_score
                print(f"修改成功～{_student}")
                return
        print("没有找到该学生")

    def remove_student(self, d_name):
        for __student in self._students:
            if __student.name == d_name:
                self.__students.remove(__student)
        print(f"删除成功～")

    def get_student(self, s_name):
        for __student in self.__students:
            if __student.name == s_name:
                print(__student, '查询成功～')
        return None

    def show_students(self):
        for __student in self.__students:
            print(__student)


system = System()
while True:
    print("*" * 20)
    print("    教务管理系统    ")
    print("*  1.添加学生成绩  *")
    print("*  2.修改学生成绩  *")
    print("*  3.删除学生成绩  *")
    print("* 4.查询指定学生成绩*")
    print("* 5.展示全部学生成绩*")
    print("*" * 20)
    operation = input("请输入要操作的序号：")

    if operation == "1":
        name = input("请输入学生姓名：")
        chinese_score = input("请输入语文分数：")
        math_score = input("请输入数学分数：")
        english_score = input("请输入英语分数：")
        system.add_student(Student(name, chinese_score, math_score, english_score))

    elif operation == "2":
        name = input("请输入要修改的学生姓名：")
        chinese_score = input("请输入语文分数：")
        math_score = input("请输入数学分数：")
        english_score = input("请输入英语分数：")
        system.update_student(Student(name, chinese_score, math_score, english_score))

    elif operation == "3":
        name = input("请输入要删除的学生姓名：")
        system.remove_student(name)

    elif operation == "4":
        name = input("请输入要查询的学生姓名：")
        system.get_student(name)

    elif operation == "5":
        print(f"全部学生成绩：")
        system.show_all()

    else:
        print("输入序号无效！")"""
