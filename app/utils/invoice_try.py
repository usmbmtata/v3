from datetime import datetime
from app import db
from app.models.fee_fare import Fee_Fare
from datetime import datetime
from flask import flash



def fetch_rate(date_str, input_type):
    # Convert input date string to a datetime object
    input_date = datetime.strptime(date_str, '%Y-%m-%d')
    print(input_date)
    # Fetch the relevant entry from the database based on the date
    if input_date >= datetime(2023, 1, 1):
        entry = Fee_Fare.query.filter(Fee_Fare.date <= input_date).order_by(Fee_Fare.date.desc()).first()
    elif input_date >= datetime(2022, 9, 30):
        entry = Fee_Fare.query.filter(Fee_Fare.date >= datetime(2022, 9, 30), Fee_Fare.date <= input_date).order_by(Fee_Fare.date.desc()).first()
    else:
        entry = Fee_Fare.query.filter(Fee_Fare.date >= datetime(2022, 3, 4), Fee_Fare.date <= input_date).order_by(Fee_Fare.date.desc()).first()

    if entry is not None:
        # Check each type column in the fetched entry
        for column_name in entry.__table__.columns.keys():
            if column_name.startswith("type"):
                # Check if the type matches the input type
                if type == column_name:
                    return getattr(entry, column_name)  # Return the value of the matching type column

        # If the input type doesn't match any column, return an error message
        return "Error: Type not found in the database."

    else:
        # If no entry is found for the given date, return an error message
        return "Error: No entry found for the given date."

# Example usage:
date_str = "2023-10-12"
input_type = "type_b"
result = fetch_rate(date_str, input_type)
print(result)
