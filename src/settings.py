class Settings:
    options = (
        ('timer', 'Here you can set a new timer.'),
        ('reminder', 'Here you can change the \'reminder song\'.'),
        ('back', 'return you to start')
    )

    def __init__(self):
        self.counter = 45  # default timer
        self.reminder_song = 'https://www.youtube.com/watch?v=j5C6X9vOEkU'  # default song (Banana Phone)

    def change_settings(self):
        while True:
            option = input('\nEnter an option: ').lower()

            if option == 'back':
                break
            elif option == 'timer':
                self.set_new_timer()
                break
            elif option == 'reminder':
                self.set_new_reminder_song()
                break
            else:
                print('That is not a valid option, try again.')

    def set_new_timer(self):
        while True:
            try:
                new_timer = int(input('\nEnter a new timer: '))
            except ValueError:
                print('That is not a valid input.')
            else:
                if new_timer > 0 and new_timer < 121:
                    self.counter = new_timer
                    break
                else:
                    print('Remember the timer has to be between 1 and 120 minutes.')

    def set_new_reminder_song(self):
        print('\nTo change the \'reminder song\' you need to enter a url for a youtube video.')
        print('Type \'quit\' to go back without changing the \'reminder song\'.')

        while True:
            new_reminder_song = input('\nEnter url for the new song: ')
            if new_reminder_song.lower() == 'quit':
                break
            elif 'youtube' not in new_reminder_song:
                print('Please enter a url for a youtube video.')
                continue
            else:
                self.reminder_song = new_reminder_song
                break
