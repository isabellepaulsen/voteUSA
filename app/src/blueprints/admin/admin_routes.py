
from src.blueprints.admin import bp
from flask_login import login_required
from flask import render_template

@bp.route('/', methods=['GET', 'POST'])
@login_required
def index() -> str:
    message = 'Logged in successfully !'
    return render_template('admin.html', message = message)
