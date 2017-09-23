import time
import webbrowser


class Timer:
    def __init__(self, timer):
        self.timer = timer

    def timer_ended(self):
        try:
            webbrowser.open('https://www.youtube.com/watch?v=j5C6X9vOEkU', 2, True)
        except webbrowser.Error:
            print('Browser control error.')

    def start(self):
        while self.timer:
            print('{} minutes left'.format(self.timer))
            self.timer -= 1
            time.sleep(60)
        print('Timer ended\n')
        self.timer_ended()
