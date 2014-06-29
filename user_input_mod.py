"""These function gets user input in unicode, add single
quotes to each end of the string (so that the SQL query
will have correct syntax), and then converts.
the entire string to utf-8 encoding """



def get_ticker():
    
    raw_ticker ="'" + raw_input('Enter the stock symbol: ') +"'" #Note that raw_input is a builtin function

    encoded_ticker = str(object = raw_ticker)

    return encoded_ticker


def get_index():


    raw_ticker ="'" + raw_input('Enter the index symbol: ') +"'"

    encoded_ticker = str(object = raw_ticker)

    return encoded_ticker


def get_start_date():

    raw_date ="'" + raw_input('Enter the start date: ') +"'"

    encoded_start = str(object = raw_date)

    return encoded_start

def get_end_date():

    raw_date ="'" + raw_input('Enter the end date: ') +"'"

    encoded_end = str(object = raw_date)

    return encoded_end
