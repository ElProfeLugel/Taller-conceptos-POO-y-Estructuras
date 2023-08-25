class Todo:
    description: str
    completed: bool
    def __init__(self, code_id: int, title: str, description: str) -> None:
        self.code_id: int = code_id
        self.title: str = title
        self.description: str = description
        self.completed: bool = False
        self.tags: list[str] = []
        pass

    def mark_completed(self):
        self.completed = True
    
    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)
    
    def __str__(self) -> str:
        return f"{self.code_id} - {self.title}"    

class TodoBook:
    todos: dict[int,Todo]
    def __init__(self) -> None:
        self.todos = {}

    def add_todo(self, title:str, description: str) -> int:
        id = len(self.todos) + 1
        todo = Todo(id, title, description)
        self.todos[id] = todo
        return id
    
    def pending_todos(self) -> list[Todo]:
        pendigItems = [self.todos[i] for i in self.todos if not self.todos[i].completed]
        return pendigItems
    
    def completed_todos(self) -> list[Todo]:
        pendigItems = [self.todos[i] for i in self.todos if self.todos[i].completed]
        return pendigItems
    
    def tags_todo_count(self) -> dict[str, int]:
        listaDeTags = []
        for i in self.todos:
            listaDeTags += self.todos[i].tags
        
        totalTags = {tag: listaDeTags.count(tag) for tag in listaDeTags}

        return totalTags




