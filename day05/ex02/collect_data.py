import psycopg2
from psycopg2 import Error


def collect_data_from_table():
    try:
        connection = psycopg2.connect(user="djangouser",
                                        password="secret",
                                        host="127.0.0.1",
                                        port="5432",
                                        database="djangotraining")
        cursor = connection.cursor()
        sql_select_query = """SELECT * FROM ex02_movies"""
        cursor.execute(sql_select_query) 
        # record_list = cursor.fetchall()
        # record = list_to_dict_table(record_list)
        desc = cursor.description
        record = [
            dict(zip([col[0] for col in desc], row))
            for row in cursor.fetchall()
        ]
    except (Exception, Error) as error:
        connection = False
    finally:
        if connection:
            cursor.close()
            connection.close()
        return record



# if __name__ == '__main__':
#     collect_data_from_table()