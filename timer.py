import time


class Timer:
    def __init__(self, timer):
        self.timer = timer

    def start(self):
        while self.timer:
            print('{} minutes left'.format(self.timer))
            self.timer -= 1
            time.sleep(60)
        print('Timer ended')
