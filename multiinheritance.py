class Parent:
    def fun1(self):
        print("this is parent class")
class Child(Parent):
    def fun2(self):
        print("this is child class")
class GrandChild(Child):
    def fun3(self):
        print("this is grandchild class")
obj = GrandChild()
obj.fun1()
obj.fun2()
obj.fun3()