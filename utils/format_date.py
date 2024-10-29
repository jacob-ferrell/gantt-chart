from datetime import datetime

# convert date string into datetime object
def format_date(date_string):
    return datetime.strptime(date_string, "%m%d%Y")

