import psycopg2
from psycopg2 import Error

def create_table_ex02_movies():
    try:
        connection = psycopg2.connect(user="djangouser",
                                        password="secret",
                                        host="127.0.0.1",
                                        port="5432",
                                        database="djangotraining")
        cursor = connection.cursor()
        query_create_table = '''CREATE TABLE    IF NOT EXISTS      ex02_movies
                                    (EPISODE_NB INT PRIMARY KEY  NOT NULL,
                                    TITLE          VARCHAR(64)      NOT NULL,
                                    OPENING_CRAWL   TEXT,
                                    DIRECTOR        VARCHAR(32)      NOT NULL,
                                    PRODUCER        VARCHAR(128)     NOT NULL,
                                    RELEASE_DATE    DATE             NOT NULL);'''
        cursor.execute(query_create_table) 
        connection.commit()
        response = "OK"
    except (Exception, Error) as error:
        response = error
        connection = False
    finally:
        if connection:
            cursor.close()
            connection.close()
        return response


def fill_table_ex02_movies():
    response = list()
    ex02_movies = fill_data()
    postgres_insert_query = """ INSERT INTO ex02_movies (EPISODE_NB, TITLE, DIRECTOR, PRODUCER, RELEASE_DATE)
                                       VALUES (%s,%s,%s,%s,%s)"""
    try:
        connection = psycopg2.connect(user="djangouser",
                                        password="secret",
                                        host="127.0.0.1",
                                        port="5432",
                                        database="djangotraining")
        cursor = connection.cursor()
        for movie in ex02_movies:
            try:
                record_to_insert = (movie['episode_nb'], movie['title'], movie['director'], movie['producer'], movie['release_date'])
                cursor.execute(postgres_insert_query, record_to_insert)
                connection.commit()
                response.append("OK")
            except (Exception, Error) as error:
                response.append(error)
    except (Exception, Error) as error:
        response = error
        connection = False
    finally:
        if connection:
            cursor.close()
            connection.close()
        return response



def add_to_dict(episode_nb, title, director, producer, release_date):
    movie = dict()
    movie["episode_nb"] = episode_nb
    movie["title"] = title
    movie["director"] = director
    movie["producer"] = producer
    movie["release_date"] = release_date
    return movie

def fill_data():
    ex02_movies = list()
    movie = dict()
    ex02_movies.append(add_to_dict(1, "The Phantom Menace", "George Lucas", "Rick McCallum", "1999-05-19"))
    ex02_movies.append(add_to_dict(2, "Attack of the Clones", "George Lucas", "Rick McCallum", "2002-05-16"))
    ex02_movies.append(add_to_dict(3, "Revenge of the Sith", "George Lucas", "Rick McCallum", "2005-05-19"))
    ex02_movies.append(add_to_dict(4, "A New Hope", "George Lucas", "Gary Kurtz, Rick McCallum", " 1977-05-25"))
    ex02_movies.append(add_to_dict(5, "The Empire Strikes Back", "Irvin Kershner", "Gary Kurtz, Rick McCallum", "1980-05-17"))
    ex02_movies.append(add_to_dict(6, "Return of the Jedi", "Howard G. Kazanjian, George Lucas, Rick McCallum", "Richard Marquand", "1983-05-25"))
    ex02_movies.append(add_to_dict(7, "The Force Awakens", "J. J. Abrams", "Kathleen Kennedy, J. J. Abrams, Bryan Burk", "1983-05-25"))
    return ex02_movies

# if __name__ == '__main__':
#     print(fill_data())


# <td>{{ movie[0][0] }}</td>
#             <td>{{ movie[0][1] }}</td>
#             <td>{{ movie[0][2] }}</td>
#             <td>{{ movie[0][3] }}</td>
#             <td>{{ movie[0][4] }}</td>
#             <td>{{ movie[0][5] }}</td>