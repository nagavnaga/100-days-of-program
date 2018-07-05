import csv
import os
import statistics
import urllib.request
from data_structure import Movies
from collections import Counter, defaultdict

logfile = os.path.join(r'C:\Program Files\JetBrains\my codes\100 days of coding\collections', 'movie.csv')
url = 'https://raw.githubusercontent.com/sundeepblue/movie_rating_prediction/master/movie_metadata.csv'


def converting_csvfile_listofmovies(logfile):
    movies = []
    with open(logfile, 'r', encoding='utf-8') as fin:
        for row in csv.DictReader(fin):
            movies.append(Movies.create_from_dict(row))
            # movies.append(m)
    return movies


def download_file(url_link, file_path):
    urllib.request.urlretrieve(url_link, file_path)


def get_movies_by_directors(movies_list):
    d_list = defaultdict(list)
    for movie in movies_list:
        d_list[movie.director_name].append(movie)

    return d_list


def get_number_of_movies_by_director(directors):
    cnt = Counter()
    for director, movie in directors.items():
        if director:
            cnt[director] = len(movie)

    return cnt


def filtered_dir(directors):
    directors_after_filter = defaultdict(list)

    for director, movie in directors.items():
        for eachmovie in movie:
            try:
                if director and int(eachmovie.year) >= 1960 and get_number_of_movies_by_director(directors)[director] >= 4:
                    directors_after_filter[director].append(eachmovie)
            except ValueError:
                continue

    return directors_after_filter


def get_average_score(selected_directors):
    average_score = defaultdict()
    for director, movie in selected_directors.items():
        average_score[director] = get_mean(movie)
    return average_score


def get_mean(movies):
    score = []
    for movie in movies:
        score.append(float(movie.imdb_score))
    mean = round(statistics.mean(score), 1)

    return mean


def print_output(selcted_dir, average_score):
    cnt=1
    for dir, avg in average_score:
        print(cnt, '.', dir, '' * 10, avg)
        print('-' * 50)
        movies = selcted_dir[dir]
        for movie in movies:
            print(movie.year, movie.movie_title, movie.imdb_score)
        cnt +=1


if __name__ == '__main__':
    movies_list = converting_csvfile_listofmovies(logfile)
    directors = get_movies_by_directors(movies_list)
    selected_dir = filtered_dir(directors)
    average_imdb_score = Counter(get_average_score(selected_dir)).most_common(5)
    print_output(selected_dir, average_imdb_score)
