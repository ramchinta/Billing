import parameters

class Add:
    def __init__(self):
        self.mysqlConn = parameters.mysqlConn

    def newProduct(self,productName,productQty,productPrice,productDescription):
        mysqlCur = self.mysqlConn.cursor()
        mysqlCur.execute("insert into products(productName,productQty,productPrice,productDescription) values ('" + productName +"'," + productQty + "," + productPrice + ",'" + productDescription + "');")
        print('New Product Added')

Add().newProduct('Mucinex','5','15.4','bronchitis')