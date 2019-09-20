from flask import Blueprint, render_template

sgm = Blueprint('sgm', __name__, template_folder='templates')


@sgm.route('/')
def index():
    return render_template('index.html')


@sgm.route('/about')
def about():
    return render_template('about.html')


@sgm.route('/sermons')
def sermons():
    return render_template('sermons.html')


@sgm.route('/blog')
def blog():
    return render_template('blog.html')


@sgm.route('/contact')
def contact():
    return render_template('contact.html')


@sgm.route('/events')
def events():
    return render_template('events.html')
