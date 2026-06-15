import psycopg2
#establishing a connection to a postgres db
conn=psycopg2.connect(host='localhost',port=5432,user='postgres',password='9467',dbname='myduka')
 #cursor object
cur=conn.cursor()
def get_products():
    cur.execute('select * from products')
    products_data=cur.fetchall()
    return products_data

# cur.execute("insert into products(name,buying_price,selling_price)values('wallet',300,500)")
# conn.commit()

def get_sales():
    cur.execute('select * from sales')
    sales_data=cur.fetchall()
    return sales_data

def insert_products2(values):
    cur.execute(f"insert into products(name,buying_price,selling_price)values{values}")
    conn.commit()

product1=('tissue',35,50)
product2=('valon',120,150)
insert_products2(product1)
insert_products2(product2)
products_data=insert_products2
print(products_data)

def insert_products2(values):
    cur.execute(f"insert into products(name,buying_price,selling_price)values(%s,%s,%s)",values)
    conn.commit()

product3=('charger',200,350)
insert_products2(product3)
products_data=insert_products2
print(products_data)
# Q1
def get_stocks():
    cur.execute("select * from stock")
    stocks_data = cur.fetchall()
    return stocks_data

stocks_data = get_stocks()
print(stocks_data)

#insert sales() 

def insert_sales(values):
    cur.execute("insert into sales(pid,quantity)values(%s,%s)",values)
    conn.commit()

# sales1=(2,8,7)
# sales2=(3,12,9)
# sales3=(500,20,4)


# insert_sales(sales1)
# insert_sales(sales2)
# insert_sales(sales3)


# sales_data=get_sales()
# print(sales_data)

# -> insert_stock()
def insert_stock(values):
    cur.execute("insert into stock(pid,stock_quantity)values(%s,%s)",values)
    conn.commit()

stock1=(2,16)
stock2=(5,21)
stock3=(7,35)

# insert_stock(stock1)
# insert_stock(stock2)
# insert_stock(stock3)

stock_data = get_stocks()
print(stock_data)







# sales_per_day

# SELECT DATE(created_at) AS sale_date, SUM(Quantity) AS sales_per_day FROM sales GROUP BY DATE(created_at) ORDER BY sale_date;

# -> profit_per_day

# SELECT DATE(sales.created_at) AS sale_date, SUM((products.selling_price - products.buying_price) * sales.quantity) AS profit_per_day FROM sales JOIN products ON sales.pid = products.id GROUP BY DATE(created_at) ORDER BY sale_date;

# -> sales_per_product

# SELECT name, SUM(sales.quantity) AS sales_per_product FROM sales JOIN products ON sales.pid = products.id GROUP BY name;

# -> profit_per_product

# SELECT name, SUM((products.selling_price - products.buying_price) * sales.quantity) AS profit_per_product FROM sales JOIN products ON sales.pid = products.id GROUP BY name;
def sales_per_day():
    cur.execute("""
      select date(sales.created_at) as date, sum(sales.quantity * products.selling_price) as
      total_sales from sales join products on products.id = sales.pid  group by date;
    """)
    daily_sales = cur.fetchall()
    return daily_sales


def profit_per_day():
    cur.execute("""
        select date(sales.created_at) as date, sum(sales.quantity *( products.selling_price -
        products.buying_price)) as total_sales from sales join products on products.id = sales.pid
         group by date;
    
    """)
    daily_profit = cur.fetchall()
    return daily_profit

def sales_per_product():
    cur.execute("""
        select products_name as p_name, sum(sales.quantity * products.selling_price) as total_sales from products join sales on products.id = sales.pid
         group by p_name;
    
    """)
    daily_profit = cur.fetchall()
    return daily_profit

def profit_per_product():
    cur.execute("""
        select products_name as p_name, sum(sales.quantity * (products.selling_price-products.buying_price)) as total_sales from sales join products on products.id = sales.pid
         group by p_name;
    
    """)
    daily_profit = cur.fetchall()
    return daily_profit

def check_available_stock(pid):
    cur.execute("select sum(stock.stockquantity) from stock where pid=%s",(pid,))
    total_stock=cur.fetchone()[0] or 0

    cur.execute("select sum(sales.quantity) from sales where pid=%s",(pid,))
    total_sold=cur.fetchone()[0] or 0

    return total_stock-total_sold

# class Horse:
# identity:Horse
# state:black,british
# behaviour:runs,walks,eats,sleeps

# class Car:
# identity:Car
# state:color-grey,type-toyota-hilux
# behaviour:transports

# class Student:
# identity:Student
# state:bright,obedient
# behaviour:runs,walks,eats,sleeps
