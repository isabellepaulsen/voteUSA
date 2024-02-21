
from flask_login import login_required

from src.blueprints.voter import bp
from flask import render_template

@bp.route('/', methods=['GET', 'POST'])
@login_required
def index() -> str:
    message = 'Logged in successfully !'
    return render_template('voter.html', message = message)

