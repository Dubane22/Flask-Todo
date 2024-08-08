from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
todos = []

@app.route('/')
def index():
	return render_template('index.html', todos = todos)

@app.route('/add', methods=['POST'])
def add_todo():
	todos_items = request.form.get('todo_item')
	if todos_items:
		todos.append(todos_items)

	return redirect(url_for('index'))
print(todos)

if __name__ == '__main__':
	app.run(debug=True)