import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        product = request.form['product']
        price = request.form['price']
        db = get_db()
        error = None

        if not product:
            error = 'Product name is required.'
        elif not price:
            error = 'Price is required.'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO products (product, price) VALUES (?, ?)",
                    (product, price),
                )
                db.commit()
            except db.IntegrityError:
                error = f"Product {product} already exists."

        flash(error)

    return render_template('pc/createproduct.html')


@bp.route('/search', methods=('GET', 'POST'))
def search():
    if request.method == 'POST':
        product = request.form['product']
        db = get_db()
        error = None
        products = db.execute(
            'SELECT * FROM products WHERE product = ?', (product,)
        ).fetchall()

        if products is None:
            flash('No results found!')
            return render_template('pc/search.html')
        else:
            return render_template('pc/search.html', products=products)

    return render_template('pc/search.html')
