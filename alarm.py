import os

from timer import Timer


class Alarm:
    options = (
        ('start', 'Start timer'),
        ('quit', 'Exit the program')
    )

    def __init__(self):
        self.timer = 45  # default timer

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_options(self):
        for option in self.options:
            print('{}: {}'.format(option[0], option[1]))

    def start(self):
        timer = Timer(self.timer)
        timer.start()

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
            choice = input('\nWhat do you want to do? ').lower()

            if choice == 'quit':
                break
            elif choice == 'start':
                self.clear_screen()
                self.start()
                self.print_options()
            else:
                print('That is not a valid input, try again\n.')


if __name__ == '__main__':
    alarm = Alarm()
    alarm.run()
