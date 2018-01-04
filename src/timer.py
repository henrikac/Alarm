import time
import webbrowser


class Timer:
    def timer_ended(self, reminder_song):
        try:
            webbrowser.open(reminder_song, 2, True)
        except webbrowser.Error:
            print('Browser control error.')

    def start(self, timer, reminder_song):
        while timer:
            print('{} minutes left'.format(timer))
            timer -= 1
            time.sleep(60)
        print('Timer ended\n')
        self.timer_ended(reminder_song)
