import psycopg2
from psycopg2 import Error

def try_connect():
    try:
        connection = psycopg2.connect(user="djangouser",
                                        password="secret",
                                        host="127.0.0.1",
                                        port="5432",
                                        database="djangotraining")
        cursor = connection.cursor()
        query_create_table = '''CREATE TABLE    IF NOT EXISTS      ex00_movies
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

# if __name__ == '__main__':
#     try_connect()