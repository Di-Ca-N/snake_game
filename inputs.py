from pynput import keyboard


class KeyboardListener:
    def __init__(self):
        self.listener = keyboard.Listener(on_press=self.notify)
        self.listener.start()

        self.observers = []

    def notify(self, key):
        for observer in self.observers:
            observer(key)

    def subscribe(self, observer):
        self.observers.append(observer)
