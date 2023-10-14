"""
Module for daily tasks and their time estimation.
"""

import re

def estimate_time(task):
    """
    Estimates time for a given daily task in natural language.
    
    Example: "Reading a 20-page book" might give 40 minutes, assuming an average of 
    2 minutes per page.
    """
    if "read" in task.lower() and "page" in task.lower():
        pages = int(re.search(r'\d+', task).group())
        return pages * 2  # Assuming 2 minutes per page

    # More patterns and estimations can be added as the program grows.

    return None  # If we don't have a pattern match for the given task
