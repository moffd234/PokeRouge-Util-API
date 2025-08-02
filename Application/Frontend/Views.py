from flask import Blueprint, render_template

views_bp: Blueprint = Blueprint('views_bp', __name__)

@views_bp.route("/", methods=['GET'])
def index():
    render_template("index.html")