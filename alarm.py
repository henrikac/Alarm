import os

from timer import Timer


class Alarm:
    options = (
        ('start', 'Start timer'),
        ('set timer', 'Here you can set a new timer'),
        ('quit', 'Exit the program')
    )

    def __init__(self):
        self.counter = 5  # default timer
        self.timer = Timer()

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_options(self):
        for option in self.options:
            print('{}: {}'.format(option[0], option[1]))
        print('\nCurrent timer: {} minutes'.format(self.counter))

    def set_timer(self):
        self.counter = self.timer.change_timer()

    def start(self):
        self.timer.start(self.counter)

    def run(self):
        self.clear_screen()
        print('''
Welcome.
\nThis program will help you reduce risk for short/long term damage.
The program will tell you when it's time for a break away from the computer (minimum 5 minutes).
You know it's time for a break when you hear the song 'Banana Phone' playing.
The standard timer is set to 45 minutes, but you can set it to anything you like (between 1 and 120 minutes).\n''')
        self.print_options()

        while True:
            choice = input('\nWhat do you want to do? ').lower().strip()

            if choice == 'quit':
                break
            elif choice == 'start':
                self.clear_screen()
                self.start()
                self.print_options()
            elif choice == 'set timer':
                self.set_timer()
                self.clear_screen()
                self.print_options()
            else:
                print('That is not a valid input, try again.\n')


if __name__ == '__main__':
    alarm = Alarm()
    alarm.run()
