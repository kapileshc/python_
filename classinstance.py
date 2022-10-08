import csv
class item:
    discount_rate = 0.8
    all=[]

    def __init__(self,product_name,description,price,quantity):
        #run validation
        assert price>= 0 , f'price {price} always should be positive'

        #initialise a value in class
        self.product_name = product_name
        self.description = description
        self.price = price
        self.quantity = quantity

        item.all.append(self)

    def edit_product_description(self,updated_description):
        self.description = updated_description
        return updated_description

    def calculate_product_price(self):
        return self.price * self.quantity

    def apply_discount(self,total):
        if total > 100:
            return total* self.discount_rate
    @classmethod
    def import_instance_from_csv(cls):
        with open('products.csv','r') as file:
            reader = csv.DictReader(file)
            items = list(reader)

            print(items)
            for i in items:
                item(product_name= i.get('product_name'),
                     description= i.get('description'),
                     price= int(i.get('price')),
                     quantity=  i.get('quantity'))

    @staticmethod
    def is_integer(num):
        if isinstance(num,float):
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False

    def __repr__(self):
        return f'{self.product_name}'


item1 = item('watch','Best build-in features to assist with the fitness',20,2)
item2 = item('Laptop','Dell leading laptop producer',250000,1)
item3 = item('mouse','zzebronics a best option',160,3)

item.import_instance_from_csv()

print(item.all)

for instance in item.all:
    print(instance.product_name)
print(type(item))
print(item1.product_name)
print(type(item2))

print(item2.description)
print(item2.edit_product_description('This laptop has 8 GB ram and 256 GB ROM'))
print(item2.description)
print(item1.apply_discount(150))
