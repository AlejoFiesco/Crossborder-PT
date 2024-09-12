from .connection import *

def get_movie(id):
    connection = connect_db()
    cursor = connection.cursor(MySQLdb.cursors.DictCursor)
    
    query = "SELECT * FROM movie WHERE id = %s"
    cursor.execute(query, (id,))
    movie = cursor.fetchone()
    
    cursor.close()
    connection.close()
    
    return movie

def get_movie_list():
    connection = connect_db()
    cursor = connection.cursor(MySQLdb.cursors.DictCursor)
    
    query = "SELECT * FROM movie"
    cursor.execute(query)
    movies = cursor.fetchall()
    
    cursor.close()
    connection.close()
    
    return movies

def get_filtered_movie_list(q):    
    connection = connect_db()
    cursor = connection.cursor(MySQLdb.cursors.DictCursor)
    
    query = """
        SELECT * FROM movie
        WHERE name LIKE %s OR country LIKE %s
    """.format(q,q)
    
    search_pattern = f"%{q}%"
    cursor.execute(query, (search_pattern, search_pattern))
    movies = cursor.fetchall()
    
    cursor.close()
    connection.close()
    return movies

def get_filtered_sorted_movie_list(q, s, o):
    valid_columns = ['name', 'country', 'score']
    if s not in valid_columns:
        raise ValueError("Invalid column name for sorting.")
    if o not in ['ASC', 'DESC']:
        raise ValueError("Invalid order. Use 'ASC' or 'DESC'.")
    
    connection = connect_db()
    cursor = connection.cursor(MySQLdb.cursors.DictCursor)
    
    query = """
        SELECT * FROM movie
        WHERE name LIKE %s OR country LIKE %s
        ORDER BY {} {}
    """.format(s, o)
    
    search_pattern = f"%{q}%"
    cursor.execute(query, (search_pattern, search_pattern))
    movies = cursor.fetchall()
    
    cursor.close()
    connection.close()
    
    return movies

def create_movie(movie):
    connection = connect_db()
    cursor = connection.cursor()
    
    query = """
        INSERT INTO movie
        VALUES (%s, %s, %s, %s)
    """
    values = (movie['id'], movie['name'], movie['country'], movie['score'])
    cursor.execute(query, values)
    connection.commit()
    
    cursor.close()
    connection.close()
    
    return movie

def modify_movie(movie, id):
    connection = connect_db()
    cursor = connection.cursor()
    
    query = """
        UPDATE movie
        SET name = %s, country = %s, score = %s
        WHERE id = %s
    """
    values = (movie['name'], movie['country'], movie['score'], id)
    cursor.execute(query, values)
    connection.commit()
    
    cursor.close()
    connection.close()
    
    if cursor.rowcount > 0:
        return {**movie, 'id': id}
    return None

def remove_movie(id):
    connection = connect_db()
    cursor = connection.cursor()
    
    query = "DELETE FROM movie WHERE id = %s"
    cursor.execute(query, (id,))
    connection.commit()
    
    cursor.close()
    connection.close()
    
    if cursor.rowcount > 0:
        return f'{id} deleted'
    return None

def get_top_movies():
    connection = connect_db()
    cursor = connection.cursor(MySQLdb.cursors.DictCursor)
    
    query = "SELECT * FROM movie ORDER BY score DESC LIMIT 5"
    cursor.execute(query)
    
    movies = cursor.fetchall()

    cursor.close()
    connection.close()

    return movies
