import random
def fight():
    health1 = 100 
    health2 = 100
    score1 = 0 
    score2 = 0
    gameStats = ["Bomb", "Medkit", "RPG", "Fire"]
    RNG1 = random.sample(gameStats,3)
    print("Player1 you got", RNG1)
    RNG2 = random.sample(gameStats,3)
    print("Player2 you got", RNG2)
    print("Player1 your score is", score1)
    print("Player2 your score is", score2)
    while True:
        print("Player1 your health is", health1)
        print("Player2 your health is", health2)
        Player1 = input("Player1, choose an item from " + str(RNG1) + ": ")
        Player2 = input("Player2, choose an item from " + str(RNG2) + ": ")
        if Player1 == "RPG":
            health2 -= 30
            print("Player2 your health is", health2)
            # Player2 = input("Player2, choose an item from " + str(RNG2) + ": ")
        elif Player1 == "Bomb":
            health2 -= 40
            print("Player2 your health is", health2)
            # Player2 = input("Player2, choose an item from " + str(RNG2) + ": ")
        elif Player1 == "Fire":
            health2 -= 10
            print("Player2 your health is", health2)
            # Player2 = input("Player2, choose an item from " + str(RNG2) + ": ")
        elif Player1 == "Medkit":
            health2 += 50
            print("Player2 your health is", health2)
            # Player2 = input("Player2, choose an item from " + str(RNG2) + ": ")
            
        if Player2 == "RPG":
            health1 -= 30
            print("Player1 your health is", health1)
            # Player1 = input("Player1, choose an item from " + str(RNG1) + ": ")
        elif Player2 == "Bomb":
            health1 -= 40
            print("Player1 your health is", health1)
            # Player1 = input("Player1, choose an item from " + str(RNG1) + ": ")
        elif Player2 == "Fire":
            health1 -= 10
            print("Player1 your health is", health1)
            # Player1 = input("Player1, choose an item from " + str(RNG1) + ": ")
        elif Player2 == "Medkit":
            health1 += 50
            print("Player1 your health is", health1)
            # Player1 = input("Player1, choose an item from " + str(RNG1) + ": ")
        
        if health1 <= 0:
            score2 += 1
            print("Player 2 won, your score is ", score2)
            print("Player 1 your score is ", score1)
            break
        if health2 <= 0:
            score1 += 1
            print("Player 1 won, your score is ", score1)
            print("Player 2 your score is ", score2)
            break
        
        
def main():
    play = fight()
    
if __name__ == "__main__":
    main()





