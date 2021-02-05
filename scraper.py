from bs4 import BeautifulSoup
import requests
import re

substrings = input(
    'Enter substring to search for. Separate with a single comma for multiple words: ')
substrings = substrings.split(",")

output = open('quotes.txt', 'w')

for word in substrings:
    start = 'https://practicalguidetoevil.wordpress.com/2015/04/01/chapter-1-knife/'
    output.write('Instances of the word "' + word +
                 '" were found in the following chapters: \n\n')
    count = 0
    length = 0
    while True:
        source = requests.get(start).text

        soup = BeautifulSoup(source, 'lxml')

        text_ = soup.find('div', class_='entry-content')
        if text_:
            length = len(re.findall(word, text_.text, re.IGNORECASE))
            count += length
            if length > 0:
                output.write(start + ' - ' + str(length) + ' instances\n')
            print(str(count) + "\n")

        match = soup.find('div', class_='nav-next')

        if match:
            match = match.a
            start = match['href']
        else:
            output.write('A total of ' + str(count) + ' instances\n')
            break
