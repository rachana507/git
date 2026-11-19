def todatetime(date_str):
    """
    Convert a date string in the format 'YYYY-MM-DD' to a datetime object.
    
    Parameters:
    date_str (str): The date string to convert.
    
    Returns:
    datetime: A datetime object representing the given date.
    """
    from datetime import datetime
    return datetime.strptime(date_str, '%Y-%m-%d')