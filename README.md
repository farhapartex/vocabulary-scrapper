### Vocabulary Scrapper
This is a  django app which can find out meaning of a word with example list (English to English). Someone can get the meaning of a word from the command line easily. 

#### Prerequisite
* Python >= 3.5
* Docker

#### How to use

* Open your command prompt
* To get the app, clone the repository using the command `git clone https://github.com/farhapartex/vocabulary-scrapper.git`
* Go to the folder `vocabulary-scrapper`
* For first use you have to build the app. To build type the command `docker-compose build server`
* For using the app, each time you have to run the server. To run the server type the command `docker-compose up server`
* Open another command prompt and move to the folder `vocabulary-scrapper`
* To find out meaning of a word type the command `python3 word.py your_word`. Here replace your word with `your_word` and press enter. And here it is!!

#### Output Format

* `Word` : This the word name you are searching
* `short_description` : This block will show to you a short idea on the word, you search
* `long_description` : This block will show to you a brief idea on the word, you search
* `first_definition` : This block will show to you the definition of the word, you search
* `group_definition` : This block will show definition list which also describe the word, you search
* `synonym_list` : This block will show synonyms for the word, you search

### For only scrapping

If you think, you just want to use the scrapper file then use the `scrapper-file` folder. There is a single file named `scrap.py`. Just call the method named `get_word_information` and pass your word as argument.

### Demo:

```
from scrap import get_word_information
word = "Morning"
scrap_data = get_word_information(word)
```
