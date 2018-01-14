from flask import Blueprint, jsonify, render_template

bp = Blueprint('core', __name__, template_folder='templates')

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/data')
def data():
    return jsonify({'data': 'hello'})
