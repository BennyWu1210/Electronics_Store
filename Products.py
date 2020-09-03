class Products:
    def __init__(self, product_id, name, brand, price, stock):
        self.id = product_id
        self.name = name
        self.brand = brand
        self.price = price
        self.stock = stock

    def __str__(self):
        return self.name + ': $' + str(self.price)

    def values(self):
        return self.price*self.stock

    def remaining(self):
        print('There are ' + str(self.stock) + ' ' + self.name + ' left')


class Devices(Products):
    def __init__(self, product_id, name, brand, price, color, stock, warranty_time, warranty_cost):
        Products.__init__(self, product_id, name, brand, price, stock)
        self.warranty_cost = warranty_cost
        self.warranty_time = warranty_time
        self.color = color


class Phones(Devices):
    def __init__(self, product_id, name, price, brand, color, stock, warranty_time, warranty_cost):
        Devices.__init__(self, product_id, name, brand, price, color, stock, warranty_time, warranty_cost)


class Computers(Devices):
    def __init__(self, product_id, name, price, brand, color, stock, warranty_time, warranty_cost):
        Devices.__init__(self, product_id, name, brand, price, color, stock, warranty_time, warranty_cost)


class Media(Products):
    def __init__(self, product_id, name, brand, price, stock, time):
        Products.__init__(self, product_id, name, brand, price, stock)
        self.time = time


class CDs(Media):
    def __init__(self, product_id, name, price, stock, brand, time):
        Media.__init__(self, product_id, name, brand, price, stock, time)


class DVDs(Media):
    def __init__(self, product_id, name, price, stock, brand, time):
        Media.__init__(self, product_id, name, brand, price, stock, time)


class Accessories(Products):
    def __init__(self, product_id, name, brand, price, stock):
        Products.__init__(self, product_id, name, brand, price, stock)


class Appliances(Products):
    def __init__(self, product_id, name, brand, price, stock, warranty_time, warranty_cost):
        Products.__init__(self, product_id, name, brand, price, stock)
        self.warranty_cost = warranty_cost
        self.warranty_time = warranty_time



    """
    Warranty information
    
    """

""" Classes:
Devices, Media, Accessories, Appliances"""

# Devices: Phones & computers
# Media: CDs & DVDs
# Accessories: ...
# Appliances: Warranties
