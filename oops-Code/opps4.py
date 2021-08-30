class Laptop:
    def __init__(self,brand,model_name,price):
        #instance veriable
        self.brand=brand
        self.model_name=model_name
        self.price=price
        self.laptop_name= brand + ' '+model_name


    def apply_discount(self,num):
        #self.price
        off_price = (num/100)*self.price
        return self.price - off_price


laptop1=Laptop('hp','ld758',60000)
laptop2=Laptop('apple','macbook pro',120000)
print(laptop2.apply_discount(10))