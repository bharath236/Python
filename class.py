class Mobile():
    def __init__(self,model,camera,name):
        self.model = model 
        self.camera = camera
        self.name = name 
    def make_call(self,number):
        print("calling...{}".format(number))

    def get_model(self):
        print(self.model)

    def update_model(self,model):
        self.model = model

mobile_obj = Mobile("Galaxy M51","64MP", "Samsung")

mobile_obj.get_model()

mobile_obj.update_model("Galaxy M53")

mobile_obj.get_model()