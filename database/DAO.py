from database.DB_connect import DBConnect
from model.retailer import Retailer


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllAnni():
        cnx=DBConnect.get_connection()
        cursor=cnx.cursor(dictionary=True)

        query="""select distinct year(Date) as anno
                    from go_daily_sales 
                    order by anno"""

        cursor.execute(query)

        res=[]


        for row in cursor:
            res.append(row["anno"])


        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getAllBrand():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """select distinct Product_brand as brand
                    from go_products  
                    order by brand"""

        cursor.execute(query)

        res = []

        for row in cursor:
            res.append(row["brand"])


        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getAllRetailer():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)

        query = """select *
                    from go_retailers """

        cursor.execute(query)

        res = []

        for row in cursor:
            res.append(Retailer(**row))


        cursor.close()
        cnx.close()
        return res