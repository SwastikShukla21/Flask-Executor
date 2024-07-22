from flask import Flask, request, jsonify
from flask_executor import Executor
import time
from tasks import long_running_task
app = Flask(__name__)
executor = Executor(app)


tasks = {}

@app.route('/start-task', methods=['POST'])
def start_task():
    data = request.json
    future = executor.submit(long_running_task, data)
    task_id = id(future)
    tasks[task_id] = future
    return jsonify({'task_id': task_id}), 202

@app.route('/task-status/<int:task_id>', methods=['GET'])
def task_status(task_id):
    future = tasks.get(task_id)
    if not future:
        return jsonify({'status': 'Task not found'}), 404

    if future.running():
        return jsonify({'status': 'Running'})
    elif future.done():
        try:
            result = future.result()
            return jsonify({'status': 'Completed', 'result': result})
        except Exception as e:
            return jsonify({'status': 'Failed', 'error': str(e)}), 500
    else:
        return jsonify({'status': 'Pending'})


if __name__ == '__main__':
    app.run(debug=True)

