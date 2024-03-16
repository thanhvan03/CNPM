from flask import Flask, render_template, request
import dao

app = Flask(__name__)
@app.route('/')
def index():
    q = request.args.get('q')
    cate_id = request.args.get('category_id')


    categories = dao.load_categories()
    products = dao.load_products(q, cate_id)
    return render_template('index.html', products=products)

@app.context_processor
def common_attributes():
    return{
        'categories': dao.load_categories()
    }

@app.route('/login', methods=['get', 'post'])
def login_my_user():
    return render_template('login.html')

if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)
