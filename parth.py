from bs4 import BeautifulSoup
from array import *
from requests import request
import time
import os

global filter_
global anime_input
global page
global path_file_txt
global path_file_html
anime_input=[]



page='https://animebest.org/anime/news/'
filter_=['None','Вход на сайт','Регистрация на сайте','']
path_file_txt= 'novelty.txt'
path_file_html= 'novelty.html'




def  download_page(page):
	page_txt = request('GET', page).text
	with open(path_file_html, 'w', encoding='utf-8') as f:
   		f.write(page_txt)


	
def soup_parth():
	html = open(path_file_html, encoding='utf8').read()
	soup = BeautifulSoup(html, 'lxml')

	div=soup.find_all('a')

	for a in div:
		link=a.get('title')
		link=str(link)
		if link not in filter_:
			anime_input.append(link+'\n')
	return anime_input		


def filter_up_len(anime):
	anime_out=[]
	len_anime=int(len(anime))
	number_line=1
	for i in anime:
		if i==anime[number_line]:
			anime_out.append(i)
		if number_line<len_anime-1:	
			number_line=number_line+1
	return anime_out		

	


def filter_cmotret(anime):
	#anime.pop(0)
	number=0
	for i in anime:
		number=number+1
		if 'Смотреть ' in i:
		 	anime.pop(number-1)
			
	return anime		


def filter_two_title(anime):
	len_anime=int(len(anime))
	number_line=1
	for i in anime:
		if i==anime[number_line]:
			anime.pop(number_line)
		if number_line<len_anime:
			number_line=number_line+1	
	return anime			



def dell_n(anime):
	anime_out=[]
	len_anime=int(len(anime))
	anime_line=anime[len_anime-1]
	for i in anime:
		if i!= anime_line:
			anime_out.append(i)
		else:	
			anime=[anime[len_anime-1].rstrip()]
	anime_out.append(anime[0])
	return anime_out		
		 


def write_in_file(anime):
	len_anime=len(anime)
	number_line=0
	my_file = open(path_file_txt, "w")
	for i in range(len_anime):
		number_line=number_line+1
		my_file.write(str(number_line)+') '+ anime[i])
	my_file.close()


def dell_file(path_file):
	try:
		path = os.path.join(os.path.abspath(os.path.dirname(__file__)), path_file)
		os.remove(path)
	except Exception:
		pass

	


def main():
	dell_file(path_file_txt)
	print('dell old file...')
	time.sleep(1)

	download_page(page)
	print('Download...')
	time.sleep(5)

	anime=soup_parth()
	print('Parth...')

	anime=filter_cmotret(anime)
	anime=filter_up_len(anime)
	anime=filter_two_title(anime)
	anime=dell_n(anime)
	print(anime)
	write_in_file(anime)

	time.sleep(1)
	print('dell file...')

	dell_file(path_file_html)

	
	
	

if __name__=='__main__':
	main()
