import time
import webbrowser


class Timer:
    def change_timer(self):
        while True:
            try:
                new_timer = int(input('Enter a new timer: '))
            except ValueError:
                print('That is not a valid input.')
            else:
                if new_timer > 0 and new_timer < 121:
                    return new_timer
                else:
                    print('Remember timers has to be between 1 and 120 minutes.')

    def timer_ended(self):
        try:
            webbrowser.open('https://www.youtube.com/watch?v=j5C6X9vOEkU', 2, True)
        except webbrowser.Error:
            print('Browser control error.')

    def start(self, timer):
        while timer:
            print('{} minutes left'.format(timer))
            timer -= 1
            time.sleep(60)
        print('Timer ended\n')
        self.timer_ended()
