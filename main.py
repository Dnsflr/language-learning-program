import random

def create_dictionary_from_file(file_path):
    dictionary = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            expressions = line.split(',')
            if len(expressions) == 2 :
                dictionary[expressions[0].strip()] = expressions[1].strip()
    return dictionary

sport_words = create_dictionary_from_file(r'path')
nature_words = create_dictionary_from_file(r'path')
town_words = create_dictionary_from_file(r'path')


def choose_set():
    print("Choose words set level: 1-Town, 2-Nature, 3-Sport")
    choice = input("Enter your choice (1/2/3): ").strip()
    if choice == '1':
        return town_words
    elif choice == '2':
        return nature_words
    elif choice == '3':
        return sport_words
    else:
        print("Invalid choice, defaulting to Town.")
        return town_words

def draw_and_ask(words):
    points = 0
    used_words = []

    for i in range(len(words)):
        chosen_word, correct_translation = random.choice(list(words.items()))
        while chosen_word in used_words:
            chosen_word, correct_translation = random.choice(list(words.items()))
        used_words.append(chosen_word)

        answer = input(f"How do you say '{chosen_word}' in English? Press q to quit ").lower().strip()
        if answer == correct_translation:
            print("Correct!")
            points += 1
        elif answer == "q":
            break
        else:
            print(f"Wrong. The correct answer is: {correct_translation}")

    return points


words = choose_set()
points = draw_and_ask(words)
print("Koniec! twój wynik to:",points)
input()