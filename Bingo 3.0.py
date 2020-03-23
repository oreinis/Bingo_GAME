import random

class PrintColors:
    HEADER = '\033[95m'
    COLOR_BLUE = '\033[94m'
    COLOR_GREEN = '\033[92m'
    FULL_GREEN = '\033[42m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END_C = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Controls:
    NEW_GAME = 'n'
    ROLL = 'r'
    END_GAME = 'e'
    DEV_TOOLS = 'd'
    QUIT = 'q'
    SET_BINGO = 'b'
    OWNER = 'o'
    SETTINGS_MENU = 's'
    NO_SAME_NUMBER_STATE = 'a'
    BACK = 'b'
    KEEP_TO_FULL = 'f'
    FULL_BINGO = 'z'

class Player:
  def __init__(self, num, name):
    self.num = num
    self.name = name
    self.bingo = False
    self.full_bingo = False
    self.table = [0,0,0,0,0,0,0,0,0]
    self.new_table()

  def table_get(self, table_num):
    return self.table[table_num]

  def new_table(self):
      for i in range(0,9):
          new_num_error = True
          while new_num_error:
              new_num = random.randint(0,50)
              new_num_error = False
              if NO_SAME_NUMBER:
                  for j in range(0,i):
                    if new_num == self.table[j]:
                      new_num_error = True
                      if testing: print('same number found')
          self.table[i] = new_num

  def table_set(self, table_num, num_to_set):
    self.table[table_num] = num_to_set
    self.check_bingo()
    self.check_bingo_full()

  def set_bingo(self):
      self.table = [-1,-1,-1,-1,-1,-1,-1,-1,-1]
      self.check_bingo()

  def bingo(self):
      if self.bingo(): return True
      else: return False

  def owner(self):
      print('Or Reinis is my owner!')

  def check_bingo(self):
    # *****Colls*****
    if not self.bingo:
        for col in range(3):
            if self.table[col] == -1 and self.table[col+3] == -1 and self.table[col+6] == -1:
                self.bingo = True
    # *****Raws*****
    if not self.bingo:
        if self.table[0] == -1 and self.table[1] == -1 and self.table[2] == -1:
            self.bingo = True
        elif self.table[3] == -1 and self.table[4] == -1 and self.table[5] == -1:
            self.bingo = True
        elif self.table[6] == -1 and self.table[7] == -1 and self.table[8] == -1:
            self.bingo = True
    # *****Diadonals*****
    if not self.bingo:
        if self.table[0] == -1 and self.table[4] == -1 and self.table[8] == -1:
            self.bingo = True
        elif self.table[2] == -1 and self.table[4] == -1 and self.table[6] == -1:
            self.bingo = True
    if testing:
        if self.bingo: print(self.name, 'has a bingo!')
    return self.bingo

  def check_bingo_full(self):
      full = True
      for num in range(9):
          if self.table[num] != -1: full = False
      self.full_bingo = full
      return

  def table_print_all(self):
    if testing:
        print(self.table)
    else:
        print(self.table[0], self.table[1], self.table[2])
        print(self.table[3], self.table[4], self.table[5])
        print(self.table[6], self.table[7], self.table[8])


  def set_name(self, name):
      self.name = name

  def name_back(self):
      return self.name

def naming():
    for x in range(0,num_players):
        if testing:
            p[x] = Player(x, 'player ' + str(x+1))
        else:
            print('player ', x + 1, ' name:')
            p[x] = Player(x, input())

def print_tables():
    table_print = ['','','','','']
    for x in range(0,num_players):
        table_print[0] += (' ' + PrintColors.BOLD + p[x].name_back() + PrintColors.END_C + ':' + (17 - len(p[x].name_back())) * ' ')
        table_print[4] += ('|--------------|' + (3 * ' '))
        for y in range(0,3):
            table_print[1] += '| '
            if p[x].table_get(y) == -1:
                table_print[1] += PrintColors.BOLD + PrintColors.COLOR_BLUE + 'X' + PrintColors.END_C
            else: table_print[1] += str(p[x].table_get(y))
            if p[x].table_get(y) >= 10:
                table_print[1] += ' '
            else: table_print[1] += '  '
            table_print[2] += '| '
            if p[x].table_get(y + 3) == -1:
                table_print[2] += PrintColors.BOLD + PrintColors.COLOR_BLUE + 'X' + PrintColors.END_C
            else: table_print[2] += str(p[x].table_get(y + 3))
            if p[x].table_get(y + 3) >= 10:
                table_print[2] += ' '
            else: table_print[2] += '  '
            table_print[3] += '| '
            if p[x].table_get(y + 6) == -1:
                table_print[3] += PrintColors.BOLD + PrintColors.COLOR_BLUE + 'X' + PrintColors.END_C
            else: table_print[3] += str(p[x].table_get(y + 6))
            if p[x].table_get(y + 6) >= 10:
                table_print[3] += ' '
            else: table_print[3] += '  '
            if y == 2:
                table_print[1] += '|   '
                table_print[2] += '|   '
                table_print[3] += '|   '
        print('')
    print(table_print[0])
    print(table_print[4])
    print(table_print[1])
    print(table_print[4])
    print(table_print[2])
    print(table_print[4])
    print(table_print[3])
    print(table_print[4])

