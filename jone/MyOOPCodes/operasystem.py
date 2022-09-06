from databases import User, Product
User.create(name = "Jonathan", email = "jonathan@gmail.com", password = "123")
User.create(name = "Brian", email = "brian@gmail.com", password = "123")
User.create(name = "Sammy", email = "sammy@gmail.com", password = "123")
User.create(name = "Elvis", email = "Elvis@gmail.com", password = "123")
User.create(name = "Shadrack", email = "shadrack@gmail.com", password = "123")
User.create(name = "Tracey", email = "tracey@gmail.com", password = "123")

users = User.select()
for User in users:
    print(User.name, User.email, User.password )


Product.create(productname = 'OMO', productprice = 'Ksh.50', productQtty= '1KG')
Product.create(productname = 'Elianto', productprice = 'Ksh.250', productQtty= '2KG')
Product.create(productname = 'Sony Sugar', productprice = 'Ksh.90', productQtty= '50G')
Product.create(productname = 'Simba cement', productprice = 'Ksh.50,000', productQtty= '1T')

products = Product.select()
for Product in products:
    print(Product.productname, Product.productprice, Product.productQtty)