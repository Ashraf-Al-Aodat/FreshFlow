'''
    This file contains the endpoints and logic for handling HTTP requests and responses.
'''

import sqlite3
from flask import jsonify

def get_orders():
        # Connect to database
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Query the database and return the list of dicts
    cursor.execute("""SELECT orderable_items.item_number,
                            orderable_items.ordering_day,
                            orderable_items.delivery_day,
                            orderable_items.suggested_retail_price,
                            orderable_items.profit_margin,
                            orderable_items.purchase_price,
                            orderable_items.item_categories,
                            orderable_items.tags || ' ' || orderable_items.extra_categories as labels,
                            orderable_items.case_content_quantity,
                            orderable_items.case_content_unit,
                            (sales_predictions.sales_quantity - inventory.inventory) / orderable_items.case_content_quantity as order_quantity,
                            inventory.inventory,
                            order_intake.unit
                      FROM orderable_items
                      LEFT JOIN inventory
                      ON orderable_items.item_number = inventory.item_number
                      AND DATE(inventory.day) = orderable_items.ordering_day
                      LEFT JOIN sales_predictions
                      ON orderable_items.item_number = sales_predictions.item_number
                      AND DATE(sales_predictions.day) = orderable_items.delivery_day
                      LEFT JOIN order_intake
                      ON orderable_items.item_number = inventory.item_number
                      AND DATE(order_intake.day) = orderable_items.delivery_day
                      """)

    data = cursor.fetchall()

    # Close the connection
    conn.close()

    # Create the list of dicts
    order_list = []
    for row in data:
        item_number, ordering_day, delivery_day, suggested_retail_price, profit_margin, purchase_price, item_categories, labels, case_content_quantity, case_content_unit, order_quantity, inventory_quantity, inventory_unit = row
        labels = labels.split()
        item_categories = item_categories.split(',')
        case = {'quantity': case_content_quantity, 'unit': case_content_unit}
        order = {'quantity': order_quantity, 'unit': 'CS'}
        inventory = {'quantity': inventory_quantity, 'unit': inventory_unit}
        order_list.append({'item_number': item_number, 'ordering_day': ordering_day, 'delivery_day': delivery_day, 'sales_price_suggestion': suggested_retail_price, 'profit_margin': profit_margin, 'purchase_price': purchase_price, 'item_categories': item_categories, 'labels': labels, 'case': case, 'order': order, 'inventory': inventory})

    return jsonify(order_list)