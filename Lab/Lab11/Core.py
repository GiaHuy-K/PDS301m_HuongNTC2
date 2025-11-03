# app.py
from flask import Flask, jsonify, request

# Khởi tạo ứng dụng Flask
app = Flask(__name__)

# --- Kho dữ liệu "trong bộ nhớ" (để đơn giản) ---
# Trong ứng dụng thật, đây sẽ là một cơ sở dữ liệu (database).
tasks = [
    {
        'id': 1,
        'title': 'Learn Python',
        'description': 'Complete a Python course to understand the basics.',
        'done': True
    },
    {
        'id': 2,
        'title': 'Build a REST API',
        'description': 'Use Flask to create a simple RESTful API.',
        'done': False
    }
]

# --- Các Endpoint của API ---

# [READ] GET /tasks
# Lấy danh sách TẤT CẢ các task.
@app.route('/tasks', methods=['GET'])
def get_tasks():
    # jsonify: Hàm của Flask, chuyển Python dict thành JSON hợp lệ
    return jsonify({'tasks': tasks})

# [READ] GET /tasks/<int:task_id>
# Lấy MỘT task cụ thể bằng ID của nó.
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    # Tìm task có ID khớp
    # next(...) là một cách viết gọn của vòng lặp for
    task = next((task for task in tasks if task['id'] == task_id), None)
    
    if task is None:
        # Nếu không tìm thấy, trả về lỗi 404 (Not Found)
        return jsonify({'error': 'Task not found'}), 404
        
    return jsonify({'task': task})

# [CREATE] POST /tasks
# Tạo một task mới.
@app.route('/tasks', methods=['POST'])
def create_task():
    # Kiểm tra xem client có gửi 'request.json' (dữ liệu JSON) không
    if not request.json or not 'title' in request.json:
        # Trả về lỗi 400 (Bad Request) nếu thiếu 'title'
        return jsonify({'error': 'Bad Request: Missing title in request body'}), 400
        
    new_task = {
        # Tạo ID mới: lấy ID cuối cùng + 1 (cách đơn giản)
        'id': tasks[-1]['id'] + 1 if tasks else 1, 
        'title': request.json['title'],
        'description': request.json.get('description', ""), # .get() an toàn, nếu thiếu thì trả về ""
        'done': False
    }
    
    tasks.append(new_task)
    
    # Trả về task mới, kèm mã trạng thái 201 (Created)
    return jsonify({'task': new_task}), 201

# [UPDATE] PUT /tasks/<int:task_id>
# Cập nhật một task đã có.
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
        
    if not request.json:
        return jsonify({'error': 'Bad Request: Invalid JSON'}), 400
        
    # Cập nhật các trường nếu chúng được cung cấp trong request
    # dùng .get(key, default_value)
    task['title'] = request.json.get('title', task['title'])
    task['description'] = request.json.get('description', task['description'])
    task['done'] = request.json.get('done', task['done'])
    
    return jsonify({'task': task})

# [DELETE] DELETE /tasks/<int:task_id>
# Xóa một task.
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    
    if task is None:
        return jsonify({'error': 'Task not found'}), 404
        
    tasks.remove(task)
    
    return jsonify({'result': True})

# Đoạn này cho phép chạy file Python trực tiếp
if __name__ == '__main__':
    # host='0.0.0.0' giúp server có thể được truy cập từ bên ngoài
    # debug=True: Tự động khởi động lại server khi code thay đổi
    app.run(host='0.0.0.0', port=5000, debug=True)