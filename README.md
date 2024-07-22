# Flask Async Task Handling Example

This repository contains a Flask application that demonstrates how to handle long-running POST requests asynchronously using `Flask-Executor`. 

## Features

- Asynchronous handling of long-running tasks
- Immediate response with a task ID
- Check task status and retrieve results

## Requirements

- Python 3.x
- Flask
- Flask-Executor

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/SwastikShukla21/Flask-Executor.git
    cd Flask-Executor
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

No additional configuration is required beyond installing the dependencies.

## Usage

1. Run the Flask application:
    ```bash
    python app.py
    ```

2. Send a POST request to start a long-running task:
    ```bash
    curl -X POST -H "Content-Type: application/json" -d '{"key": "value"}' http://localhost:5000/start-task
    ```

   This will return a response with a task ID:
    ```json
    {
        "task_id": 123456789
    }
    ```

3. Check the status of the task:
    ```bash
    curl http://localhost:5000/task-status/123456789
    ```

   The response will indicate the status of the task:
    ```json
    {
        "status": "Running"
    }
    ```

   Once the task is completed, you will get the result:
    ```json
    {
        "status": "Completed",
        "result": {
            "status": "Task completed",
            "data": {"key": "value"}
        }
    }
    ```
