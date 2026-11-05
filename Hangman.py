import random;
secret_key = ["apple", "banana", "orange", "paris", "french"];
word = random.choice(secret_key);
hidden_word = "_" * len(word);
size = len(word);
for i in range(size):
    print("_", end="");
guess_count = 5;
print(f"\n\n-----You have {guess_count} Guesses to Win the game-----")
print("You will not lose Guess if the guess is correct\n")
while guess_count != 0:
    guess_count -= 1
    guess = input("enter your guess:")
    if guess in hidden_word:
        print(f"You have already guessed {guess}")
    elif guess in word:
        guess_count += 1
        target = list(hidden_word)
        index = 0
        for i, val in enumerate(word):
            index = i
            if val == guess:
                target[index] = guess
        hidden_word = "" . join(target)
    else:
        print("Wrong guess")

    print(f"Hidden word: {hidden_word}")
    print(f"Guesses left: {guess_count}")
    if word == hidden_word:
        break;
    
if word == hidden_word and guess_count != 0:
    print(f"\n-----you win!----- \n your word is: {hidden_word}");
else:
    print(f"\n-----You lose!----- \n Your word was: {word}");
            

