from datetime import datetime


def generate_invoice_number(last_invoice_number):
    try:
        # Extract YYMM and NNN from the last invoice number
        last_yymm = last_invoice_number[8:12]
        last_nnn = int(last_invoice_number[-3:])

        # Get current YYMM
        curr_yymm = datetime.now().strftime('%y%m')

        # Compare last_YYMM with curr_YYMM
        if last_yymm == curr_yymm:
            nnn = last_nnn
        else:
            nnn = 0

        # Increment NNN by 1
        nnn += 1

        # Format the new invoice number
        new_inv_number = f'inv_ved-{curr_yymm}{nnn:03d}'

        return new_inv_number
    except Exception as e:
        # In case of any error, return the default value
        default_value = f'inv_ved-{datetime.now().strftime("%y%m")}001'
        return default_value

