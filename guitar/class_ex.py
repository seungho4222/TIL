class Person:
    count = 0

    def __init__(self, name, age): # 생성자 메서드 / self가 가리키는 객체공간에 name, age 필드 생성
        self.__name = name      # 더블언더스코어(__)를 통해 프라이빗필드 생성
        self.__age = age
        Person.count += 1
        print(f'{self.__name} 객체가 생성되었습니다.')

    def __del__(self): # 소멸자 메서드
        print(f'{self.__name} 객체가 제거되었습니다.')

    # def to_str(self):
    #     return f'{self.__name} {self.__age}'
    
    @property
    def name(self):     # 변수처럼 사용 가능, __name 필드값을 반환하는 getter메서드의 역할
        return self.__name
    
    @property
    def age(self):      # 변수처럼 사용 가능, __age 필드값을 반환하는 getter메서드의 역할
        return self.__age
    
    @age.setter                 # 변수처럼 사용 가능, __name 필드값을 반환하는 setter메서드의 역할
    def age(self, age):     # __age 필드의 값을 변경하는 메서드
        if age < 0:
            raise TypeError("나이는 0이상의 값만 허용합니다.")
        self.__age = age

    @classmethod
    def get_info(cls):      # class 참조 정보가 인자로 넘어올 매개변수
        return f'현재 Person 클래스의 인스터스는 총 {cls.count} 개입니다.'

    def __gt__(self, other):
        return self.__age > other.__age

    def __ge__(self, other):
        return self.__age >= other.__age

    def __lt__(self, other):
        return self.__age < other.__age

    def __le__(self, other):
        return self.__age <= other.__age

    def __eq__(self, other):
        return self.__age == other.__age

    def __ne__(self, other):
        return self.__age != other.__age
    
    def __str__(self):
        return f'{self.__name} {self.__age}'
        
    
members = [             # 객체 생성
    Person("홍길동", 20),
    Person("이순신", 45), 
    Person("강감찬", 35)
]

for member in members:
    print(str(member))      # Person 클래스의 객체 전달하면 __str__ 메서드 호출

# cnt = len(members)
# i = 0
# while True:
#     print(f'members[{i}] > members[{i + 1}] => {members[i] > members[i + 1]}')
#     i += 1
#     if i == cnt - 1:
#         print(f'members[{i}] > members[{0}] => {members[i] > members[0]}')
#         break

# print(Person.get_info()) 

# members[0].age = 22     # age@property 데코레이터를 이용해 변수처럼 값 저장

# for member in members:
#     print(member.to_str())


"""
getter : 멤버를 읽어오는 메서드
setter : 멤버를 변경하는 메서드
"""