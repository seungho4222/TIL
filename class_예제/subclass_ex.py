class Parent:
    def __init__(self, family_name):
        self.__family_name = family_name
        print('Parent 클래스의 __init__()...')

    @property
    def family_name(self):
        return self.__family_name
    
    def print_info(self):
        print(f'Parent: {self.family_name}')


class Child(Parent):    # Parent 클래스 상속
    def __init__(self, first_name, last_name):
        Parent.__init__(self, last_name)    # 부모 클래스의 __family_name 필드를 매개변수 last_name으로 초기화
        # super().__init__(last_name)
        self.__first_name = first_name     # 매개변수 first_name에 의해 초기화됨
        print('Child 클래스의 __init__()...')

    @property
    def first_name(self):
        return self.__first_name
    
    @first_name.setter
    def first_name(self, first_name):
        self.__first_name = first_name

    @property
    def name(self):
        return f'{self.family_name} {self.first_name}'
    
    def print_info(self):
        Parent.print_info(self)
        # super().print_info()
        print(f'Child: {self.name}')

child = Child("길동", "홍")
child.print_info()

# print(child.family_name)
# print(child.first_name)
# print(child.name)
# print('======>')
# child.first_name = '길순'
# print(child.name)