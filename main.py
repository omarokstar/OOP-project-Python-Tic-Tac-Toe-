import os 
def clear_screen():
 os.system("cls" if os.name == 'nt' else 'clear')
  
class player:
    def __init__(self):
        self.name=""
        self.symbol=""
    def choose_name(self):
        while True:
            name=input("Enter your name: ")
            if name.isalpha():
                self.name=name
                break
            print("Invalid name. Please use only letters.")
    def choose_symbol(self):
        while True:
            symbol=input("Choose your symbol (X or O): ").upper()
            if symbol in ['X', 'O'] and len(symbol) == 1:
                self.symbol=symbol.upper()
                break
            print("Invalid symbol. Please choose X or O.")




class Menu:
    def display_main_menu(self):
        print("Welcome Okstar Tic Tac Toe Game!")
        print("1. Start Game")
        print("2. Exit")
        choice = input("Enter your choice: ")
        return choice          

    def display_endgame_menu(self):
        print("Game Over!")
        print("1. Play Again")
        print("2. Exit")
        choice = input("Enter your choice: ")
        return choice 

    def validate_choice(self, choice, valid_choices):
        if choice in valid_choices:
            return True
        else:
            print("Invalid choice. Please try again.")
            return False   
        
class Board:
    def __init__(self):
       self.board=[]
       for i in range(1,10):
           self.board.append(str(i))

    def display_board(self):
        print("\nCurrent Board:")
        for i in range(0,9,3):
         print('|'.join(self.board[i:i+3]))
         if i < 6:
            print('-' * 5)

    def update_board(self, choice, symbol):
        if self.is_valid_move(choice):
            self.board[int(choice) - 1] = symbol
            return True
        else:
           return False
        

    def is_valid_move(self,choice):
        return self.board[choice-1].isdigit()


    def reset_board(self):
        self.board = [str(i) for i in range(1, 10)]


class Game:

    def __init__(self):
        self.players = [player(), player()]
        self.board = Board()
        self.menu = Menu()
        self.current_player_index = 0

    def start_game(self):
        choice=self.menu.display_main_menu()
        if choice == '1':
            self.setup_players()
            self.play_game()
        else:
            self.quit_game()



    def setup_players(self):
        symbols_chosen = set()
        for i, player in enumerate(self.players, start=1):
            print(f"Player {i}:")
            player.choose_name()
            while True:
                player.choose_symbol()
                if player.symbol in symbols_chosen:
                    print("Symbol already taken. Choose the other one.")
                else:
                    symbols_chosen.add(player.symbol)
                    break
            clear_screen()


    def play_game(self):
        while True:
            self.play_turn()

            if self.check_win() or  self.check_draw():
                choice = self.menu.display_endgame_menu()
                if choice == '1':
                    self.restart_game()
                else:    
                    self.quit_game()  
                    break

    def restart_game(self):
        self.board.reset_board()
        self.current_player_index = 0
        self.play_game() 

            
    def check_win(self):
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  
            [0, 3, 6], [1, 4, 7], [2, 5, 8], 
            [0, 4, 8], [2, 4, 6]             
        ]
        for combination in win_combinations:
            if (self.board.board[combination[0]] == self.board.board[combination[1]] == 
                self.board.board[combination[2]] and 
                self.board.board[combination[0]]  in ['X', 'O']):
                print(f"Player {self.players[self.current_player_index].name} wins!")
                return True
        return False 
    
    def check_draw(self):
        return all (not cell.isdigit() for cell in self.board.board)
    
    
    def play_turn(self):
        player = self.players[self.current_player_index] 
        self.board.display_board()
        print(f"{player.name}'s turn ({player.symbol})")
        while True:
            try:
               cell_choice=int(input("choose a cell (1-9): "))
               if 1 <= cell_choice <= 9 and self.board.update_board(cell_choice, player.symbol):

                    break
               else: 
                    print("Invalid choice. Please choose a valid cell.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 9.")          
        self.switch_player()
        clear_screen()


    
    def switch_player(self):
       self.current_player_index=1- self.current_player_index 


    def quit_game(self):
        print("Thank you for playing! Goodbye!")   




game=Game()
game.start_game()    