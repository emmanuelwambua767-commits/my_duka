# import psycopg2
# #establishing a connection to a postgres db
# conn=psycopg2.connect(host='localhost',port=5432,user='postgres',password='9467',dbname='myduka')
#  #cursor object
# cur=conn.cursor()

# def get_sales():
#     cur.execute('select * from sales')
#     sales_data=cur.fetchall()
#     print(sales_data)

# # def get_stocks():
# #     cur.execute('select * from stock')
# #     stocks_data=cur.fetchall()
# #     print(stocks_data)