# class Computer:
#     def config(self):
#         print("i5, 1TB,16gb")


# comp1 = Computer();
# print(type(comp1))
# comp1.config()
class Store:
    def __init__(self,name,price,value):
        self.name = name
        self.price = name
        self.value = value

class Shop(Store):
    def __init__(self,shopname,shoptype):
        self.shopname = shopname,
        self.shoptype = shoptype

if __name__ == "__main__":
    n = int(input("Store numbers"))
    sl = []
    for i in range(n):
        n = input("store name: ")
        p = int(input("price"))
        v = int(input('Value'))
        sl.append(Store(n,p,v))
    print(sl)
    

        