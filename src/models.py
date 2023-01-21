'''
    This file contains the database models.
'''
import sqlite3

def create_tables():
    conn = sqlite3.connect('database.db') # change the name to ":memory:" if you want a in memory db :)

    cursor = conn.cursor()

    # create a inventory table 
    cursor.execute('''CREATE TABLE inventory (
                        item_number INTEGER PRIMARY KEY,
                        day DATE NOT NULL,
                        inventory INTEGER NOT NULL
                    )''')

    # create a order_intake table
    cursor.execute('''CREATE TABLE order_intake (
                        item_number INTEGER PRIMARY KEY,
                        day DATE NOT NULL,
                        purchase_price REAL NOT NULL,
                        quantity INTEGER NOT NULL,
                        unit TEXT NOT NULL
                    )''')

    # create a sales_predictions table
    cursor.execute('''CREATE TABLE sales_predictions (
                        item_number INTEGER PRIMARY KEY,
                        day DATE NOT NULL,
                        sales_quantity INTEGER NOT NULL
                    )''')

    # create a orderable_items table
    cursor.execute('''CREATE TABLE orderable_items (
                        item_number INTEGER PRIMARY KEY,
                        delivery_day DATE NOT NULL,
                        ordering_day DATE NOT NULL,
                        'index' INTEGER NOT NULL AUTOINCREMENT,
                        purchase_price REAL NOT NULL,
                        suggested_retail_price REAL NOT NULL,
                        profit_margin REAL NOT NULL,
                        tags TEXT NOT NULL,
                        is_bio BOOLEAN NOT NULL,
                        product_line TEXT NOT NULL,
                        item_categories TEXT NOT NULL,
                        extra_categories TEXT NOT NULL,
                        case_content_quantity INTEGER NOT NULL,
                        case_content_unit TEXT NOT NULL
                    )''')

    # create a trigger that resets the index it will check if the date has a new value if yes then resset index to 0
    cursor.execute('''CREATE TRIGGER reset_index 
                    BEFORE INSERT ON orderable_items
                    FOR EACH ROW
                    BEGIN 
                    IF (strftime('%d', new.ordering_day) != strftime('%d', (SELECT ordering_day FROM orderable_items ORDER BY ordering_day DESC LIMIT 1))) THEN
                        UPDATE orderable_items SET `index` = 0;
                    END IF;
                    END;
                    ''')

    # limit the otpion of the tags to ('new','on_sale','price_change')
    cursor.execute("ALTER TABLE orderable_items ADD CHECK (tags IN ('new','on_sale','price_change'))")

    # Commit the changes
    conn.commit()

    # close the connection
    conn.close()