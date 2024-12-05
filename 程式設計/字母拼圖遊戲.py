import random

def load_words():
    # 載入單字列表，可以從檔案中載入或直接定義一個列表
    return ["example", "puzzle", "python", "programming", "computer"]

def shuffle_word(word):
    # 將單字打亂順序
    word = list(word)
    random.shuffle(word)
    return ''.join(word)

def play_game():
    # 載入單字列表
    words = load_words()
    # 隨機選擇一個單字
    word_to_guess = random.choice(words)
    # 將選擇的單字打亂順序
    shuffled_word = shuffle_word(word_to_guess)
    # 設定猜測次數
    attempts = 5

    print("Welcome to the Letter Puzzle Game!")
    print(f"Here is your puzzle: {shuffled_word}")

    # 開始遊戲循環
    while attempts > 0:
        # 讓玩家輸入猜測的單字
        guess = input("Your guess: ")
        if guess == word_to_guess:
            # 如果猜對了，顯示祝賀訊息並結束遊戲
            print("Congratulations! You've guessed the word correctly.")
            return
        else:
            # 如果猜錯了，減少一次猜測機會並提示剩餘次數
            attempts -= 1
            print(f"Incorrect guess. You have {attempts} attempts left.")

    # 如果用完所有猜測次數，顯示正確答案
    print(f"Game over! The correct word was: {word_to_guess}")

if __name__ == "__main__":
    # 開始遊戲
    play_game()