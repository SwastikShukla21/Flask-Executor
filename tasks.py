import time

def long_running_task(data):
    # Simulate a long-running task
    time.sleep(30)  # Replace with actual long-running task
    return {'status': 'Task completed', 'data': data}
