import requests
from bs4 import BeautifulSoup
from googletrans import Translator

# Создаём объект переводчика
translator = Translator()

# Функция для получения английских слов и их определения
def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)

        # Создаём объект Soup
        soup = BeautifulSoup(response.content, "html.parser")
        # Получаем слово
        english_words = soup.find("div", id="random_word").text.strip()
        # Получаем описание слова
        word_definition = soup.find("div", id="random_word_definition").text.strip()

        # Переводим слово и его определение на русский
        translated_word = translator.translate(english_words, dest='ru').text
        translated_definition = translator.translate(word_definition, dest='ru').text

        # Возвращаем результаты
        return {
            "english_words": translated_word,
            "word_definition": translated_definition
        }
    except Exception as e:
        print(f"Произошла ошибка: {e}")


# Функция для самой игры
def word_game():
    print("Добро пожаловать в игру")
    while True:
        # Используем результат функции-словаря
        word_dict = get_english_words()
        word = word_dict.get("english_words")
        word_definition = word_dict.get("word_definition")

        # Начинаем игру
        print(f"Значение слова - {word_definition}")
        user = input("Что это за слово? ")
        if user == word:
            print("Все верно!")
        else:
            print(f"Ответ неверный, было загадано это слово - {word}")

        # Возможность закончить игру
        play_again = input("Хотите сыграть еще раз? y/n")
        if play_again != "y":
            print("Спасибо за игру!")
            break


# Запуск игры
word_game()
