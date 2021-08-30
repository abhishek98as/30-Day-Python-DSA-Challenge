class Laptop:
    discount_percent=10
    def __init__(self,brand,model_name,price):
        #instance veriable
        self.brand=brand
        self.model_name=model_name
        self.price=price
        self.laptop_name= brand + ' '+model_name


    def apply_discount(self):
        #self.price
        off_price = (Laptop.discount_percent/100)*self.price
        return self.price - off_price


laptop1=Laptop('hp','ld758',60000)
laptop2=Laptop('apple','macbook pro',120000)
print(laptop1.apply_discount())

print(laptop1.__dict__)