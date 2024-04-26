import gspread
from google.oauth2.service_account import Credentials

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




data = get_sales_data() 



















