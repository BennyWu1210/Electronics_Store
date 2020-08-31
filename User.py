class User:
    def __init__(self, user_name, name, age, gender, address, credit_card, shopping_history, admin=False):
        self.user_name = user_name
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address
        self.credit_card = credit_card
        self.history = shopping_history
        self.cart = []
        self.admin = admin

    def display_cart(self):
        print("This is what you currently have in your shopping cart:")
        for i in range(len(self.cart)):
            print(i + ': ' + self.cart[i][0] + " $" + self.cart[i][1])

    def check_out(self, items):
        for item in self.cart:
            product = item[0]
            qty = item[1]
            print("You've bought " + qty + " " + product.name + " for $" + product.price * qty)
        self.history.append(items)
