class Task:
    def __init__(self, title, priority, done=False):
        self.title = title
        self.priority = priority
        self.done = done

class TaskManager():
    def __init__(self):
        self.tasks = []

    def add_task(self, title, priority):
        task = Task(title, priority)
        self.tasks.append(task)

    def show_all(self):
        for task in self.tasks:
            status = "[Done]" if task.done else "[Not Done]"
            print(f"{task.title} - Priority: {task.priority} - Status: {status}")

    def complete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                task.done = True
                break

    def delete_done(self):
        self.tasks = [task for task in self.tasks if not task.done]

    def save(self, filename):
        with open(filename, "w") as f:
            for task in self.tasks:
                f.write(f"{task.title},{task.priority},{task.done}\n")

    def load(self, filename):
        try:
            with open(filename, "r") as f:
                for line in f:
                    title, priority, done = line.strip().split(",")
                    done = done == "True"
                    self.tasks.append(Task(title, priority, done))
        except FileNotFoundError:
            print("Файл не найден, начинаем с пустого списка")


manager = TaskManager()
manager.add_task("Купить продукты", "высокий")
manager.add_task("Позвонить маме", "средний")
manager.complete_task("Купить продукты")
manager.delete_done()
manager.save("tasks.txt")
manager.load("tasks.txt")
manager.show_all()
