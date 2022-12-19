import main

if __name__ == '__main__': 
    print("Play with a bot?Input 'Y' for YES, or else for NO")
    answer = input()
    if 'y' == answer or 'Y' == answer:
        # bot player & human player(case 1&2): 
        print("Play first/ take 'O'? Input 'Y' for YES, or else for NO")
        answer = input()
        if 'y' == answer or 'Y' == answer:
            #case 1: U play first, bot goes second
            print("what is your name?")
            Player1_name = input ()
            Player2_name = "bot" # is it ok to write so many commands in one function?
            game = main.Game(main.HumanPlayer(), main.BotPlayer())
            

        else:
            #case 2: Bot plays first, human player goes second:
            print("what is your name?")
            Player1_name = "bot"
            Player2_name = input ()
            game = main.Game(main.BotPlayer(), main.HumanPlayer())
            
    else:
        # It's a human x human game(case 3):
        print("what the name of first player?")
        Player1_name = input ()
        print("what's the name of the second player?")
        Player2_name = input()
        game = main.Game(main.HumanPlayer(), main.HumanPlayer())
    
    
        


    # Game starts!
    game.run()