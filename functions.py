import pandas as pd
import os

def verify_user(ic_number, password):
    """Verify the user's credentials."""
    return ic_number.isdigit() and len(ic_number) == 12 and ic_number[-4:] == password

def calculate_tax(income, tax_reliefs):
    """Calculate the tax payable based on Malaysian tax rates."""

    taxable_income = income - tax_reliefs
    tax_payable = 0

    if taxable_income <= 5000:
        tax_payable = 0
    elif taxable_income <= 20000:
        tax_payable = (taxable_income - 5000) * 0.01
    elif taxable_income <= 35000:
        tax_payable = 150 + (taxable_income - 20000) * 0.03
    elif taxable_income <= 50000:
        tax_payable = 600 + (taxable_income - 35000) * 0.06
    elif taxable_income <= 70000:
        tax_payable = 1500 + (taxable_income - 50000) * 0.11
    elif taxable_income <= 100000:
        tax_payable = 3700 + (taxable_income - 70000) * 0.19
    elif taxable_income <= 400000:
        tax_payable = 9400 + (taxable_income - 100000) * 0.25
    elif taxable_income <= 600000:
        tax_payable = 84900 + (taxable_income - 400000) * 0.26
    elif taxable_income <= 2000000:
        tax_payable = 136400 + (taxable_income - 600000) * 0.28
    else:
        tax_payable = 528400 + (taxable_income - 2000000) * 0.30
    return tax_payable

def save_to_csv(data, filename):
    """Save user data to a CSV file."""
    columns = ['IC Number', 'Annual Income', 'Tax Relief', 'Tax Payable']
    df = pd.DataFrame([data])

    if not os.path.exists(filename):
        df.to_csv(filename, mode='w', header=columns, index=False)
    else:
        df.to_csv(filename, mode='a', header=False, index=False)

def read_from_csv(filename):
    """Read data from the CSV file."""
    if os.path.exists(filename):
        return pd.read_csv(filename)
    else:
        return None