import art
import game_data
import random
import art
def competitor(first, second):
        print("Competitor A: " , first["name"], ", a" ,first["description"] , 'from' ,first["country"])
        print(art.vs)
        print("Competitor B: " , second["name"], ", a", second["description"], 'from', second["country"])
def comparison(first , second ):
    game_over = False
    score = 0

    while not game_over:
        f_follower = first["follower_count"]
        s_follower = second["follower_count"]
        answer = input("Who has more followers? Type 'A' or 'B': ").lower()
        if f_follower > s_follower and answer == 'a' :
                score += 1
                first = second
                second = random.choice(game_data.data)
                competitor(first , second)
                print(f"You are right , current score is {score}")
        elif f_follower < s_follower and answer == 'b':
            score += 1
            first = second
            second = random.choice(game_data.data)
            competitor(first, second)
            print(f"You are right , current score is {score}")
        else:
                print(f"Sorry , that's wrong your final score is {score}")
                game_over = True
print(art.logo)
A = random.choice(game_data.data)
B = random.choice(game_data.data)
competitor(A, B)
comparison(A , B)

