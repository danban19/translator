import requests
from bs4 import BeautifulSoup

class Translator:

    def __init__(self):
        print('''Hello, you're welcome to the translator. Translator supports: 
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
13. Turkish''')

    def greetings(self):
        self.first_language = input("Type the number of your language:\n")
        self.second_language = input("Type the number of a language you want to translate to or '0' to translate to all languages:\n")
        self.word = input("Type the word you want to translate:\n")
        self.languages = {'1':'Arabic', '2':'German', '3': 'English', '4':'Spanish', '5':'French',
                          '6':'Hebrew', '7':'Japanese','8': 'Dutch', '9': 'Polish', '10': 'Portuguese',
        '11':'Romanian', '12': 'Russian', '13': 'Turkish'}
        if self.second_language == '0':
            self.multitranslation()
        else:
            self.single_translation()

    def single_translation(self):
        page = f'https://context.reverso.net/translation/{self.languages.get(self.first_language).lower()}-' \
               f'{self.languages.get(self.second_language).lower()}/{self.word}'
        user_agent = 'Mozilla/5.0'
        r = requests.get(page, headers={'User-Agent': user_agent})
        soup = BeautifulSoup(r.content, 'html.parser')
        if r.status_code == 200:
            print(r.status_code, 'OK\n')
        translations = [p.text for p in soup.find_all('a', class_='translation')]
        examples = [p.text for p in soup.find_all('div', class_='ltr')]
        translate_file = open(f'{self.word}.txt', 'w', encoding='utf-8')

        print(f'{self.languages.get(self.second_language)} Translations:')
        translate_file.write(f'{self.languages.get(self.second_language)} Translations:')
        translate_file.write('\n')
        for i in range(1, len(translations)):
            print(translations[i].strip())
            translate_file.write(translations[i].strip())
            translate_file.write('\n')
        translate_file.write('\n\n')
        print('\n')

        print(f'{self.languages.get(self.second_language)} Example:')
        translate_file.write(f'{self.languages.get(self.second_language)} Example:')
        translate_file.write('\n')
        for i in range(1, len(examples)):
            print(examples[i].strip())
            translate_file.write(examples[i].strip())
            translate_file.write('\n')
            if i % 2 == 0:
                print('\n')
                translate_file.write('\n\n')
        print('\n')
        translate_file.write('\n\n')
        translate_file.close()

    def multitranslation(self):
        user_agent = 'Mozilla/5.0'
        translate_file = open(f'{self.word}.txt', 'w', encoding='utf-8')
        for element in self.languages.values():
            page = f'https://context.reverso.net/translation/{self.languages.get(self.first_language).lower()}-' \
                   f'{element.lower()}/{self.word}'
            r = requests.get(page, headers={'User-Agent': user_agent})
            soup = BeautifulSoup(r.content, 'html.parser')
            translations = [p.text for p in soup.find_all('a', class_='translation')]
            examples = [p.text for p in soup.find_all('div', class_='ltr')]

            print(f'{element} Translations:')
            translate_file.write(f'{element} Translations:')
            translate_file.write('\n')
            for i in range(1, len(translations)):
                print(translations[i].strip())
                translate_file.write(translations[i].strip())
                translate_file.write('\n')
            translate_file.write('\n\n')
            print('\n')

            print(f'{element} Example:')
            translate_file.write(f'{element} Example:')
            translate_file.write('\n')
            for i in range(1, len(examples)):
                print(examples[i].strip())
                translate_file.write(examples[i].strip())
                translate_file.write('\n')
                if i % 2 == 0:
                    print('\n')
                    translate_file.write('\n\n')
            print('\n')
            translate_file.write('\n\n')
        translate_file.close()

translate = Translator()
translate.greetings()
