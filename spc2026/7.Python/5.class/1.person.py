# class는 무언가를 정의하는 틀이다. class instantiation을 통해 객체를 생성한다.
class Person:
  # 초기화 메서드
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self):
    print(f"Hello, my name is {self.name} and I am {self.age} years old.")

person = Person("John", 30)
person.greet()