def begin_game():
    num_players_error = True
    while num_players_error:
        print('********************************************\n'
              '*               Lets Play!                 *\n'
              '********************************************\n'
              '|------------------------------------------|\n'
              '|To roll a number|End Game| quit |New Game |\n'
              '|------------------------------------------|\n'
              '|       ' + Controls.ROLL + '        |   ' + Controls.END_GAME +
              '    |  ' + Controls.QUIT + '   |    ' + Controls.NEW_GAME + '    |\n'
              '|------------------------------------------|\n') # Game Menu
        if full_bingo_mode: print(PrintColors.BOLD + 'Lets Start Playing in FULL BINGO MODE!' + PrintColors.END_C)
        print(PrintColors.BOLD + 'how many players are playing? (max: 16)' + PrintColors.END_C)
        no_input = True
        while no_input:
            num = input()
            if not num.isdigit():
                print(PrintColors.FAIL + 'please enter a valid num' + PrintColors.END_C)
            else: no_input = False
        num = int(num)
        if num <= 16:
            num_players_error = False
        else: print(PrintColors.WARNING + 'Too many players' + PrintColors.END_C)
    return num

def randomize_num():
    num_ok = False
    while not num_ok:
        num = random.randint(0,50)
        if str(num) not in used_nums:
            num_ok = True
    return num

def play_num():
    num = randomize_num()
    # ***** Check in Tables *******
    player_has_num = ''
    player_has_num_state = False
    last_player_has = -1
    for i in range(0,num_players):
        for j in range(0,9):
            if p[i].table_get(j) == num:
                p[i].table_set(j, -1)
                player_has_num_state = True
                last_player_has = i
                if player_has_num == '': player_has_num += p[i].name
                else: player_has_num += ', ' + p[i].name
    # ***** Stats Print *******
    print_tables()
    print('The Number is:', num)
    if player_has_num_state:
        if len(player_has_num) > len(p[last_player_has].name):
            to_print = player_has_num[0:(len(player_has_num) - len(p[last_player_has].name) - 2)]
            if testing: print(to_print)
            to_print += player_has_num[(len(player_has_num) - len(p[last_player_has].name) - 2) : len(player_has_num)].replace(',', ' And')
        else: to_print = p[last_player_has].name
        print(to_print, 'Has It!')
    # ***** Check For Bingo *******
    bingo = False
    if not full_bingo_mode:
        for i in range(0,num_players):
            if p[i].bingo:
                print(PrintColors.COLOR_GREEN + p[i].name, ' Has a Bingo!' + PrintColors.END_C + '\n')
                bingo = True
    else:
        for i in range(0,num_players):
            if p[i].full_bingo:
                bingo = True
                print(PrintColors.COLOR_GREEN + p[i].name, 'Has Full Bingo!'+ PrintColors.END_C + '\n')
    if bingo:
        num = -1
    return num

def main_menu():
    print('********************************************\n'
          '*         Welcome To Bingo Game!           *\n'
          '********************************************\n'
          '|------------------------------------------|\n'
          '| to start new game  | Settings |   quit   |\n'
          '|------------------------------------------|\n'
          '|' + ' '*9 + Controls.NEW_GAME + ' '*10 + '|' + ' '*4 + Controls.SETTINGS_MENU + ' '*5 + '|' + ' '*4 + Controls.QUIT + ' '*5 + '|\n'
          '|------------------------------------------|\n'
          '| Press Back Anytime to Go to Main Menu (b)|\n'
          '|------------------------------------------|\n')
    return True

