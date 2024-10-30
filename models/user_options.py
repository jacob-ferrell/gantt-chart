from constants import COLORS

class UserOptions:

    def __init__(self):
        self.set_mode()
        self.set_color_palette()
        self.set_has_demo_data()

    # Get choice of light/dark mode from user
    def set_mode(self):
        choice = None
        acceptable_inputs = ('1', '2')
        while choice not in acceptable_inputs:
            choice = input('\nSelect an option: \n1: Light Mode\n2: Dark Mode\n')
        self.dark_mode = choice == '2'

    # Get choice of color palette from user:
    def set_color_palette(self):
        choice = None
        acceptable_choices = ('1', '2')
        while choice not in acceptable_choices:
            choice = input('\nSelect one of the following color palettes:\n1. ROY G BIV (Well suited for light/dark mode)\n2. SHADES OF GRAY (Best in light mode)\n')

        self.color_palette = COLORS.get(('ROY G BIV', 'SHADES OF GRAY')[int(choice) - 1])


    # Give user option to add demo data to dataset to showcase ability to handle 
    # multiple periods per ship
    def set_has_demo_data(self):
        acceptable_choices = ['1', '2']
        choice = None
        #choice = '1' # auto select 1 for development
        while choice not in acceptable_choices:
            choice = input('\nSelect one of the following options:\n1. Generate chart with original data\n2. Generate chart with demo data, showcasing handling of multiple maintenance/docking periods per ship\n')

        self.has_demo_data = choice == '2'