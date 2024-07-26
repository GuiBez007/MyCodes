# Create a unique tuple with product names and its respective prices. At the end, show a price list in a tabular form.

products = (
            "Pencil", 1.75,
            "Eraser", 2.00,
            "Notebook", 15.90,
            "Case", 25.00,
            "Protractor", 4.20,
            "Compass", 9.99,
            "Bag", 120.32,
            "Pens", 22.30,
            "Book", 34.90
            )

print(f'{'PRODUCT':15}{'PRICE':>6}')
for i in range(len(products)):
    if i % 2 == 0:
        print(f'{products[i]:15}', end='')
    else:
        print(f'{products[i]:>6.2f}')

input() #wait