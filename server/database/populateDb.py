import csv
import psycopg2
from psycopg2.extras import execute_values
from random import randint, random




# Function to establish a connection to the PostgreSQL database
def create_connection():
    try:
        connection = psycopg2.connect(
            ""
        )
        return connection
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)

# Function to insert data into the PostgreSQL database
def insert_books(connection, books_data):
    cursor = connection.cursor()

    # SQL query to insert data into the 'books' table
    insert_query = """
        INSERT INTO books (isbn13, isbn10, title, subtitle, authors, categories, thumbnail, discription, publication_year, avrage_rating, pages, rating_count, price)
        VALUES %s;
    """

    # Execute the query with the provided data
    execute_values(cursor, insert_query, books_data)
    
    # Commit the changes to the database
    connection.commit()

# Function to read data from CSV file
def read_csv_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        header = next(reader)  # Skip the header row
        data = [row for row in reader]
    return data

# Function to format data for insertion into PostgreSQL database
def format_data(csv_data):
    formatted_data = []
    for row in csv_data:
        # Handle empty or non-numeric average_rating
        try:
            average_rating = float(row[9])
        except (ValueError, TypeError):
            average_rating = None
        
         # Handle empty or non-numeric values in num_pages and ratings_count
        try:
            num_pages = int(row[10])
        except (ValueError, TypeError):
            num_pages = 0

        try:
            ratings_count = int(row[11])
        except (ValueError, TypeError):
            ratings_count = 0
        
        try:
            year = int(row[8])
        except (ValueError, TypeError):
            year = 2000



        # Generate a random price half of the times
        price = round(random() * 100 + 200, 2) if randint(0, 1) == 0 else 0
        formatted_data.append(
            (
                row[0], row[1], row[2], row[3], [author.strip() for author in row[4].split(';')],
                [category.strip() for category in row[5].split(';')],
                row[6], row[7], year, average_rating,
                num_pages, ratings_count, price
            )
        )
    return formatted_data

if __name__ == "__main__":
    # Replace these values with your PostgreSQL connection details
    db_connection = create_connection()

    # Specify the path to your CSV file
    csv_file_path = "/Users/drumilved/Desktop/Development/Library-systems/server/database/data.csv"

    # Read data from CSV file
    csv_data = read_csv_file(csv_file_path)

    # Format data for insertion into PostgreSQL database
    formatted_data = format_data(csv_data)

    # Insert data into the PostgreSQL database
    insert_books(db_connection, formatted_data)

    # print if everthing worked fine
    print("\n operation successfull!")

    # Close the database connection
    db_connection.close()
