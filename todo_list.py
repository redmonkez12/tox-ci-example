class Todo:
    def __init__(self, id, label, status):
        self.id = id
        self.label = label
        self.status = status
# ------------------------------------------------------|
# Ukol                                                  |
# Ve tride Todo list udelat metodu done                 |
#  a tato metoda prevede todo podle id                  |
# na stav done                                          |
# ------------------------------------------------------|
# Hint                                                  |
# musite zaiterovat nad todo a prvne si to toto najit   |
# Pokud ho nenajdete tak vratite None                   |
# ------------------------------------------------------|

class TodoList:
    def __init__(self):
        self.todos: list[Todo] = []

    def add(self, label: str, status: str):
        todo = Todo(id=len(self.todos) + 1, label=label, status=status)
        self.todos.append(todo)

        return todo

    def done(self, id: int):
        for todo in self.todos:
            if todo.id == id:
                todo.status = "done"
                return todo

        return None

    def change_status(self, id, status):
        change_todo = None

        for todo in self.todos:
            if todo.id == id:
                change_todo = todo
                break

        if not change_todo:
            raise Exception(f"Todo not found [{id}]")

        change_todo.status = status

        return change_todo

    def remove(self, id):
        for index, todo in enumerate(self.todos):
            if todo.id == id:
                del self.todos[index]
                return True

        return False