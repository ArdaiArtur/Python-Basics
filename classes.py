class MyClass:
  x = 5
  
  
  p1 = MyClass()
print(p1.x)
  
  
  
  
  class Person1:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person1("John", 36)

print(p1.name)
print(p1.age)
  
  
  class Person2:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person2("John", 36)
p1.myfunc()
  
  
  
  class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()
