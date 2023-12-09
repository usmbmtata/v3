# Assuming you have a function like this in your utils
def generate_registration_number(last_registration_number):
    if last_registration_number:
        # Extract the numeric part of the last registration number
        last_number = int(last_registration_number.reg_no[3:])
        # Increment by 1
        new_number = last_number + 1
        # Format it back to the registration number format (assuming reg001, reg002, etc.)
        new_registration_number = f'reg{new_number:03d}'
    else:
        # If no previous registration number, start from reg001
        new_registration_number = 'reg001'

    return new_registration_number
