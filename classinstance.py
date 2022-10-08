
class item:
    discount_rate = 0.8

    def __init__(self,product_name,description,price,quantity):
        self.product_name = product_name
        self.description = description
        self.price = price
        self.quantity = quantity

    def edit_product_description(self,updated_description):
        self.description = updated_description
        return updated_description

    def calculate_product_price(self):
        return self.price * self.quantity

    def apply_discount(self,total):
        if total > 100:
            return total* self.discount_rate


item1 = item('watch','Best build-in features to assist with the fitness',20,2)
item2 = item('Laptop','Dell leading laptop producer',250000,1)

print(type(item))
print(item1.product_name)
print(type(item2))

print(item2.description)
print(item2.edit_product_description('This laptop has 8 GB ram and 256 GB ROM'))
print(item2.description)
print(item1.apply_discount(150))
