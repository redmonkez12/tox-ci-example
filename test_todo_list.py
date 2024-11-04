from todo_list import Todo, TodoList

def test_append_todo():
    todo_list = TodoList()
    todo_list.add("Jit ven", "backlog")

    assert len(todo_list.todos) == 1
    assert todo_list.todos[0].status == "backlog"

def test_done_status():
    todo_list = TodoList()
    todo_list.add("Jit ven", "backlog") # 1
    todo_list.add("Koupit rohliky", "backlog") # 2

    todo_1 = todo_list.done(1)
    todo_2 = todo_list.done(2)

    assert todo_1.status == "done"
    assert todo_2.status == "done"

def test_done_status_not_found():
    todo_list = TodoList()

    todo = todo_list.done(2)

    assert todo is None

def test_change_status():
    todo_list = TodoList()
    todo_list.add("Jit ven", "backlog")  # 1
    todo_list.add("Koupit rohliky", "backlog")  # 2

    todo_1 = todo_list.change_status(1, "in_progress")
    todo_2 = todo_list.change_status(2, "in_progress")

    assert todo_1.status == "in_progress"
    assert todo_2.status == "in_progress"

def test_remove_todo():
    todo_list = TodoList()
    todo_list.add("Jit ven", "backlog")  # 1
    todo_list.add("Koupit rohliky", "backlog")  # 2
    todo_list.add("Koupit chleba", "backlog")  # 3

    result = todo_list.remove(2)

    assert result == True
    assert todo_list.todos[0].id == 1
    assert todo_list.todos[1].id == 3