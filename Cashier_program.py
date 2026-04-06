#Bismillah
a = 0
total = 0
basket = []
menu = {'apple':15,
        'bread':10,
        'milk':15,
        'chocolate':25,
        'banana':20
}
def count():
    global total
    for i in basket:
        total = total + int(i)
    print('You collect', len(basket), 'things')
    print('Total is: ', total)

while a < 1:
    ask = input('Choice your products: ').lower()
    if ask == 'apple':
        basket.append(menu['apple'])
    elif ask == 'bread':
        basket.append(menu['bread'])
    elif ask == 'milk':
        basket.append(menu['milk'])
    elif ask == 'chocolate':
        basket.append(menu['chocolate'])
    elif ask == 'banana':
        basket.append(menu['banana'])
    elif ask == 'stop':
        break
    else:
        print('Please choice another thing!')
count()