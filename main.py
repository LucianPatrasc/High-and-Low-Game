#display art
from art import logo , vs
from game_data import data
import random

def format_data(account):
    """Extrage detele din cont si le returneaza printate"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name} este {account_descr} originar din {account_country}"

def check_answer(user_guess, a_followers, b_followers):
    if a_followers > a_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:

    #genereaza un cont random din lista
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compara A : {format_data(account_a)}.")
    print(vs)
    print(f"Compara B : {format_data(account_b)}")
    print()


    #intreaba jucatorul sa ghiceasca
    guess = input("Cine crezi ca este mai urmarit pe net? 'A' sau 'B' ? ").lower()
    print("\n" *20)
    print(logo)
    #verifica daca jucatorul are dreptate

    a_follower_account = account_a["follower_count"]
    b_follower_account = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_account, b_follower_account)

    if is_correct:
        score += 1
        print(f" Ai avut dreptate ! Scorul tau este {score} !")
    else:
        print(f" Nu ai avut dreptate ! scorul tau este {score} !")
        game_should_continue = False

# tine scorul


#fa jocul sa se repete daca se raspunde corect, sa il duca in runda urmatoare


#fa ca contul B sa devina locul A si el sa fie inlocuit





