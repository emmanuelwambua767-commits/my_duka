from flask import Flask,render_template,request,redirect,url_for
from database import get_products,get_sales,get_stocks,check_available_stock,insert_products2,insert_sales,insert_stock
app=Flask(__name__)

@app.route('/')
def home():
    name='This is the home page'
    return render_template('index.html',x=name)

@app.route('/sales')
def sales():
    sales_data=get_sales()
    products=get_products()
    return render_template('sales.html',sales_data=sales_data,products=products) 

@app.route('/add_sales',methods=['GET','POST'])
def add_sales():
    if request.method =='POST':
     products_ID=request.form['products_id']
     Quantity=request.form['quantity']

    new_sales=(products_ID,Quantity)
    available_stock=check_available_stock()
    if available_stock<Quantity:
       print("Insufficient stock,add more")
    insert_sales(new_sales)
    print('sales added successfully')
    return redirect(url_for('sales'))


@app.route('/products')
def products():
    products_data =get_products()
    return render_template('products.html',products_data=products_data)

@app.route('/add_products',methods=['GET','POST'])
def add_products():
    if request.method =='POST':
     product_name=request.form['p_name']
     buying_price=request.form['b_price']
     selling_price=request.form['s_price']

    new_product=(product_name,buying_price,selling_price)
    insert_products2(new_product)
    print('product added successfully')
    return redirect(url_for('products'))

@app.route('/stock')
def stock():
    stock_data =get_stocks()
    products=get_products()
    return render_template('stock.html',stock_data=stock_data,products=products)

@app.route('/add_stock',methods=['GET','POST'])
def add_stock():
    if request.method =='POST':
     products_id=request.form['products_id']
     quantity=request.form['quantity']

    new_stock=(products_id,quantity)
    insert_stock(new_stock)
    print('stock added successfully')
    return redirect(url_for('stock'))



@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')



app.run(debug=True)