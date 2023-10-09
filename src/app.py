from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [
  {"label": "My first task", "done": False},
  {"label": "My second task", "done": False},
]

# GET
@app.route('/todos', methods=['GET'])
def hello_world():
  print('Testing')
  json_data = jsonify(todos)
  return json_data

# POST
@app.route('/todos', methods=['POST'])
def add_new_todo(): 
  request_body = request.get_json(silent=True)
  if request_body is None: 
    return 'Invalid JSON in request body', 400
  todos.append(request_body)
  return jsonify(todos), 200

# DELETE
@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id): 
  del todos[todo_id]
  return jsonify(todos), 200

# END
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)