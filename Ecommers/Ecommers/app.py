from flask import Flask, render_template,request,redirect,url_for
import sqlite3
con = sqlite3.connect("data.db")
cr = con.cursor()

app=Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/jewellery')
def jewellery():
    return render_template('jewellery.html')

@app.route('/fashion')
def fashion():
    return render_template('fashion.html')

@app.route('/electronic')
def electronic():
    return render_template('electronic.html')

@app.route('/t_shirt')
def t_shirt():
        con = sqlite3.connect("data.db")
        cr = con.cursor()
        cr.execute("select * from Dress where Dresstype ='T_Shirt' ")
        value =cr.fetchall()
        print(value)
        headings=['Dresstype','gender','price','brand','clothtype']
        return render_template('items.html', result=value, title="T-Shirts",tbl="Dress", headings=headings)
    
@app.route('/shirt')
def shirt():
        con = sqlite3.connect("data.db")
        cr = con.cursor()
        cr.execute("select * from Dress where Dresstype ='Shirt'")
        value =cr.fetchall()
        print(value)
        headings=['Dresstype','gender','price','brand','clothtype']
        return render_template('items.html', result=value, title="Shirt",tbl="Dress",headings=headings)

@app.route('/scart')
def scart():
        con = sqlite3.connect("data.db")
        cr = con.cursor()
        cr.execute("select * from Dress where Dresstype ='Scart'")
        value =cr.fetchall()
        print(value)
        headings=['Dresstype','gender','price','brand','clothtype']
        return render_template('items.html', result=value, title="Scart",tbl="Dress", headings=headings)
    
@app.route('/lap')
def lap():
        con = sqlite3.connect("data.db")
        cr = con.cursor()
        cr.execute("select * from Electronic where type ='Laptop'")
        value =cr.fetchall()
        print(value)
        headings=['type', 'price', 'storage', 'brand']
        return render_template('items.html', result=value,title="laptops", tbl="Electronic", headings=headings)

@app.route('/mob')
def mob():
        con = sqlite3.connect("data.db")
        cr = con.cursor()
        cr.execute("select * from Electronic where type ='mobile'")
        value =cr.fetchall()
        print(value)
        headings=['type', 'price', 'storage', 'brand']
        return render_template('items.html', result=value,title="moblie", tbl="Electronic", headings=headings)
    
@app.route('/com')
def com():
        con = sqlite3.connect("data.db")
        cr = con.cursor()
        cr.execute("select * from Electronic where type ='computers'")
        value =cr.fetchall()
        print(value)
        headings=['type', 'price', 'storage', 'brand']
        return render_template('items.html', result=value,title="computers", tbl="Electronic", headings=headings)

@app.route('/Jumkas')
def Jumkas():
        con = sqlite3.connect("data.db")
        cr = con.cursor()
        cr.execute("select * from Jewellery where type ='Jumkas'")
        value =cr.fetchall()
        print(value)
        headings = ['Type', 'Brand', 'Price']
        return render_template('items.html', result=value,title="jumkas", tbl="Jewellery",  headings=headings)

@app.route('/Necklaces')
def Necklaces():
        con = sqlite3.connect("data.db")
        cr = con.cursor()
        cr.execute("select * from Jewellery where type ='Necklaces'")
        value =cr.fetchall()
        print(value)
        headings = ['Type', 'Brand', 'Price']
        return render_template('items.html', result=value,title="Necklaces", tbl="Jewellery", headings=headings)

@app.route('/Kangans')
def Kangans():
        con = sqlite3.connect("data.db")
        cr = con.cursor()
        cr.execute("select * from Jewellery where type ='Kangans'")
        value =cr.fetchall()
        print(value)
        headings = ['Type', 'Brand', 'Price']
        return render_template('items.html', result=value,title="Banglas", tbl="Jewellery", headings=headings)

