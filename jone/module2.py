def listmodule():
    data = []
    while True:
        l1 = input('enter items? ')
        data.append(l1)
        l2 = input('any other item? (y/n)')
        if l2.casefold() == 'n':
            break
    for h in data:
        print(h)
        if len(h)>5:
            print(h)
            break

listmodule()
