from email.policy import default
import json
import random

# Zad 1
lambda1 = lambda x: x + 15
lambda2 = lambda x, y: x * y
print(f'Wynik lambda_1 {lambda1(10)}')
print(f'Wynik lambda_2 {lambda2(6, 8)}')

# Zad 2
mylist = [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
          {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
          {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
slist = []
for myvar in mylist:
    slist.append(sorted(myvar.items(), key=lambda item: str(item[1])))
print(slist)

# Zad 3
listofnumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listofnumbersDoKwadratu = list(map(lambda x: x ** 2, listofnumbers))
listofnumbersDoSzeczcianu = list(map(lambda x: x ** 3, listofnumbers))
print(listofnumbersDoKwadratu)
print(listofnumbersDoSzeczcianu)

