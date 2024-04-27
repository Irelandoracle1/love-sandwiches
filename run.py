import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

def get_sales_data():
    """
    get sales data
    """
    while True:
        print("please enter sales data from last market.")
        print("Data should be six numbers , seperated by commas")
        print("Examples: 10,20,30,30,50,60\n")
        
        data_str = input("Enter your data here: ")
    
        sales_data = data_str.split(",")
        

        if validate_data(sales_data):
            print("Data is Valid")
            break
        
    return sales_data        


   
    

def validate_data(values):
    """
    check if values are 6 and can be converted to integers with try 
    and except
    """
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"invalid data: {e}, please try again.\n")
        return False        
    return True



def update_sales_worksheet(data):
    """
    update sales worksheet and add new row with list of data provided
    """
    print("updating sales worksheet....\n")
    sales_worksheet = SHEET.worksheet("sales")
    sales_worksheet.append_row(data)
    print("sales worksheet updated succesfully\n")


def caculate_surplus_data(sales_row):
    """
    compare sales with stock and calculate the surplus for each 
    item type
    surplus is sales minus stock
    positive surplus is waste
    negative surplus indicates extra made when stock was sold out
    """
    stock = SHEET.worksheet("stock").get_all_values()
    
    stock_row = stock[-1]
    print(stock_row)







def main():
    """
    run all program function
    """
    data = get_sales_data() 
    sales_data = [int(num) for num in data]
    update_sales_worksheet(sales_data)
    caculate_surplus_data(sales_data)


print("WELCOME TO LOVE SANWHICHES")
main()




















