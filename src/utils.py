"""
Utility functions for the DailyTaskCalculator.
"""

def convert_minutes_to_readable_format(minutes):
    """
    Converts minutes to a more readable format.
    """
    hours = minutes // 60
    minutes %= 60

    if hours and minutes:
        return f"{hours} hour(s) and {minutes} minute(s)"
    elif hours:
        return f"{hours} hour(s)"
    else:
        return f"{minutes} minute(s)"
