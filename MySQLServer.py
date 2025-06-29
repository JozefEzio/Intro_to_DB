import pymysql
import pymysql.cursors

def create_database():
    try:
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='******',  
            cursorclass=pymysql.cursors.DictCursor
        )

        with connection.cursor() as cursor:
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("✅ Database 'alx_book_store' created successfully!")

        connection.commit()
        connection.close()

    except pymysql.MySQLError as e:
        print("Failed to connect or create database.")
        print("Error:", e)

create_database()
