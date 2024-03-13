#The game board lay-out and display
board_values = {'A1':' ', 'A2':' ', 'A3':' ', 'B1':' ', 'B2':' ', 'B3':' ', 'C1':' ', 'C2':' ', 'C3':' '}
w = '  '
x = '**'
y = '*' *19
z = ' '*5

def board_display():
    print(' ' * 5 + 'A' + z + 'B' + z + 'C')
    print('  ' + y)
    print(f'1 *{w}{board_values["A1"]}{w}|{w}{board_values["B1"]}{w}|{w}{board_values["C1"]}{w}*')
    print('  ' + y)
    print(f'2 *{w}{board_values["A2"]}{w}|{w}{board_values["B2"]}{w}|{w}{board_values["C2"]}{w}*')
    print('  ' + y)
    print(f'3 *{w}{board_values["A3"]}{w}|{w}{board_values["B3"]}{w}|{w}{board_values["C3"]}{w}*')
    print('  ' + y)

#A function to reset the board
def board_reset():
    board_values['A1'] = ' '
    board_values['A2'] = ' '
    board_values['A3'] = ' '
    board_values['B1'] = ' '
    board_values['B2'] = ' '
    board_values['B3'] = ' '
    board_values['C1'] = ' '
    board_values['C2'] = ' '
    board_values['C3'] = ' '

#Letting the player select a colom and row
#Check if the player gives a valid input
def choice_colom():
    colom = ['A', 'B', 'C']
    switch_colom = True
    
    while switch_colom:
        choice_colom = input('Please choose your Colom (A-B-C): ')
        choice_colom = choice_colom.upper()
        
        if choice_colom.isdigit() == False: 
        
            if choice_colom in colom:
                return str(choice_colom)
            
            else:
                print('This is not a letter in the given range, please try again.')
    
        else:
            print('This is not a valid letter, please try again.')


def choice_row():
    row = [1,2,3]
    switch_row = True
    
    while switch_row:
        choice_row = input('Please choose your Row (1-2-3): ')
        
        if choice_row.isdigit():
            choice_row = int(choice_row)
        
            if choice_row in row:
                return str(choice_row)
            
            else:
                print('This is not a number in the given range, please try again.')
    
        else:
            print('This is not a valid number, please try again.')

#Check which player is playing
#Check if the player gives a valid input
def choice_player():
    player = ['X', 'O']
    switch_player = True
    
    while switch_player:
        choice_player = input('Are you playing as X or O? ')
        choice_player = choice_player.upper()
        
        if choice_player.isdigit() == False: 
        
            if choice_player in player:
                return str(choice_player)
            
            else:
                print('This is not a player, please try again.')
    
        else:
            print('This is not a valid letter, please try again.')

#Option to stop the game after a game has been played
def game_off():
    stop = ['Y', 'N']
    switch_stop = True
    
    while switch_stop:
        game_off = input('Do you want to stop the game? (Y/N): ')
        game_off = game_off.upper()
        
        if game_off.isdigit() == False: 
        
            if game_off in stop:
                
                if game_off == 'Y':
                    return False
                
                elif game_off == 'N':
                    return True
            
            else:
                print('This is not a letter in the given range, please try again.')
    
        else:
            print('This is not a valid letter, please try again.')

#Function to check the winner
def win_check(a):
    
    if board_values['A1'] == a and board_values['B1'] == a and board_values['C1'] == a:
        print(f'Congrats {a} is the winner!')
        board_display()
        return True
    
    elif board_values['A1'] == a and board_values['A2'] == a and board_values['A3'] == a:
        print(f'Congrats {a} is the winner!')
        board_display()
        return True
    
    elif board_values['A2'] == a and board_values['B2'] == a and board_values['C2'] == a:
        print(f'Congrats {a} is the winner!')
        board_display()
        return True
    
    elif board_values['B1'] == a and board_values['B2'] == a and board_values['B3'] == a:
        print(f'Congrats {a} is the winner!')
        board_display()
        return True
    
    elif board_values['A3'] == a and board_values['B3'] == a and board_values['C3'] == a:
        print(f'Congrats {a} is the winner!')
        board_display()
        return True
    
    elif board_values['C1'] == a and board_values['C2'] == a and board_values['C3'] == a:
        print(f'Congrats {a} is the winner!')
        board_display()
        return True
    
    elif board_values['A1'] == a and board_values['B2'] == a and board_values['C3'] == a:
        print(f'Congrats {a} is the winner!')
        board_display()
        return True
        
    elif board_values['A3'] == a and board_values['B2'] == a and board_values['C1'] == a:
        print(f'Congrats {a} is the winner!')
        board_display()
        return True
    
    else:
        return False

#Function to check if the board is full
def full_board_check():
    
    if ' ' not in board_values.values():
        board_display()
        print("The board is full, so it's a tie!")
        board_reset()
        return True
    
    else:#
        return False

#Combining all the previous functions, to turn the game on
def game_on():
    game_on = True
    
    while game_on:
    
        board_display()
        colom = choice_colom()
        row = choice_row()
        player = choice_player()
    
        if board_values[colom+row] == ' ':
            board_values[colom+row] = player
        
        elif board_values[colom+row] != ' ':
            print('This is not an empty space, please choose again.')
            continue
        
        if win_check('X'):
            board_reset()
            game_on = game_off()
        
        elif win_check('O'):
            board_reset()
            game_on = game_off()
        
        elif full_board_check():
            game_on = game_off()

#To start the game, uncomment the next line
#game_on()
