from bs4 import BeautifulSoup
import requests
import sqlite3
import random


def database_connection(path):
	conn = sqlite3.connect('%smemriseDeutsch.db' %path)
	print 'Database is available!'
	cursor = conn.cursor()
	conn.execute('''CREATE TABLE IF NOT EXISTS memriseDe(id integer primary key autoincrement, word text, meaning text, example text)''')
	return conn


def text_take():
    c = database_connection('')
    resp = []
    for i in range(1, 203, 1): # 10-13
        quote_page = 'https://www.memrise.com/course/920/5000-german-words-top-87/' + str(i)
        resp.append(requests.get(quote_page))
    for respItem in resp:
        if respItem.status_code != 200:
            raise ValueError('Error accured!')
        if respItem.status_code == 200:
            soup = BeautifulSoup(respItem.content, 'html.parser')
            wordsList = soup.find('div', attrs={'id': 'content'}).find_all('div', attrs={'class': 'thing text-text'})
        for word in wordsList:
            w = word.find('div', attrs={'class': 'col_a col text'}).find('div', attrs={'class': 'text'}).text.strip()
            meaning = word.find('div', attrs={'class': 'col_b col text'}).find('div', attrs={'class': 'text'}).text.strip()
            c.execute("insert into memriseDe values (?, ?, ?, ?)", (None, w, meaning, None))
            c.commit()


def text_get():
    # text_take()
    c = database_connection('')
    wm = {}
    for word, meaning in c.execute('SELECT word, meaning from memriseDe;'):
        wm[word] = meaning
    print len(wm)
    return wm
        