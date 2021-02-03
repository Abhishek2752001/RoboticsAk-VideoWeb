from flask import Flask,render_template,request,redirect,session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from datetime import datetime
import os
import math
from flask_mail import Mail
import json

with open('config.json', 'r') as c:
    params = json.load(c)["params"]
local_server = True


app=Flask(__name__)
app.secret_key = 'super-secret-key'
app.config['UPLOAD_FOLDER'] = params['upload_location']

app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = params['gmail-user'],
    MAIL_PASSWORD=  params['gmail-password']
)

mail = Mail(app)

if(local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']
db = SQLAlchemy(app)


class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    phone_num = db.Column(db.String(12), nullable=False)
    subject = db.Column(db.String(12), nullable=False)
    msg = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)

class Posts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    slug = db.Column(db.String(21), nullable=False)
    content = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=False)
    video_file=db.Column(db.String(12), nullable=False)
    fronted_img=db.Column(db.String(12), nullable=False)


class Suscribes(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(20), nullable=False)
    date = db.Column(db.String(12), nullable=True)

@app.route('/')
def home():
    videos = Posts.query.filter_by().all()
    last = math.ceil(len(videos) / int(params['no_of_videos']))
    page = request.args.get('page')
    if (not str(page).isnumeric()):
        page = 1
    page = int(page)
    videos = videos[(page - 1) * int(params['no_of_videos']): (page - 1) * int(params['no_of_videos']) + int(
        params['no_of_videos'])]
    # Pagination Logic
    # First
    if (page == 1):
        prev = "#"
        next = "/?page=" + str(page + 1)
    elif (page == last):
        prev = "/?page=" + str(page - 1)
        next = "#"
    else:
        prev = "/?page=" + str(page - 1)
        next = "/?page=" + str(page + 1)

    return render_template('index.html', params=params, videos=videos, prev=prev, next=next)

@app.route('/about')
def about():
    return render_template('about.html',params=params)

@app.route("/dashboard",methods=['GET', 'POST'])
def dashboard():
    if 'user' in session and session['user']==params['admin_user']:
        videos = Posts.query.all()
        return render_template('dashboard.html',params=params,videos=videos )

    if request.method=='POST':
       ''' Rdirect to panal'''
       username=request.form.get('uname')
       userpass=request.form.get('pass')
       if username == params['admin_user'] and userpass == params['admin_password']:
          '''set the section variable'''
          session['user'] = username
          videos=Posts.query.all()
          return render_template('dashboard.html', params=params,videos=videos)
       else:
           print('password was wrong')
           return redirect('/dashboard')


    else:
     return render_template('login.html', params=params)


@app.route("/edit/<string:sno>", methods=['GET', 'POST'])
def edit(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        if request.method == 'POST':
            title = request.form.get('title')
            slug = request.form.get('slug')
            content = request.form.get('content')
            video_file = request.form.get('video_file')
            fronted_img = request.form.get('fronted_img')
            date = datetime.now()

            if sno == '0':
                video = Posts(title=title, slug=slug, content=content,video_file=video_file,fronted_img=fronted_img,date=date)
                db.session.add(video)
                db.session.commit()

            else:
                video = Posts.query.filter_by(sno=sno).first()
                video.title = title
                video.slug = slug
                video.content = content # update karne keliye
                video.video_file = video_file
                video.fronted_img = fronted_img
                video.date = date
                db.session.commit()
                return redirect('/dashboard')

        video= Posts.query.filter_by(sno=sno).first()
        return render_template('edit.html', params=params,sno=sno,video=video)

@app.route("/uploader", methods = ['GET', 'POST'])
def uploader():
    if ('user' in session and session['user'] == params['admin_user']):
        if (request.method == 'POST'):
            f= request.files['file']
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename) ))
            return "Uploaded successfully"



@app.route("/logout")
def logout():
    session.pop('user')
    return redirect('/dashboard')


@app.route("/rough")
def rough():
    return render_template("rough.html")

@app.route("/delete/<string:sno>", methods = ['GET', 'POST'])
def delete(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        video = Posts.query.filter_by(sno=sno).first()
        db.session.delete(video)
        db.session.commit()
    return redirect('/dashboard')

@app.route("/video/<string:video_slug>",methods=['GET'])
def video_route(video_slug):
    videos = Posts.query.filter_by().all()
    video=Posts.query.filter_by(slug=video_slug).first()
    return render_template('video-page.html', params=params ,video=video)

@app.route("/contact", methods = ['GET', 'POST'])
def contact():
    if (request.method == 'POST'):
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        subject = request.form.get('subject')
        message = request.form.get('message')
        entry = Contacts(name=name,email=email, phone_num=phone,subject=subject, msg=message, date=datetime.now())
        db.session.add(entry)
        db.session.commit()
        mail.send_message('New message from ' + name,
                          sender=email,
                          recipients=[params['gmail-user']],
                          body=message + "\nphone number is :- " + phone +"subject is:-" +subject
                          )

    return render_template('contact.html',params=params)

@app.route("/suscribe", methods = ['GET', 'POST'])
def suscribe():
    if (request.method == 'POST'):
        email = request.form.get('email')
        entry = Suscribes(email=email, date=datetime.now())
        db.session.add(entry)
        db.session.commit()
        return render_template("suscribe.html",params=params)

    return render_template('index.html',params=params)

app.run(debug=True)

