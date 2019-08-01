from bs4 import BeautifulSoup
import requests


def get_inner_text(data):
    data = data.find("h3", attrs={"class": "definition"})
    data.a.decompose()
    data = data.text.strip()

    return data


def get_group_text_list(groups):
    data_list = []
    for g in groups:
        data = get_inner_text(g)
        data_list.append(data)
    return data_list


def get_synoname_list(data):
    s_list = []
    data = data.find("dl", attrs={"class": "instances"})
    data = data.find("dd")
    data = data.find_all("a")
    for a in data:
        s_list.append(a.text)

    return s_list


def get_word_information(word=None):
    data_object = {}
    url = 'https://www.vocabulary.com/dictionary/{0}'

    if word:
        url = url.format(word)
        req = requests.get(url)
        response = req.text
        soup = BeautifulSoup(response, "html.parser")
        if len(soup.select("p[class='short']")) > 0:
            short_description = soup.select("p[class='short']")[0].text
            long_description = soup.select("p[class='long']")[0].text

            groups = soup.find("div", attrs={"class": "group"})
            groups = groups.find_all("div", attrs={"class": "ordinal"})

            definition = groups[0]
            definition = get_inner_text(definition)

            groups = get_group_text_list(groups[1:])

            syn_list_data = soup.find("div", attrs={"class": "defContent"})
            syn_list = get_synoname_list(syn_list_data)

            data_object = {'main_word': word,
                           'short_description': short_description, 'long_description': long_description, "first_definition": definition, "group_definition": groups, "synonym_list": syn_list}
        else:
            data_object = {
                'message': "The word you are searching, is not found!"}

        #examples = soup.find("div",attrs={"class":"results"})

    return data_object
