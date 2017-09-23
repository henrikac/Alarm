from timer import Timer


class Alarm:
    def __init__(self):
        self.timer = 45  # default timer

    def start(self):
        timer = Timer(self.timer)
        timer.start()


if __name__ == '__main__':
    alarm = Alarm()
    alarm.start()
