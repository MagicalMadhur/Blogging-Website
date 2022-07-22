from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/tech_with_madhur'
db = SQLAlchemy(app)



class video(db.Model):
    
    # sno, thumbnail ,slug ,title
    
    sno = db.Column(db.Integer, primary_key=True)
    
    slug = db.Column(db.String(12), nullable=False)
    title = db.Column(db.String(120), nullable=False)
  










@app.route("/")
def home():
    return render_template('index.html')

@app.route("/videos")
def videos():
    return render_template('video.html')
    
@app.route("/blog_post")
def blog():
    return render_template('blog.html')


@app.route("/about_us")
def About():
    return render_template('about.html')

@app.route("/contact_us")
def contact():
    return render_template('contact.html')

@app.route("/videos/fixing")
def fixvideo():
    return render_template('fixing.html')  



@app.route("/videos/tech_education")
def tech_education():
    return render_template('techedu.html')  

@app.route("/videos/money_earning")
def money_earning():
    return render_template('money.html')  

@app.route("/videos/tips_n_tricks")
def tips_n_tricks():
    return render_template('tips.html')  


# tempory page for disigen
@app.route("/vid")
def videop():
    return render_template('videopage.html')  

# temp form fetching
@app.route("/f", methods = ['GET', 'POST'])
def vi():
    if(request.method=='POST'):
        # Add entry to the database
        number = request.form.get('num')
        title = request.form.get('title')
        slug = request.form.get('slug')
        entry = video(sno = number, title = title, slug = slug )
        db.session.add(entry)
        db.session.commit()

    return render_template('form.html')  

 

app.run(debug=True)


