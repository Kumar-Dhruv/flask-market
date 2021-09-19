# Routes for Flask Market
from market import app, db, forms
from flask import render_template, redirect, url_for, flash, get_flashed_messages
from market.models import Item, User
from market.forms import RegisterForm, LoginForm
from flask_login import login_user

# Route for Home Page and executing the home.html file
@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

# Route for Market Page and executing the market.html file
@app.route('/market')
def market_page():
    items = Item.query.all() # Getting all the Items from db and passing them as arguments to market.html
    return render_template('market.html', items=items)

# Route for Register Page with GET and POST methods and executing the register.html file
@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm() # Instancing the Register Form
    if form.validate_on_submit(): # Validating all the fields with their respective validators
        user_to_create = User(username=form.username.data,
                            email_address=form.email_address.data,
                            password=form.password1.data)
        db.session.add(user_to_create) 
        db.session.commit() # Adding and then Commiting changes
        return redirect(url_for('market_page'))

    if form.errors != {}: # If any errors or form.errors is not an empty dictionary
        for err_msg in form.errors.values():
            print(form.errors)
            # Flash error messages with category to base.html
            flash(f'Error: {err_msg}', category='danger')

    return render_template('register.html', form=form)

# Route for Login Page with GET and POST methods and executing login.html file
@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm() # Instancing the Login Form
    if form.validate_on_submit(): # Validating all the fields with their respective validators
        attempted_user = User.query.filter_by(username=form.username.data).first() # Getting the user by username from db
        if attempted_user and attempted_user.check_password_correction(
            attempted_password=form.password.data): # Comparing Password with the hashed-Password throught bcrypt
            login_user(attempted_user) # Using login manager to login user
            flash(f'You are successfully loggin in as {attempted_user.username}', category='success')
            return redirect(url_for('market_page')) 
        else:
            flash('Username or Password dont match', category='danger')
        # Flashing appropriate messages and redirecting to market page

    return render_template('login.html', form=form)