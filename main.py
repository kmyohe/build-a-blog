from flask import Flask, request, redirect, render_template, session
from flask_sqlalchemy import SQLAlchemy
from validate_blog import login

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:help@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
app.secret_key = 'doeubg0938yrobvso80fdpqi03ir03nlffbyvu'

# app.secret_key = 'any string you want, make it weird' 
# (protects session from outside influence)

class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    blog_name = db.Column(db.String(30))
    blog = db.Column(db.String(1000))
    author = db.Column(db.String(30))
    delete = db.Column(db.Boolean)

    def __init__(self, blog_name, blog, author):
        self.blog_name = blog_name
        self.blog = blog
        self.author = author
        self.delete = False


@app.route('/', methods=['POST', 'GET'])
def index():

    blog = Blog.query.all()
    return render_template('blog.html',title="Build A Blog", 
        blog=blog)

@app.route('/new_blog', methods=['POST', 'GET'])
def new_blog():

    form = render_template('new_blog.html')
    my_blog = Blog.query.all()
    if request.method == 'POST':
            
        blog_name = request.form['blog_name']
        author = request.form['author']
        blog = request.form['blog']

        form = render_template('new_blog.html')
        
        verify = login(blog_name, author, blog)
        if verify == 2:

            new_blog = Blog(blog_name, blog, author)
            db.session.add(new_blog)
            db.session.commit()
            return(redirect('/'))
        
        return(verify)

    return form.format('', '', '')

@app.route('/full_blog', methods=['POST', 'GET'])
def full_blog():
    if request.method == 'GET':

        blog_id = request.args.get('id')

        my_blog = Blog.query.get(blog_id)

        return render_template('full_blog.html', title='Full Blog', my_blog=my_blog)
    else:
        return "<h1>This Link is Broken</h1>"

if __name__ == '__main__':
    app.run()