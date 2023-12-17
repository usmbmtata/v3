from app import db
from app.models.fee_fare import Fee_Fare
from datetime import datetime


def get_rate(type, date):
    # Assuming date is a string in the format 'YYYY-MM-DD'
    date = datetime.strptime(date, '%Y-%m-%d').date()

    # Query the database for the rates
    rates = Fee_Fare.query.filter(Fee_Fare.date <= date).order_by(Fee_Fare.date.desc()).first()

    if rates is None:
        return None

    # Return the rate based on the type
    if type == 'type_a':
        return rates.type_a
    elif type == 'type_b':
        return rates.type_b
    elif type == 'type_c':
        return rates.type_c
    elif type == 'type_d':
        return rates.type_d
    elif type == 'type_e':
        return rates.type_e
    elif type == 'type_a1':
        return rates.type_a1
    elif type == 'type_b1':
        return rates.type_b1
    elif type == 'type_c1':
        return rates.type_c1
    elif type == 'type_d1':
        return rates.type_d1
    elif type == 'type_e1':
        return rates.type_e1
    else:
        return None
