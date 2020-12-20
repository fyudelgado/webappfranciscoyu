from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, flash
from sqlite3 import OperationalError

app = Flask(__name__)
app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
USERS_PER_PAGE = 25

@app.route('/users')
@app.route('/users/<int:page>')
def all_users(page = 1):
    from models import User
    headers = User.get_headers()
    try:
        page_size = int(request.args.get('page_size')) if request.args.get('page_size') is not None else USERS_PER_PAGE
        ordering = request.args.get('ordering') if request.args.get('ordering') is not  None else 'asc'
        if ordering == 'asc':
            users_list = User.query.order_by(
                User.id.asc()
            ).paginate(page, per_page=page_size)
        else:
            users_list = User.query.order_by(
                User.id.desc()
            ).paginate(page, per_page=page_size)

    except OperationalError:
        flash("No users in the database")
        user_list = None

    return render_template('template.html', my_string="GitHub Users!", users_list=users_list, title="GitHub Users", headers=headers, page_size=page_size, ordering=ordering )

if __name__ == ('__main__'):
    app.run(debug=True)
