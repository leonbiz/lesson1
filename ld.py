phones = ["iPhone Xs", "Xiaomi Mi8", "Samsung S20", "iPhone Xs"]

# print(phones)

# phones.remove('iPhone X')
# print(phones)

product = {
    "name": "iPhone Xs", 
    "stock": 5, 
    "price": 65000.0,
    "recomend": phones
    }


print(product['recomend'])
print(product['recomend'][1])

product['recomend'].append("iPhone 6")

print(product)