@app.route('/electronic_cart/<ID>')
def electronic_cart(ID):
        print(ID)
        con = sqlite3.connect("data.db")
        cr = con.cursor()
        cr.execute("select brand, price, photo from electronic where id = '"+ID+"'")
        result = cr.fetchone()
        print(result)
        
        brand = result[0]
        price = result[1]
        photo=result[2]
        f = open('session.txt', 'r')
        data = f.read()
        f.close()
        data=data.split(',')
        gmail=data[0]
        phone=data[1]
        List = [gmail, brand, price, photo, phone]
        print(List)
        cr.execute("insert into Cart ( gmail, brand, price, photo, phone) values(?,?,?,?,?)", List)
        con.commit()
        return render_template('electronic.html')

@app.route('/jewellery_cart/<ID>')
def jewellery_cart(ID):
        print(ID)
        con = sqlite3.connect("data.db")
        cr = con.cursor()
        cr.execute("select brand, price, photo from jewellery where id = '"+ID+"'")
        result = cr.fetchone()
        print(result)
        f = open('session.txt', 'r')
        data = f.read()
        f.close()
        data=data.split(',')
        brand = result[0]
        price = result[1]
        photo=result[2]
        gmail=data[0]
        phone=data[1]
        List = [gmail, brand, price, photo, phone]
        print(List)
        con = sqlite3.connect("data.db")
        cr = con.cursor()
        cr.execute("insert into Cart ( gmail, brand, price, photo, phone) values(?,?,?,?,?)", List)
        con.commit()
        return render_template('jewellery.html')

@app.route('/Sign_Up',methods=['POST','GET'])
def Sign_Up():
    if request.method =='POST':
        name = request.form['name']
        email = request.form['email']
        phoneno = request.form['phoneno']
        Address = request.form['Address']
        password =request.form['password']
        con = sqlite3.connect("data.db")
        cr = con.cursor()
        print(name,email,phoneno,Address,password)
        List = [name,email,phoneno,Address,password]
        print(List)
        con = sqlite3.connect("data.db")
        cr = con.cursor()
        cr.execute("insert into sign ( name, email, phoneno, Address, password) values(?,?,?,?,?)", List)
        con.commit()
        return render_template('home.html')
    return render_template('home.html')

@app.route('/Sign_in',methods=['POST','GET'])
def Sign_in():
    if request.method =='POST':
        email = request.form['email']
        password = request.form['password']
        con = sqlite3.connect("data.db")
        cr = con.cursor()
        print("email,password")
        cr.execute("select * from sign where email = '"+email+"' and password = '"+password+"'")
        result = cr.fetchone()
        if result:
                f = open('session.txt', 'w')
                f.write(result[2]+','+str(result[3]))
                f.close()
                return render_template('index.html', )
        else:
            return render_template('home.html', msg="entered wrong username or password")
    return render_template('index.html')


@app.route('/dress_cart/<ID>')
def dress_cart(ID):
        print(ID)
        con = sqlite3.connect("data.db")
        cr = con.cursor()
        cr.execute("select brand, price, photo from dress where id = '"+ID+"'")
        result = cr.fetchone()
        print(result)
        f = open('session.txt', 'r')
        data = f.read()
        f.close()
        data=data.split(',')
        brand = result[0]
        price = result[1]
        photo=result[2]
        gmail=data[0]
        phone=data[1]
        List = [gmail, brand, price, photo, phone]
        print(List)
        con = sqlite3.connect("data.db")
        cr = con.cursor()
        cr.execute("insert into Cart ( gmail, brand, price, photo, phone) values(?,?,?,?,?)", List)
        con.commit()
        return render_template('fashion.html')

@app.route('/cart')
def cart():
      con = sqlite3.connect("data.db")
      cr = con.cursor()
      f = open('session.txt', 'r')
      data = f.read()
      f.close()
      data=data.split(',')
      gmail=data[0]
      cr.execute("select price, brand, photo from cart where gmail = '"+gmail+"'")
      result = cr.fetchall()
      print(result)
      items = 0
      amount = 0
      for row in result:
            items += 1
            amt = row[0][1:]
            print(amt)
            amount += int(amt)
      return render_template('cart.html', result=result, items=items, amount=amount)

if __name__ == "__main__":
    app.run(debug=True)
