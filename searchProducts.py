import parameters

class search:
    def __init__(self):
        self.mysqlConn = parameters.mysqlConn

    def viewProducts(self):
        mysqlCur = self.mysqlConn.cursor()
        mysqlCur.execute("select productName,productQty,productPrice from BillingSystem.products")
        rows = mysqlCur.fetchall()
        return rows

    def searchProduct(self,productName):
        mysqlCur = self.mysqlConn.cursor()
        mysqlCur.execute("select productName,productQty,productPrice from BillingSystem.products where productName like '%" + productName + "%' or productDescription like '%"+ productName +"%'")
        rows = mysqlCur.fetchall()
        return rows

#print(search().viewProducts())
#print(search().searchProduct('bengay'))