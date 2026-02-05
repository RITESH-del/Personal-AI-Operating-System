class AppLogic:
    def generate_message(self, name):
        if not name.strip():
            return "Please enter a valid name."
        return f"Hello, {name}! Welcome to your GUI app."
