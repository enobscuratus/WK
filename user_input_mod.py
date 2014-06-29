"""These function gets user input in unicode, add single
quotes to each end of the string (so that the SQL query
will have correct syntax), and then converts.
the entire string to utf-8 encoding """


def get_ticker():
    
    return str(raw_input('Enter the stock symbol: '))

def get_index():

    return str(raw_input('Enter the index symbol: '))

def get_start_date():

    return str(raw_input('Enter the start date: '))
    
def get_end_date():

    return str(raw_input('Enter the end date: '))

def get_mysqlpw():

    return str(raw_input('Enter the password: '))

def get_mysqlusr():

    return str(raw_input('Enter the user id: '))
