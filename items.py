from flask import Blueprint, render_template, redirect, request
from . import db

logged_in = False
account = ''

items = Blueprint('items', __name__)

@items.route('/necklaces', methods=['GET', 'POST'])
def necklace():
    global logged_in, account
    user = db.accounts.find_one({"logged_in": True})
    if (user is None):
        account = ''
        logged_in = False
    else:
        account = user['username']
        logged_in = True
    necklaces = db.items.find({"type": "necklace"})

    if request.method == 'POST':
        if 'asec' in request.form:
            necklaces.sort('price', 1)
        elif 'desc' in request.form:
            necklaces.sort('price', -1)
        elif 'form_id' in request.form:
            form_id = request.form
            user = db.accounts.find_one({'logged_in': True})
            if (user is None):
                return redirect('/login')
            else:
                db.accounts.update_one({'_id': user['_id']}, {'$push': {'cart': form_id['form_id']}})
    return render_template('items.html', items=necklaces, logged_in=logged_in, account=account, item_name="necklace")

@items.route('/rings', methods=['GET', 'POST'])
def rings():
    global logged_in, account
    user = db.accounts.find_one({"logged_in": True})
    if (user is None):
        account = ''
        logged_in = False
    else:
        account = user['username']
        logged_in = True

    rings = db.items.find({"type": "ring"})
    if request.method == 'POST':
        if 'asec' in request.form:
            rings.sort('price', 1)
        elif 'desc' in request.form:
            rings.sort('price', -1)
        elif 'form_id' in request.form:
            form_id = request.form
            user = db.accounts.find_one({'logged_in': True})
            if (user is None):
                return redirect('/login')
            else:
                db.accounts.update_one({'_id': user['_id']}, {'$push': {'cart': form_id['form_id']}})
    return render_template('items.html', items=rings, logged_in=logged_in, account=account, item_name="rings")

@items.route('/ear-rings', methods=['GET', 'POST'])
def ear_rings():
    global logged_in, account
    user = db.accounts.find_one({"logged_in": True})
    if (user is None):
        account = ''
        logged_in = False
    else:
        account = user['username']
        logged_in = True

    ear_rings = db.items.find({"type": "ear_rings"})
    if request.method == 'POST':
        if 'asec' in request.form:
            ear_rings.sort('price', 1)
        elif 'desc' in request.form:
            ear_rings.sort('price', -1)
        elif 'form_id' in request.form:
            form_id = request.form
            user = db.accounts.find_one({'logged_in': True})
            if (user is None):
                return redirect('/login')
            else:
                db.accounts.update_one({'_id': user['_id']}, {'$push': {'cart': form_id['form_id']}})
    return render_template('items.html', items=ear_rings, logged_in=logged_in, account=account, item_name="ear rings")

@items.route('/bracelates', methods=['GET', 'POST'])
def bracelates():
    global logged_in, account
    user = db.accounts.find_one({"logged_in": True})
    if (user is None):
        account = ''
        logged_in = False
    else:
        account = user['username']
        logged_in = True

    bracelates = db.items.find({"type": "bracelates"})
    if request.method == 'POST':
        if 'asec' in request.form:
            bracelates.sort('price', 1)
        elif 'desc' in request.form:
            bracelates.sort('price', -1)
        elif 'form_id' in request.form:
            form_id = request.form
            user = db.accounts.find_one({'logged_in': True})
            if (user is None):
                return redirect('/login')
            else:
                db.accounts.update_one({'_id': user['_id']}, {'$push': {'cart': form_id['form_id']}})
    return render_template('items.html', items=bracelates, logged_in=logged_in, account=account, item_name="bracelates")

@items.route('/products', methods=['GET', 'POST'])
def products():
    global logged_in, account
    user = db.accounts.find_one({"logged_in": True})
    if (user is None):
        account = ''
        logged_in = False
    else:
        account = user['username']
        logged_in = True

    bracelates = db.items.find({"type": "bracelates"})
    ear_rings = db.items.find({"type": "ear_rings"})
    necklaces = db.items.find({"type": "necklace"})
    rings = db.items.find({"type": "ring"})
    if request.method == 'POST':
        if 'form_id' in request.form:
            form_id = request.form
            user = db.accounts.find_one({'logged_in': True})
            if (user is None):
                return redirect('/login')
            else:
                db.accounts.update_one({'_id': user['_id']}, {'$push': {'cart': form_id['form_id']}})
    return render_template('products.html', items=bracelates, logged_in=logged_in, account=account, rings=rings, ear_rings=ear_rings, bracelates=bracelates, necklaces=necklaces)

@items.route("/plique-A'-jour", methods=['GET', 'POST'])
def plique():
    global logged_in, account
    user = db.accounts.find_one({"logged_in": True})
    if (user is None):
        account = ''
        logged_in = False
    else:
        account = user['username']
        logged_in = True

    collection = db.items.find({"collection": "plique-A'-jour"})
    if request.method == 'POST':
        if 'form_id' in request.form:
            form_id = request.form
            user = db.accounts.find_one({'logged_in': True})
            if (user is None):
                return redirect('/login')
            else:
                db.accounts.update_one({'_id': user['_id']}, {'$push': {'cart': form_id['form_id']}})
    return render_template('collections.html', items=collection, logged_in=logged_in, account=account)

