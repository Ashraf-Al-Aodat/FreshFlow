'''
    This file is used to run the development server for your application.
'''

from flask import Flask
from .views import get_orders
from .models import create_tables

app = Flask(__name__)

@app.route('/orders', methods=['GET'])
def get_orders():
    return get_orders()

if __name__ == '__main__':
    create_tables()
    app.run(debug=True, host='0.0.0.0')
