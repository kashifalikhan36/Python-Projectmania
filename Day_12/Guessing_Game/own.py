import random

print(
    """  ________                            .__                   ________                       
 /  _____/ __ __   ____   ______ _____|__| ____    ____    /  _____/_____    _____   ____  
/   \  ___|  |  \_/ __ \ /  ___//  ___/  |/    \  / ___\  /   \  ___\__  \  /     \_/ __ \ 
\    \_\  \  |  /\  ___/ \___ \ \___ \|  |   |  \/ /_/  > \    \_\  \/ __ \|  Y Y  \  ___/ 
 \______  /____/  \___  >____  >____  >__|___|  /\___  /   \______  (____  /__|_|  /\___  >
        \/            \/     \/     \/        \//_____/           \/     \/      \/     \/ """
)


def no_gen():
    k = 0
    k = random.randint(0, 100)
    return k


def guess_count(guess, comp_unit, end):
    global make_guess
    make_guess = int(input("Make a guess:"))
    if guess == 0:
        print("Game_over")
    else:
        if make_guess < comp_unit:
            print("too low")
            print("Guess Again")
            guess -= 1
            return end

        elif make_guess > comp_unit:
            print("too high")
            print("Guess Again")
            guess -= 1
            return end
        elif make_guess == comp_unit:
            print("U win")
            end = 1
            return end


end = 0
dif = input("Choose the dif : Hard, Easy :-").lower()
guess = 0
comp_unit = 0
while end == 0:
    if dif == "hard":
        guess = 5
        comp_unit = no_gen()
        end = guess_count(guess, comp_unit, end)
    elif dif == "easy":
        guess = 10
        comp_unit = no_gen()
        end = guess_count(guess, comp_unit, end)