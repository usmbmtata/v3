from datetime import datetime

def generate_invoice_number(last_invoice_number):
    if last_invoice_number:
        # Extract the numeric part of the last invoice number
        last_number = int(last_invoice_number.split('-')[1])
        # Increment by 1
        new_number = last_number + 1
        # Get the current month and year in the YYMM format
        current_month_year = datetime.now().strftime('%y%m')
        # Format it back to the invoice number format (inv_ved-YYMMNNN)
        new_inv_number = f'inv_ved-{current_month_year}{new_number:03d}'
    else:
        # If no previous invoice number, start from inv_ved-YYMM0001
        current_month_year = datetime.now().strftime('%y%m')
        new_inv_number = f'inv_ved-{current_month_year}0001'

    return new_inv_number
