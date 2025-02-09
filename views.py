import bson.objectid
from flask import Blueprint, render_template, request, redirect
from flask_mail import Message
from . import db, mail

from bson.objectid import ObjectId

logged_in = False
account = ''

views = Blueprint('views', __name__)

@views.route('/')
@views.route('/home')
def index():
    global logged_in, account
    user = db.accounts.find_one({"logged_in": True})
    if user is not None:
        account = user['username']
        logged_in = True
    else:
        logged_in = False
        account = ''

    images = db.home_item.find()
    return render_template('index.html', logged_in=logged_in, account=account, home_item=images)

@views.route('/cart', methods=['GET', 'POST'])
def cart():
    global logged_in, account,total,quantity
        
    user = db.accounts.find_one({"logged_in": True})
    if (user is None):
        return redirect('/login')
    account = user['username']
    logged_in = True
    item_frequency = {}
    user_cart = user['cart']
    cart_items = []
    total = 0
    quantity=0
    
        
    for item in user_cart:
        if item in item_frequency.keys():
            item_frequency[item] += 1
            
        else:
            item_frequency.update({item: 1})
        
        total += db.items.find_one({"_id": bson.ObjectId(item)})['price']
        
    counter = 0
    for item in item_frequency.keys():
        cart_items.append(db.items.find_one({"_id": bson.ObjectId(item)}))
        cart_items[counter].update({"qty": item_frequency[item]})
        counter += 1
        quantity+=item_frequency[item]
            
    if 'form_id' in request.form:
        form_id = request.form
        cart_new = db.accounts.find_one({"_id": user['_id']})['cart']
        cart_new.remove(form_id['form_id'])
        db.accounts.update_one({"_id": user['_id']}, {"$set": {"cart": cart_new}})
        return redirect('/cart')
        
    return render_template('cart.html', logged_in=logged_in, account=account, items=cart_items, total=total)

@views.route('/checkout',methods=['GET','POST'])
def checkout():
    global total,quantity
    user = db.accounts.find_one({"logged_in": True})
    if (user is None):
        return redirect('/login')
    else:
        account = user['username']
        logged_in = True
    if request.method=='POST':
        name=request.form.get('name')
        phone_no=request.form.get('phone')
        address=request.form.get('address')
        country=request.form.get('country')
        account_mail=user['email']
        total = 0
        cart = db.accounts.find_one({"email": account_mail})['cart']
        quantity = len(cart)

        for item in cart:
            total += db.items.find_one({"_id": bson.ObjectId(item)})['price']

        db.order.insert_one(
            {
                "name":name,
                "phone_no. ":phone_no,
                "address":address,
                "country":country,
                "accout":account_mail,
                "total":total,
                "cart": cart
            }
        )
    
    return render_template('checkout.html', logged_in=logged_in, account=account,total=total,quantity=quantity)


@views.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        image_name = request.form.get('image')
        item_type = request.form.get('type')
        item_price = request.form.get('price')
        item_description = request.form.get('discription')
        hover_image = request.form.get('hover_image')
        collection = request.form.get('collection')
        
        db.items.insert_one(
            {
                "type": item_type,
                "image_url": f"../static/assets/{image_name}",
                "price": int(item_price),
                "hover_image": f"../static/assets/{hover_image}",
                "discription": str(item_description),
                "collection" : str(collection)
            }
        )

    return render_template('admin.html')

@views.route('/about')
def about_us():
    return render_template('aboutus.html', logged_in=logged_in, account=account)

@views.route('/contact', methods=['GET', 'POST'])
def contact():
    global logged_in, account
    user = db.accounts.find_one({"logged_in": True})
    if (user is None):
        account = ''
        logged_in = False
    else:
        account = user['username']
        logged_in = True

    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('textarea')

        db.contact.insert_one(
            {
                "name": name,
                "email": email,
                "message": str(message)
            }
        )

        msg = Message("PCJ Agent : Mr Deepak Singh", sender='noreply@gmail.com', recipients=[email])
        msg.body = "thank you for contacting us\n "+"your agent : Mr. deepak Singh\n"+"Email : Deepak-Singh-PCJ@pcj.ac.in\n"+"Mobile no. : 6376720653\n"+"For further more you can vist our nearest showroom\n"+"Once again thank's for contacting us ."
        mail.send(msg)

    return render_template('contact_us.html', logged_in=logged_in, account=account)