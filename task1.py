# Task 1 - CodeAlpha Backend - To-Do API
from flask import Flask, jsonify, request
app = Flask(__name__)
todos = []
@app.route('/')
def home():
    return "Task 1 Working"
@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)
@app.route('/todos', methods=['POST'])
def add_todo():
    data = request.get_json()
    todos.append(data)
    return jsonify({"message": "Added"})
if __name__ == '__main__':
    app.run()
