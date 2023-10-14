def test_estimate_time():
    task = "Reading a 20-page book"
    estimated_time = estimate_time(task)
    print(f"Task: {task}, Estimated Time: {estimated_time}")
    assert estimated_time == 40, f"Expected 40, but got {estimated_time}"
