import json
from urllib.request import urlopen

with urlopen("http://jsonplaceholder.typicode.com/todos") as response:
    source = response.read()

data = json.loads(source)


new_user_id = 11
new_todo_id = len(data) + 1
new_title = "Stuffs"
completed = False
new_todo = {"userId": new_user_id, "id": new_todo_id, "title": new_title, "completed": completed}
data.append(new_todo)

given_id = 19
for todo in data:
    if todo['id'] is given_id:
        data.remove(todo)

with open('todos_list.json', 'w') as new_file:
    json.dump(data, new_file, indent=2)