class Settings:
    def __init__(self):
        self.counter = 45  # default timer

    def change_timer(self):
        while True:
            try:
                new_timer = int(input('Enter a new timer: '))
            except ValueError:
                print('That is not a valid input.')
            else:
                if new_timer > 0 and new_timer < 121:
                    self.counter = new_timer
                    break
                else:
                    print('Remember the timer has to be between 1 and 120 minutes.')
