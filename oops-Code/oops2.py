class Laptop:
    def __init__(self,brand,model_name,price):
        #instance veriable
        self.brand=brand
        self.model_name=model_name
        self.price=price
        self.laptop_name= brand + ' '+model_name

laptop1=Laptop('hp','ld758',60000)

print(laptop1.brand)
print(laptop1.laptop_name)