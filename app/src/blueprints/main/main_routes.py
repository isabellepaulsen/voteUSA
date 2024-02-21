import bcrypt
from src.blueprints.main import bp
from flask import render_template, redirect, url_for, request, session

import src.blueprints.main.main_model as main_model
import src.blueprints.main.main_forms as main_forms
from flask_login import LoginManager, UserMixin, login_required
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user

@bp.route('/')
def index() -> str:
    return render_template('main.html', message = 'MainPage')


# Inspired from https://realpython.com/introduction-to-flask-part-2-creating-a-login-page/
@bp.route('/login', methods=['GET', 'POST'])
def login():
    error = ''
    form = main_forms.LoginForm()
    email = form.email.data
    password = form.password.data
    if form.validate_on_submit():
        user = main_model.get_user_auth(email)
        if user and user['password'].encode('utf-8') == main_model.hash_password(password,user['salt']):
            users = main_model.User(user['email'])
            users.id = user['email']
            login_user(users)
            if (user['role'] == 'Manager'):
                return redirect(url_for('manager_bp.index'))
            elif (user['role'] == 'Voter'):
                return redirect(url_for('voter_bp.index'))
            elif (user['role'] == 'Admin'):
                return redirect(url_for('admin_bp.index'))
            else:
                logout_user()
                error = 'Invalid account role. Please contact an Administrator if you believe this is in error'
                return render_template('login.html', form = form, error = error)
        else:
            error = 'Invalid user'
    return render_template('login.html', form = form, error = error)

@bp.route('/new', methods = ['GET', 'POST'])
def new() -> str:
    error = " "
    form = main_forms.NewVoterForm()
    if form.validate_on_submit():
        #user = main_model.get_user_auth(form.data)
        password = form.password.data
        passwordConfirm = form.passwordConfirm.data
        if password == passwordConfirm and form.age.data >= 18:
            main_model.insert_user(form.name1.data, form.name2.data, form.name3.data, form.age.data, form.address1.data, form.address2.data, form.city.data, form.state.data, form.zip.data, form.ID1.data, form.ID2.data, form.email.data, form.password.data, 'Voter')
            return redirect(url_for('main_bp.login'))
        elif form.age.data < 18:
            error = "Must be 18 to vote."
        else:
            error = "Passwords must match."
    return render_template('profilerequest.html', form=form, error=error)

@bp.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return render_template('main.html', message = 'MainPage')
    



