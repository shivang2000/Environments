from flask import Flask, render_template, url_for, flash, redirect
from forms import Registration_Form, Login_Form

app = Flask(__name__)

app.config['SECRET_KEY'] = '475ae18c3cfb6879aa3c24127582a9c5'
posts = [
    {
        'author': 'corey schafer',
        'title': 'blog post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'jane doe',
        'title': 'blog post 2',
        'content': 'second post content',
        'date_posted': 'April 21, 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',title='About' )

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = Registration_Form()
    if form.validate_on_submit():
        flash(u'Account created for {form.username.data}', category='error')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form = Login_Form()
    return render_template('Login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)
