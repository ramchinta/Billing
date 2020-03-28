import parameters

class Add:
    def __init__(self):
        self.mysqlConn = parameters.mysqlConn

    def newProduct(self,productName,productQty,productPrice,productDescription):
        mysqlCur = self.mysqlConn.cursor()
        mysqlCur.execute("insert into products(productName,productQty,productPrice,productDescription) values ('" + productName +"'," + productQty + "," + productPrice + ",'" + productDescription + "');")
        return 'New Product Added'

    def updateQty(self,productName,addQty):
        mysqlCur = self.mysqlConn.cursor()
        mysqlCur.execute("update products set productQty = productQty + " + addQty + " where productName = '" + productName +"'")
        return 'Product Qty Updated'

#Add().newProduct('Mucinex','5','15.4','bronchitis')
#Add().updateQty('Mucinex','3')