import csv
# from Main import *
import hashlib
import json
import User
from datetime import *

now = datetime.now().time()
print(now)

"""def shopping_cart():
    print("Shopping cart")
    for i in range(len(logged_user.cart)):
        print(i + ': ' + logged_user.cart[i][0] + " $" + logged_user.cart[i][1])

    removing = True
    remove_list = []
    while removing:
        item = int(input("Enter the index of the item you want to remove(-1) to submit:"))

        if item == -1:
            removing = False
            remove_list.remove(-1)
            remove_list.sort(reverse=True)
            for item in remove_list:
                remove_list.pop(item)
        remove_list.append(item)
        for index in remove_list:
            print(logged_user.cart[index][0].name, logged_user.cart[index][0].price*logged_user.cart[index][1])

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
        # TODO if quantity larger than stock write something (change amount)
        print(quantity + ' ' + product + ' $' + float(quantity * product.price))

    # TODO save ID in the dictionary instead of the name

    # display items
    # can remove items
    # check out (can be a function): change the stock, remove card, add to history, receipt.
shopping_cart()

data = {}


data['aaa'] = []
data['bbb'] = []
data['ccc'] = []

data['aaa'].append({
    'name': 'Scott\n',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
})
data['bbb'].append({
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
})
data['ccc'].append({
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
})
print(data['aaa'][0]['name'])
with open('User info.json', 'w') as outfile:
    json.dump(data, outfile)
# appending the data


logged_user = None


def login():
    logged_user = 'hi'
    return logged_user

login()

print(logged_user)
lst = [x for x in range(10)]
print(lst)
print(x for x in range(10))

password = input("Please create your password:")
hashed = hashlib.sha256(password.encode())
print(hashed.hexdigest())


f = open('User info.json', 'a')
r = open('User info.json', 'r')
writers = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
reader_obj = csv.reader(r, delimiter=',')
writers.writerow(['john', 'ben', 'cool'])
writers.writerow(['benny', 1234])
for i in reader_obj:
    print(i[0])


f = open('Products/Phones.csv')
john = 'john'
reader_obj = csv.reader(f, delimiter=',')
obj_writer = csv.writer(f, quotechar='"', quoting=csv.QUOTE_MINIMAL)
obj_writer.writerow(john)
obj_writer.writerow('hi')

print(f.read())

for i in reader:
    i[1] += str(1.0)

for i in reader:
    print(float(i[1]))


print(type(products[0].price))
products[0].price = float(products[0].price) - 150
print(type(products[0].price))

for i in products:
    print(i)
"""