def settings_menu():
    if NO_SAME_NUMBER: same_state = PrintColors.COLOR_GREEN + 'OFF' + PrintColors.END_C
    else: same_state = PrintColors.FAIL + 'ON ' + PrintColors.END_C
    if testing: dev_state = PrintColors.FAIL + 'ON ' + PrintColors.END_C
    else: dev_state = PrintColors.COLOR_GREEN + 'OFF' + PrintColors.END_C
    if full_bingo_mode: full_bingo_state = PrintColors.FAIL + 'ON ' + PrintColors.END_C
    else: full_bingo_state = PrintColors.COLOR_GREEN + 'OFF' + PrintColors.END_C
    print('********************************************\n'
          '*                 Settings                 *\n'
          '********************************************\n'
          '| Allow Same Number | ' + same_state + ' |' + 7*' ' + Controls.NO_SAME_NUMBER_STATE  + 8*' ' + '|\n'
          '|------------------------------------------|\n'
          '| Full Bingo Mode   | ' + full_bingo_state + ' |' + 7*' ' + Controls.FULL_BINGO + 8*' ' + '|\n'
          '|------------------------------------------|\n'
          '| DEV Tools         | ' + dev_state + ' |' + 7*' ' + Controls.DEV_TOOLS + 8*' ' + '|\n'
          '|------------------------------------------|\n'
          '| Press Back Anytime to Go to Main Menu (b)|\n'
          '|------------------------------------------|\n')
    return True

def bingo_menu():
    print('********************************************\n'
          '*    Do you want to keep to full bingo?!   *\n'
          '********************************************\n'
          '|------------------------------------------|\n'
          '|    keep till full    | finish |   quit   |\n'
          '|------------------------------------------|\n'
          '|' + ' ' * 10 + Controls.KEEP_TO_FULL + ' ' * 11 + '|' + ' ' * 3 + Controls.END_GAME + ' ' * 4 + '|' + ' ' * 4 + Controls.QUIT + ' ' * 5 + '|\n'
          '|------------------------------------------|\n'
          '| Press Back Anytime to Go to Main Menu (b)|\n'
          '|------------------------------------------|\n')

p = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
used_nums = ''
testing = False
NO_SAME_NUMBER = True
play_game = False
SETTING_MENU = False
MAIN_MENU = False
BINGO_MENU = False
keep = True
full_bingo_mode = False

MAIN_MENU = main_menu()
while keep:
    data = input()
    data.lower()
    if play_game and data == Controls.ROLL:
        num_played = play_num()
        used_nums += str(num_played) + ','
        if testing: print('\nused:', used_nums, '\n')
        if num_played == -1:
            if not full_bingo_mode:
                play_game = False
                SETTING_MENU = False
                bingo_menu()
                BINGO_MENU = True
            else:
                print('Well Played!\nSee You Soon!\n\n')
                play_game = False
                full_bingo_mode = False
                SETTING_MENU = False
                MAIN_MENU = main_menu()


    elif (play_game or BINGO_MENU) and data == Controls.END_GAME:
        print('Ending game...' + '\n'*8)
        play_game = False
        SETTING_MENU = False
        BINGO_MENU = False
        MAIN_MENU = main_menu()

    elif not play_game and (data == Controls.ROLL or data == Controls.END_GAME):
        print('Not in a game...')

    elif MAIN_MENU and data == Controls.NEW_GAME:
        num_players = begin_game()
        play_game = True
        MAIN_MENU = False
        used_nums = ''
        naming()
        print_tables()

    elif data == Controls.QUIT:
        keep = False

    elif SETTING_MENU and data == Controls.DEV_TOOLS:
        if not testing:
            testing = True
        else:
            testing = False
        SETTING_MENU = settings_menu()
        MAIN_MENU = False

    elif MAIN_MENU and testing and data == Controls.SET_BINGO:
        p[0].set_bingo()

    elif MAIN_MENU and testing and data == Controls.OWNER:
        p[0].owner()

    elif MAIN_MENU and data == Controls.SETTINGS_MENU:
        SETTING_MENU = settings_menu()
        MAIN_MENU = False

    elif SETTING_MENU and data == Controls.NO_SAME_NUMBER_STATE:
        if NO_SAME_NUMBER:
            NO_SAME_NUMBER = False
        else:
            NO_SAME_NUMBER = True
        SETTING_MENU = settings_menu()
        MAIN_MENU = False

    elif (SETTING_MENU or play_game) and data == Controls.BACK:
        play_game = False
        MAIN_MENU = main_menu()
        SETTING_MENU = False

    elif BINGO_MENU and data == Controls.KEEP_TO_FULL:
        full_bingo_mode = True
        play_game = True
        BINGO_MENU = False
        print('Lets Keep on Playing!\nPress', Controls.ROLL , 'to Roll a Number!')

    elif SETTING_MENU and data == Controls.FULL_BINGO:
        if full_bingo_mode: full_bingo_mode = False
        else: full_bingo_mode = True
        SETTING_MENU = settings_menu()
        MAIN_MENU = False

    else: print('Unknown command\nPlease try again')


