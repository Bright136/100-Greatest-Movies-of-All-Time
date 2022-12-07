import requests
from bs4 import BeautifulSoup

# create a request
response = requests.get('https://www.empireonline.com/movies/features/best-movies-2/')

# convert the  response from the site into text
contents = response.text

# create a soup with an html parser
soup = BeautifulSoup(contents, 'html.parser')

# get the names of the movies from the site using their html tags and classes
titles_list = soup.find_all(name='img', class_="jsx-952983560")
movies = [title.get('alt') for title in titles_list]
movies = movies[1:]
movies.reverse()

# save the names of the movies in a .txt file
for index, movie in enumerate(movies, 1):
    with open('movies.txt', mode='w', encoding='utf-8') as file:
        file.write(f'{index}. {movie} \n')
print(len(movies))