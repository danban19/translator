import requests
import sys
from bs4 import BeautifulSoup


class Translator:

    def __init__(self, arguments):
        self.greets = '''Hello, you're welcome to the translator. Translator supports: 
1. Arabic
2. German
3. English
4. Spanish
5. French
6. Hebrew
7. Japanese
8. Dutch
9. Polish
10. Portuguese
11. Romanian
12. Russian
13. Turkish\n'''
        self.languages = ['Arabic', 'German', 'English', 'Spanish', 'French', 'Hebrew', 'Japanese', 'Dutch',
                          'Polish', 'Portuguese', 'Romanian', 'Russian', 'Turkish', 'All']
        self.arguments = arguments
        self.first_language = str(self.arguments[1]).capitalize()
        self.second_language = str(self.arguments[2]).capitalize()
        self.word = str(self.arguments[3])
        self.translate_file = open(f'{self.word}.txt', 'w', encoding='utf-8')
        self.input_check()

    def input_check(self):  # checks if input languages and word are valid
        try:
            self.languages.index(self.first_language)
        except ValueError:
            print(f"Sorry, the program doesn't support {self.first_language.lower()}")
            sys.exit()
        try:
            self.languages.index(self.second_language)
        except ValueError:
            print(f"Sorry, the program doesn't support {self.second_language.lower()}")
            sys.exit()
        else:
            self.translation_choice()

    def translation_choice(self):
        if self.second_language == '0' or self.second_language == 'All':
            self.multi_translation(self.first_language, self.word)
        else:
            print(self.greets)
            self.translate_file.write(f'{self.greets}\n')
            self.single_translation(self.first_language, self.second_language, self.word)

    def url_scrapper(self, first_language, second_language, word):  # scraps the website, checks connection
        page = f'https://context.reverso.net/translation/{first_language.lower()}-' \
               f'{second_language.lower()}/{word}'
        user_agent = 'Mozilla/5.0'
        r = requests.get(page, headers={'User-Agent': user_agent})
        soup = BeautifulSoup(r.content, 'html.parser')
        translations = [p.text for p in soup.find_all('a', class_='translation')][1:]
        examples = [p.text for p in soup.find_all('div', class_='src ltr')]
        try:
            if r.status_code == 404:
                raise ValueError
            elif r.status_code != 200:
                raise ConnectionError
        except ValueError:
            print(f'Sorry, unable to find {self.word}')
            sys.exit()
        except ConnectionError:
            print('Something wrong with your internet connection')
            sys.exit()
        else:
            return translations, examples, r.status_code

    def single_translation(self, first_language, second_language, word):
        translation_soup = self.url_scrapper(first_language, second_language, word)
        translations = translation_soup[0]
        examples = translation_soup[1]
        print(f'\n{second_language} Translations:')
        print(f'\n{second_language} Translations:', file=self.translate_file)
        length_tr = 3 if len(translations) > 3 else len(translations)
        length_ex = 3 if len(examples) > 3 else len(examples)
        for i in range(length_tr):
            print(translations[i].strip(), end='\n')
            print(translations[i].strip(), end='\n', file=self.translate_file)
        print(f'\n{second_language} Example:')
        print(f'\n{second_language} Example:', file=self.translate_file)
        for i in range(1, length_ex):
            print(examples[i].strip(), end='\n')
            print(examples[i].strip(), end='\n', file=self.translate_file)

    def multi_translation(self, first_language, word):
        # iterates through all the languages using for loop and single_translation method
        print(self.greets)
        print(self.greets, file=self.translate_file)
        for element in self.languages[:-1]:
            self.single_translation(first_language, element, word)
        self.translate_file.close()
        sys.exit()


translation = Translator(sys.argv)
translation.input_check()
