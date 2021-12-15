from flask import render_template, url_for, request, redirect
from blog import app, db
from blog.models import User, Post
from blog.forms import RegistrationForm, LoginForm
from flask_login import login_user, logout_user

@app.route("/")

@app.route("/home")
def home():
  posts=Post.query.all()
  return render_template('home.html',posts=posts)

@app.route("/about")
def about():
  return render_template('about.html', title='About')

@app.route("/post/<int:post_id>")
def post(post_id):
  post=Post.query.get_or_404(post_id)
  return render_template('post.html',title=post.title,post=post)

@app.route("/register",methods=['GET','POST'])
def register():
  form = RegistrationForm()
  if request.method == 'POST':
    user = User(username=form.username.data, password=form.password.data)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('registered'))
  return render_template('register.html',title='Register',form=form)

@app.route("/registered")
def registered():
  return render_template('registered.html', title='Thanks!')

@app.route("/login",methods=['GET','POST'])
def login():
  form = LoginForm()
  if request.method == 'POST':
    user = User.query.filter_by(username=form.username.data).first()
    login_user(user)
    return redirect(url_for('home'))
  return render_template('login.html',title='Login',form=form)

@app.route("/logout")
def logout():
  logout_user()
  return redirect(url_for('home'))
