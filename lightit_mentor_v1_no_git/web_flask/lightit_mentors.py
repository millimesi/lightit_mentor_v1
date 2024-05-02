#!/usr/bin/python3
from flask import Flask, render_template, url_for, flash, redirect, get_flashed_messages, request
from forms import RegistrationForm, LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] = 'a81ec48251ca802dd70d96da14b419e6'

mentorslist = [
    {
        'name': 'Million',
        'father_name': 'Meseret',
        'grand_father_name': 'Yirdaw',
        'Bio': 'I am a passionate educator with a Master\'s degree and a track record of academic excellence. With a dedication to fostering a dynamic learning environment, I bring 3 years of experience in guiding students towards success. As a mentor, my goal is to inspire and empower students to reach their full potential, equipping them with the knowledge and skills needed to excel. Let\'s embark on this journey of learning together!',
        'experience': '3 years university lecturing',
        'photo': 'none',
        'email': 'millionmesi1@gmail.com',
        'phone_number': '0910120891',
        'password': 'Million1234!',
    },
     {
        'name': 'Betelihem',
        'father_name': 'Meseret',
        'grand_father_name': 'Yirdaw',
        'Bio': 'I am a passionate tutor with 3 years of experience in guiding students towards success. As a mentor, my goal is to inspire and empower students to reach their full potential, equipping them with the knowledge and skills needed to excel!',
        'experience': '2 years tutoring',
        'photo': 'none',
        'email': 'millionmesi1@gmail.com',
        'phone_number': '0910120891',
        'password': 'Million1234!',
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/mentors")
def mentors():
    return render_template('mentors.html', mentorslist=mentorslist, title='mentors')

@app.route("/about")
def about():
    return render_template('about.html', title='about')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST':
        if form.validate():
            # user = User(form.username.data, form.email.data,
            #             form.password.data)
            # db_session.add(user)
            flash(f"User Account Created for {form.name.data} successfully!", 'success')
            return redirect(url_for('mentors'))
        else:
            return ("<h1>Validation Failed<h1>")
    return render_template('register.html', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate():
            if form.email.data == 'millionmesi1@gmail.com' and form.password.data == '1234':
                flash(f"Login successfully!", 'success')
                return redirect(url_for('mentors'))
            else: 
                flash(f"Login unsuccessfully! Please check Password and Email", 'failed')
        else:
            return ("<h1>Validation Failed<h1>")
    return render_template('login.html', title='register', form=form)

if __name__ == "__main__":
    app.run(debug=True)

 