import random
import unittest

def generate_secret_code():
    numbers = list(range(10))
    random.shuffle(numbers)
    return numbers[:4]

def get_clues(guess, secret_code):
    if len(guess) != 4:
        return 0, 0  # 如果 guess 長度不等於 4，返回 0A0B
    
    # 計算位置和數字都正確的數量 (A)
    A = sum(1 for i in range(4) if guess[i] == secret_code[i])
    
    # 計算數字正確但位置不正確的數量 (B)
    B = sum(1 for i in range(4) if guess[i] in secret_code) - A
    
    # 返回 A 和 B 的值
    return A, B

def play_game(secret_code, attempts=10):
    print("Welcome to the 1A2B guessing game!")
    print("You have to guess the 4-digit secret code. You have {} attempts.".format(attempts))

    for attempt in range(1, attempts + 1):
        guess = input("Attempt {}: Enter your guess: ".format(attempt))
        
        if len(guess) != 4 or not guess.isdigit():
            print("Invalid input! Please enter exactly 4 digits.")
            continue
        
        guess = [int(digit) for digit in guess]

        if guess == secret_code:
            print("Congratulations! You've guessed the secret code.")
            break

        A, B = get_clues(guess, secret_code)
        print("Clues: {}A{}B".format(A, B))

    print("The secret code was: {}".format(''.join(map(str, secret_code))))

def main():
    secret_code = generate_secret_code()
    play_game(secret_code)

class Test1A2BGame(unittest.TestCase):
    def test_generate_secret_code(self):
        code = generate_secret_code()
        self.assertEqual(len(code), 4)
        self.assertEqual(len(set(code)), 4)
    
    def test_get_clues(self):
        self.assertEqual(get_clues([1, 2, 3, 4], [1, 2, 3, 4]), (4, 0))
        self.assertEqual(get_clues([1, 2, 3, 4], [4, 3, 2, 1]), (0, 4))
        self.assertEqual(get_clues([1, 2, 3, 4], [1, 3, 2, 5]), (1, 2))
        self.assertEqual(get_clues([1, 2, 3, 4], [5, 6, 7, 8]), (0, 0))
        self.assertEqual(get_clues([1, 2, 3], [1, 2, 3, 4]), (0, 0))  # Invalid guess length

if __name__ == "__main__":
    main()
    unittest.main()