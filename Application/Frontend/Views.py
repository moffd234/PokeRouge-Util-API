from datetime import datetime

from flask import Blueprint, render_template

views_bp: Blueprint = Blueprint('views_bp', __name__)


@views_bp.app_context_processor
def inject_current_year():
    return {'year': datetime.now().year}


@views_bp.route("/", methods=['GET'])
def index():
    return render_template("index.html")

@views_bp.route("/weaknesses", methods=['GET'])
def weaknesses():
    return render_template("weaknesses.html")