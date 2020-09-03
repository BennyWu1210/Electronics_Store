from Products import *
from User import *
import csv
import time
import hashlib
import json
import datetime  # save date to shop history.


products = []
user_info = {}
user_dir = 'User info/'
logged_user = None
product_dict = {Phones: 'Phones.csv',
                Computers: 'Computers.csv',
                CDs: 'CD.csv',
                DVDs: 'DVD.csv'}

# Aug 31
# todo: 1. Optimize the sell function(perhaps create a virtual object to store the stock of a product's stock)
#  2. generate product id (uuid?)
#  3. Save id in the 'items' dictionary instead of name


def read(file):
    # todo reader and writer save as function
    f = open("Encrypted password.csv")
    reader = csv.reader(file, delimiter=',')
    pass


def take_info(user):
    name = input("Enter your name:")
    user_file = user + '.json'
    age = input("Enter your age:")
    gender = input("Enter your gender:")
    address = input("Enter your address:")
    credit_card = input("Credit card:")
    with open(user_dir + user_file, 'a') as outfile:
        json.dump({user: {'name': name, 'age': age, 'gender': gender,
                          'address': address, 'credit_card': credit_card, 'shopping_his': []}}, outfile, indent=1)


def create_account():
    r = open('Encrypted password.csv')

    creating = True
    while creating:
        valid = True
        f = open("Encrypted password.csv")
        reader = csv.reader(f, delimiter=',')
        f = open('Encrypted password.csv', 'a')
        appender = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        user_name = input("Please create a user name:")
        for lines in reader:
            if lines[0] == user_name:
                print("This username already exists!")
                valid = False
                break
        if valid:  # When the username is valid
            password = input("Please create your password:")  # take password
            hashed = hashlib.sha256(password.encode()).hexdigest()  # hash the password
            appender.writerow([user_name, hashed])
            take_info(user_name)  # Take user info
            print("You've created an account, now please log in")
            creating = False


def login():
    user_name = input("Please enter your user name:")
    logging = True
    while logging:
        file = open("Encrypted password.csv")
        reader = csv.reader(file, delimiter=',')
        for lines in reader:
            if lines[0] == user_name:
                pw = input("Please enter your password:")
                password = hashlib.sha256(pw.encode())
                if password.hexdigest() == lines[1]:
                    print("You've logged in!")
                    with open(user_dir + user_name + '.json', 'r') as file:
                        data = json.load(file)[user_name]
                        global logged_user
                        logged_user = User(user_name, data['name'], data['age'], data['gender'],
                                           data['address'], data['credit_card'], data['shopping_his'])
                    logging = False
                else:
                    print("Invalid password!")
        if logging:
            user_name = input("Can't find this user, please reenter:")


def shopping_cart():
    print("Shopping cart")

    removing = True
    remove_list = []
    while removing:
        logged_user.display_cart()
        item = int(input("Enter the index of the item you want to remove(-1 to submit):"))
        remove_list.append(item)
        if item == -1:
            removing = False
            remove_list.remove(-1)
            remove_list.sort(reverse=True)
            for item in remove_list:
                logged_user.cart.pop(item)

        for index in remove_list:
            print(logged_user.cart[index][0].name, logged_user.cart[index][0].price*logged_user.cart[index][1])

    changing_quantity = True
    while changing_quantity:
        logged_user.display_cart()
        item = int(input("Enter the index of the item you want to change(-1 to submit):"))
        quantity = int(input("Enter the quantity you want to change for " + logged_user.cart[item][0]))
        logged_user.cart[item][1] += quantity


def check_out():
    checking_out = True
    while checking_out:
        items = {}
        print("You've bought:")
        for product_list in logged_user.cart:
            product = product_list[0]
            quantity = product_list[1]
            if product in items:
                items[product] += quantity
            else:
                items[product] = quantity
            product.stock -= quantity
            print(quantity + ' ' + product + ' $' + float(quantity * product.price))
        # TODO save ID in the dictionary instead of the name
        logged_user.check_out(items)


def create_products():
    adding = True
    while adding:
        i = 0
        _dict = {}

        for product in product_dict.values():
            i += 1
            _dict[product] = i
            print(str(i) + ": " + product)
        types = input("choose the type of product:")
        name = input('Name:')
        price = input('Price:')
        brand = input('Brand:')
        color = input('Color:')
        stock = input('Stock:')
        warranty_time = input('warranty_time:')
        warranty_cost = input('warranty_cost:')




def store_products():
    product_dir = 'Products'
    for p in product_dict:
        types = p
        file = product_dir + '/' + product_dict[p]
        f = open(file)
        reader = csv.reader(f, delimiter=',')
        info = []
        for i in reader:
            info.append(i)

        for i in range(len(info)):
            if types == Phones or types == Computers:
                products.append(types(info[i][0], info[i][1], info[i][2], info[i][3],
                                      info[i][4], info[i][5], info[i][6], info[i][7]))

            else:
                products.append(types(info[i][0], info[i][1], info[i][2], info[i][3], info[i][4], info[i][5]))

        """QUESTION!!!
        How would you simplify the expression above regarding to storing the elements in the list to a class?"""


def redirect():
    option = input("Enter: 1 --> Menu; 2 --> purchase items; 3 --> shopping cart; 4 --> check out;")
    if option == '1':
        menu()
    elif option == '2':
        sell()
    elif option == '3':
        shopping_cart()
    elif option == '4':
        check_out()


def menu():
    print("Welcome to Benny's store ")
    account = input("Press 1 if you have an account already. Press 2 to sign up")
    while account != '1':
        if account == '2':
            create_account()
            break
        else:
            print("Invalid option")
            account = input("Press 1 if you have an account already. Press 1 to sign up")
    login()

    print("HI " + logged_user.name + '!!!')
    time.sleep(0.3)
    redirect()


def sell():
    print("These are the products we have:")
    time.sleep(0.3)
    for i in range(len(products)):
        print(str(i + 1) + ": " + str(products[i]))
        time.sleep(0.05)

    buying = True
    while buying:
        item = int(input("Choose the number corresponding to the item you want to purchase(0 to check out):"))
        if item == 0:
            buying = False
            shopping_cart()
        else:
            product = products[item - 1]
            cart = logged_user.cart
            quantity = int(input("How many " + product.name + " do you want?"))
            if int(product.stock) < quantity:
                item = int(input("We only have " + product.stock + " " + product.name + ", please enter again: "))
            else:
                print("You've added " + product.name + " into your shopping cart.")
                cart.append([product, quantity])


store_products()
menu()
sell()
