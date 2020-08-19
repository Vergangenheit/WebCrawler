import pyodbc


class DbConn(object):
    def __init__(self):
        self.cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=(local);DATABASE=Crawl;Trusted_Connection=yes;UID=User')
        self.cursor = self.cnxn.cursor()

    def write_to_db(self, product, price, site):
        self.cursor.execute("insert into Results(Product, Price,Site) values (?, ?, ?)", product.text, price.text, site)
        self.cnxn.commit()
