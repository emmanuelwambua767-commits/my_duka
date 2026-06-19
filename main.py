from flask import Flask,render_template,request,redirect,url_for,flash,session
from database import get_products,get_sales,get_stocks,check_available_stock,insert_products2,insert_sales,insert_stock,create_user,check_user_exists,sales_per_day,sales_per_product,profit_per_day,profit_per_product
from flask_bcrypt import Bcrypt
from functools import wraps

# flask instance
app=Flask(__name__)

# bcrypt instance with flask app
bcrypt=Bcrypt(app)

app.secret_key='vghghgfc78656763g'


@app.route('/')
def home():
    name='This is the home page'
    return render_template('index.html',x=name)

def login_required(f):
   @wraps(f)
   def protected (*args,**kwargs):
      if 'email' not in session:
         return redirect(url_for('login'))
      return f(*args,**kwargs)
   return protected

@app.route('/sales')
@login_required
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
@login_required
def products():
    products_data =get_products()
    products=get_products
    return render_template('products.html',products_data=products_data,products=products)

@app.route('/add_products',methods=['GET','POST'])
def add_products():
    if request.method =='POST':
     product_name=request.form['p_name']
     buying_price=request.form['b_price']
     selling_price=request.form['s_price']

    new_product=(product_name,buying_price,selling_price)
    insert_products2(new_product)
    flash('product added successfully',"success")
    return redirect(url_for('products'))

@app.route('/stock')
@login_required
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



@app.route('/login',methods=['GET','POST'])
def login():
    if request.method =='POST':
       email=request.form['email']
       password=request.form['password']

       registered_user=check_user_exists(email)
       if not registered_user:
          flash("User doesn't exist,please register",'danger')
       else:
          if bcrypt.check_password_hash(registered_user[-1],password):
             session['email']=email
             flash("Login successfully",'success')
             return redirect(url_for('dashboard'))
          else:
             flash("Incorrect password,please try again",'danger')
             return redirect(url_for('login'))
          
    return render_template('login.html')

@app.route('/register',methods=['GET','POST'])
def register():
     if request.method =='POST':
      full_name=request.form['full_name']
      email=request.form['email']
      phone_number=request.form['phone']
      password=request.form['password']

      existing_user=check_user_exists(email)
      if not existing_user:
        hashed_password=bcrypt.generate_password_hash(password).decode('utf-8')
        new_user=(full_name,email,phone_number,hashed_password)
        create_user(new_user)
        flash("User created successfully",'success')
        return redirect(url_for('login'))
      else:
        flash("User already exists,please login instead",'danger')

     return render_template('register.html')


@app.route('/dashboard')
@login_required
def dashboard():
    product_sales=sales_per_product()
    product_profit=profit_per_product()

    daily_sales=sales_per_day()
    daily_profit=profit_per_day()

    p_name=[ y[0] for y in product_sales ]
    prod_profit=[ float(y[1]) for y in product_profit ]
    prod_sales=[ float(y[1]) for y in product_sales ]

    dates=[ str(z[0]) for z in daily_sales]
    day_sales=[ float(z[1]) for z in daily_sales]
    day_profit=[ float(z[1]) for z in daily_profit]


    return render_template('dashboard.html',product_names=p_name,prod_profit=prod_profit,prod_sales=prod_sales,dates=dates,day_sales=day_sales,day_profit=day_profit)

@app.route('/logout')
def logout():
   session.pop('email',None)
   flash("Logged out successfully",'success')
   return redirect(url_for('login'))


app.run(debug=True)