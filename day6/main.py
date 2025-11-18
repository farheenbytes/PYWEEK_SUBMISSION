from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Models
class Todo(BaseModel):
    id: int
    task: str
    completed: bool = False

class TodoCreate(BaseModel):
    task: str
    completed: bool = False

# Initial todo list
todos = [
    Todo(id=1, task="clean the bed", completed=False),
    Todo(id=2, task="Complete ALC assignment", completed=False),
    Todo(id=3, task="make dinner", completed=False)
]

# Create a new todo
@app.post("/todos")
def create_todo(todo: TodoCreate):
    new_id = len(todos) + 1
    new_todo = Todo(id=new_id, task=todo.task, completed=todo.completed)
    todos.append(new_todo)
    return new_todo

# Get all todos
@app.get("/todos")
def view_todos():
    return todos

# Get a specific todo by id
@app.get("/todos/{todo_id}")
def get_one_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

# Update a todo
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo: Todo):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = Todo(id=todo_id, task=updated_todo.task, completed=updated_todo.completed)
            return todos[index]
    raise HTTPException(status_code=404, detail="Todo id not found")

# Delete a todo
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos.pop(index)
            return {"message": "Todo deleted successfully"}
    raise HTTPException(status_code=404, detail="Todo not found")
