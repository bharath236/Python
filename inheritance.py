class Human:
    def __init__(self,name,occupation):
        self.name = name
        self.occupation = occupation
    def do_work(self):
        if self.occupation == "tennis player":
            print(self.name,"plays tennis")
        elif self.occupation == "actor":
            print(self.name, "shoots film")
        elif self.occupation == "business":
            print(self.name,"doing business")
    def speaks(self):
        print(self.name, "says how are you?")
tom = Human("tom cruise,","business")
tom.do_work()
tom.speaks()