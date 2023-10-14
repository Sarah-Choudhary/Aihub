"""
Tests for the daily_task module.
"""

import sys
sys.path.append("/workspaces/Aihub")

from src.daily_task import estimate_time

def test_estimate_time():
    """
    Test the estimate_time function.
    """
    task = "Reading a 20-page book"
    estimated_time = estimate_time(task)
    assert estimated_time == 40, f"Expected 40, but got {estimated_time}"
    print(f"Task: {task}, Estimated Time: {estimated_time} minutes")

if __name__ == "__main__":
    test_estimate_time()