@items.route("/anant", methods=['GET', 'POST'])
def anant():
    global logged_in, account
    user = db.accounts.find_one({"logged_in": True})
    if (user is None):
        account = ''
        logged_in = False
    else:
        account = user['username']
        logged_in = True

    collection = db.items.find({"collection": "anant"})
    if request.method == 'POST':
        if 'form_id' in request.form:
            form_id = request.form
            user = db.accounts.find_one({'logged_in': True})
            if (user is None):
                return redirect('/login')
            else:
                db.accounts.update_one({'_id': user['_id']}, {'$push': {'cart': form_id['form_id']}})
    return render_template('collections.html', items=collection, logged_in=logged_in, account=account)

@items.route("/mirosa", methods=['GET', 'POST'])
def mirosa():
    global logged_in, account
    user = db.accounts.find_one({"logged_in": True})
    if (user is None):
        account = ''
        logged_in = False
    else:
        account = user['username']
        logged_in = True

    collection = db.items.find({"collection": "mirosa"})
    if request.method == 'POST':
        if 'form_id' in request.form:
            form_id = request.form
            user = db.accounts.find_one({'logged_in': True})
            if (user is None):
                return redirect('/login')
            else:
                db.accounts.update_one({'_id': user['_id']}, {'$push': {'cart': form_id['form_id']}})
    return render_template('collections.html', items=collection, logged_in=logged_in, account=account)

@items.route("/initials", methods=['GET', 'POST'])
def initials():
    global logged_in, account
    user = db.accounts.find_one({"logged_in": True})
    if (user is None):
        account = ''
        logged_in = False
    else:
        account = user['username']
        logged_in = True

    collection = db.items.find({"collection": "initials"})
    if request.method == 'POST':
        if 'form_id' in request.form:
            form_id = request.form
            user = db.accounts.find_one({'logged_in': True})
            if (user is None):
                return redirect('/login')
            else:
                db.accounts.update_one({'_id': user['_id']}, {'$push': {'cart': form_id['form_id']}})
    return render_template('collections.html', items=collection, logged_in=logged_in, account=account)

@items.route("/amour", methods=['GET', 'POST'])
def amour():
    global logged_in, account
    user = db.accounts.find_one({"logged_in": True})
    if (user is None):
        account = ''
        logged_in = False
    else:
        account = user['username']
        logged_in = True

    collection = db.items.find({"collection": "amour"})
    if request.method == 'POST':
        if 'form_id' in request.form:
            form_id = request.form
            user = db.accounts.find_one({'logged_in': True})
            if (user is None):
                return redirect('/login')
            else:
                db.accounts.update_one({'_id': user['_id']}, {'$push': {'cart': form_id['form_id']}})
    return render_template('collections.html', items=collection, logged_in=logged_in, account=account)

@items.route("/twinning", methods=['GET', 'POST'])
def twinning():
    global logged_in, account
    user = db.accounts.find_one({"logged_in": True})
    if (user is None):
        account = ''
        logged_in = False
    else:
        account = user['username']
        logged_in = True

    collection = db.items.find({"collection": "twinning"})
    if request.method == 'POST':
        if 'form_id' in request.form:
            form_id = request.form
            user = db.accounts.find_one({'logged_in': True})
            if (user is None):
                return redirect('/login')
            else:
                db.accounts.update_one({'_id': user['_id']}, {'$push': {'cart': form_id['form_id']}})
    return render_template('collections.html', items=collection, logged_in=logged_in, account=account)

@items.route("/inayat", methods=['GET', 'POST'])
def inayat():
    global logged_in, account
    user = db.accounts.find_one({"logged_in": True})
    if (user is None):
        account = ''
        logged_in = False
    else:
        account = user['username']
        logged_in = True

    collection = db.items.find({"collection": "inayat"})
    if request.method == 'POST':
        if 'form_id' in request.form:
            form_id = request.form
            user = db.accounts.find_one({'logged_in': True})
            if (user is None):
                return redirect('/login')
            else:
                db.accounts.update_one({'_id': user['_id']}, {'$push': {'cart': form_id['form_id']}})
    return render_template('collections.html', items=collection, logged_in=logged_in, account=account)

@items.route("/ladanza", methods=['GET', 'POST'])
def ladanza():
    global logged_in, account
    user = db.accounts.find_one({"logged_in": True})
    if (user is None):
        account = ''
        logged_in = False
    else:
        account = user['username']
        logged_in = True

    collection = db.items.find({"collection": "ladanza"})
    if request.method == 'POST':
        if 'form_id' in request.form:
            form_id = request.form
            user = db.accounts.find_one({'logged_in': True})
            if (user is None):
                return redirect('/login')
            else:
                db.accounts.update_one({'_id': user['_id']}, {'$push': {'cart': form_id['form_id']}})
    return render_template('collections.html', items=collection, logged_in=logged_in, account=account)

@items.route("/dashavatar", methods=['GET', 'POST'])
def dashavatar():
    global logged_in, account
    user = db.accounts.find_one({"logged_in": True})
    if (user is None):
        account = ''
        logged_in = False
    else:
        account = user['username']
        logged_in = True

    collection = db.items.find({"collection": "dashavatar"})
    if request.method == 'POST':
        if 'form_id' in request.form:
            form_id = request.form
            user = db.accounts.find_one({'logged_in': True})
            if (user is None):
                return redirect('/login')
            else:
                db.accounts.update_one({'_id': user['_id']}, {'$push': {'cart': form_id['form_id']}})
    return render_template('collections.html', items=collection, logged_in=logged_in, account=account)