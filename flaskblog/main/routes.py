"""TODO: Add module docstring"""
from flask import Blueprint, request, render_template
from flaskblog.models import Post

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")  # Multiple URL patterns
def home():
    """TODO: Add method docstring"""
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(
        Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)


@main.route("/about")
def about():
    """TODO: Add method docstring"""
    return render_template('about.html', title="About")
