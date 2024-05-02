!/usr/bin/python3
from flask import Flask, render_template, url_for, flash, redirect, get_flashed_messages, request
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from forms import RegistrationForm
app = Flask(__name__)
app.config['SECRET_KEY'] = 'a81ec48251ca802dd70d96da14b419e6'

@app.route("/")
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST':
        if form.validate():
            # user = User(form.username.data, form.email.data,
            #             form.password.data)
            # db_session.add(user)
            flash(f"User Account Created for {form.name.data} successfully!", 'success')
            return redirect(url_for('login'))
        else:
            return ("<h1>Validation Failed<h1>")
    return render_template('register.html', form=form)

@app.route("/login")
def login():
    # form = LoginForm()
    return render_template('login.html', title='register')

if __name__ == "__main__":
    app.run(debug=True)