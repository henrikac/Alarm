import os

from scraper import Scraper
from settings import Settings
from timer import Timer


class Alarm:
    options = (
        ('start', 'Start timer'),
        ('settings', 'Here you can change the settings'),
        ('quit', 'Exit the program')
    )

    def __init__(self):
        self.scraper = Scraper()
        self.settings = Settings()
        self.timer = Timer()

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_options(self, options):
        for option in options:
            print('{}: {}'.format(option[0], option[1]))
        print('\nCurrent timer: {} minutes'.format(self.settings.counter))
        print('Current \'reminder song\': {}'.format(self.scraper.scrape_url(self.settings.reminder_song)))

    def run(self):
        self.clear_screen()
        print('''
Welcome.
\nThis program will help you reduce risk for short/long term damage.
The program will tell you when it's time for a break away from the computer (minimum 5 minutes).
You know it's time for a break when you hear the 'reminder song' (default: Banana Phone) playing.
The standard timer is set to 45 minutes, but you can set it to anything you like (between 1 and 120 minutes).\n''')
        self.print_options(self.options)

        while True:
            choice = input('\nWhat do you want to do? ').lower().strip()

            if choice == 'quit':
                break
            elif choice == 'start':
                self.clear_screen()
                self.timer.start(self.settings.counter, self.settings.reminder_song)
                self.print_options(self.options)
            elif choice == 'settings':
                self.clear_screen()
                self.print_options(self.settings.options)
                self.settings.change_settings()
                self.clear_screen()
                self.print_options(self.options)
            else:
                print('That is not a valid input, try again.\n')


if __name__ == '__main__':
    alarm = Alarm()
    alarm.run()
