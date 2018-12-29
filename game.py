"""
Animal Diary: this diary application asks you how you are feeling and encourages you to write your emotions and experiences down. Steps:
    Open diary

    User enters date and title

    Diary asks if you want to chat or write

    If chat: enter feeling --> get animal response --> asks if you're ready to write --> loop til write or exit.

    If/when write, prompt to start writing
    
    After writing - save? If yes, log away. If no, don't save.
"""
import datetime
now = datetime.datetime.now()
diary_entries = {}

environment_lookup = {'U': 'lobster', 'G': 'spider', 'S': 'giraffe' , 'O': 'alien'}

animals_lookup = {'giraffe': '    /)/) \n   ( ..\     \n   /\'-._)   \n  /#/       \n /#/  ',
            'alien' : ' o   o\n  )-(\n (O O)\n  \=/\n .-"-.',
            'spider' : '  /^\ ___ /^\ \n //^\(o o)/^\\\n/\'<^~\'\'~\'\'~^>\'\ ', 
            'lobster' : ' /==g           _\n//      >>>/---{_\n`==::[[[[|:     _\n        >>>\---{_ '}

feels_lookup = {'happy': ':-) It\'s a beautiful day! Enjoy this bliss.',
                'sad': 'Everyone has rough days. It\'s ok to cry! And sometimes it feels great;-).',
                'self-conscious': 'Pft, fuck the haters. You\'re beautiful, smart and capable. Go get \'em girl <3.',
                'confident': 'Yeehaw. Do something nice for a friend today!',
                'tired': 'Take a nap, chickadee! Gotta rest to be the best.',
                'energized': 'Love it. Think about what you want to accomplish today and take steps towards that.',
                'annoyed': 'HRUMPH. I know the feeling. Ah, fuck it. Go hang out with Leia:).',
                'other': 'I got you, gurl. Your feelings are valid! Here\'s a virtual hug. Go do something positive for yourself or a loved one.'}

def pick_a_creature(environment_lookup, animals_lookup):
    """Asks user for environment preference - returns user input value"""

    while True:

        environment = input('Pick an environment. \n Enter: \n - Underwater (U) \n - On the ground (G) \n - In the sky (S) \n - Outerspace (O) \n > ').upper()
        print()

        if environment in ('U', 'G', 'S', 'O'):
            creature = environment_lookup[environment]
            creature_character = animals_lookup[creature]
            return (creature, creature_character)
            break

        else:
            print('I didn\'t understand that. Please enter U,G,S, or O')

def match_feeling_to_advice(feels_lookup):
    """Asks user how they are feeling - returns user input value"""
    
    feels = input('How are you feeling today? \n Enter: \n - happy \n - sad \n - self-concious \n - confident \n - tired \n - energized \n - annoyed \n - other \n >  ')
    print()

    if feels in feels_lookup:
        return feels_lookup[feels]
    else:
        return feels_lookup['other']

def give_advice(advice, creature, creature_character):
    """Prints an input piece of advice with assigned ascii character."""

    print(creature_character)
    print()
    print(creature.upper(), "says.....", advice)
    print()

def enter_date_and_title():
    """Prompts user for date and title for their diary entry - returns user input value"""
    
    todays_date = input('Enter date/time: ')
    todays_title = input('Enter entry title: ')

    return todays_date, todays_title

def write_diary_entry():
    """promps the user to input title and a diary entry""" 
    print ('Great. Let\'s get some thoughts down.')
    print()
    
    print ('If you save this entry, I\'ll log it with today\'s date and a title of your choosing.')
    print()

    date = str(now.month) + '.' + str(now.day) + '.' + str(now.year)
    title = input('What would you like to call this entry? > ')
    
    print('Date: {}     Title: {}   '.format(date, title))
    print()
    entry = input('Let\'s write. Ready when you are! \n \n > ')
    print()
    
    return entry, date, title

def save_diary_entry(new_entry, date, title, diary_dictionary):
    """save diary entry into a dictionary"""
    diary_dictionary[date] = [title, new_entry]
    print('Great, I\'ve logged your entry!')
    return diary_entries


def diary_main():
    """calls all the other functions!"""
    print('Heyo - diary here. Whatcha feel like doing?')
    print()
    
    while True:
    
        user_action = input('(W)rite, (A)dvice, (V)iew, (E)xit? >  ').upper()
        print()

        if user_action == 'W':
            new_entry, date, title = write_diary_entry()
            save_entry = input('Would you like to save your diary entry? (Y/N) ').upper()
            print() 

            if save_entry == 'Y':
                diary_updated = save_diary_entry(new_entry, date, title, diary_entries)
                print()

        elif user_action == 'A':
            advice = match_feeling_to_advice(feels_lookup)
            creature, creature_character = pick_a_creature(environment_lookup, animals_lookup)
            give_advice(advice, creature, creature_character) 
        
        elif user_action == 'E':
            print('Cool, let\'s catch up later! Always here for whatever you need.')
            break 
        
        elif user_action == 'V':
            print(diary_entries)
            print()

        else:
            print("Sorry, I didn't understand that. Please enter W, T, V or E.")
            print()

diary_main()
