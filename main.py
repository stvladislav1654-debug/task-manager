class Task:
    def __init__(self, title, priority, done=False):
        self.title = title
        self.priority = priority
        self.done = done

t = Task("Купить продукты", "высокий")
print(t.title)     # Купить продукты
print(t.priority)  # высокий
print(t.done)      # False
        