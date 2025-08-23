# UTILITY/HELPER FUNCTIONS

# create connection
import pymysql

def get_connection(db_name=None):
    """
    Establishes a connection to the MySQL database.
    If db_name is provided and doesn't exist, it will be created.
    """
    try:
        # Connect to MySQL server without a database to create one if needed
        base_connection = pymysql.connect(
            host='localhost',
            user='root',
            password='actowiz'
        )
        if db_name:
            with base_connection.cursor() as cursor:
                cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
                print(f"Database '{db_name}' is ready.")
        base_connection.close()

        # Now connect to the requested database
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='actowiz',
            database=db_name if db_name else None
        )
        return connection

    except pymysql.MySQLError as e:
        print(f"Database connection error: {e}")
        return None

def create_table(db_name, table_name, columns):
    """
    Creates a table in the specified database.

    Parameters:
        db_name (str): Name of the database.
        table_name (str): Name of the table.
        columns (dict): Dictionary of column names and types.
    """
    connection = get_connection(db_name)
    if connection:
        try:
            with connection.cursor() as cursor:
                column_definitions = ", ".join([f"{col} {dtype}" for col, dtype in columns.items()])
                query = f"CREATE TABLE IF NOT EXISTS {table_name} ({column_definitions})"
                cursor.execute(query)
                connection.commit()
                print(f"Table '{table_name}' created successfully in '{db_name}'.")
        except pymysql.MySQLError as e:
            print(f"Error creating table '{table_name}': {e}")
        finally:
            connection.close()

def insert_data(region, subregion, movie_url_lists,database,table):
    conn = get_connection(database)
    data_to_insert = []
    for movie_list in movie_url_lists:
        for url in movie_list:
            data_to_insert.append((region, subregion, url))

    if data_to_insert:
        with conn.cursor() as cursor:
            sql = f"""
                INSERT INTO {table} (region, subregion, url)
                VALUES (%s, %s, %s)
            """
            cursor.executemany(sql, data_to_insert)
        conn.commit()
def select_data(db_name,table_name, columns, conditions=None):
    """
    Selects data from a specified table.

    Parameters:
        table_name (str): Name of the table to select data from.
        columns (list): List of column names to select.
        conditions (dict, optional): Dictionary of conditions where key is column name and value is the condition value.
    """
    connection = get_connection(db_name)
    if connection:
        try:
            with connection.cursor() as cursor:
                # Build the SELECT query
                columns_str = ", ".join(columns) if columns else "*"
                query = f"SELECT {columns_str} FROM {table_name}"
                
                # Add WHERE clause if conditions are provided
                if conditions:
                    where_clause = " AND ".join([f"{col} = %s" for col in conditions.keys()])
                    query += f" WHERE {where_clause}"
                    cursor.execute(query, tuple(conditions.values()))
                else:
                    cursor.execute(query)
                
                # Fetch all results
                results = cursor.fetchall()
                return results
        except pymysql.MySQLError as e:
            print(f"Error selecting data from '{table_name}': {e}")
            return None
        finally:
            connection.close()

def update_data(db_name,table_name, data, record_id):
    """
    Updates data in a specified table for a given ID.

    Parameters:
        table_name (str): Name of the table to update data in.
        data (dict): Dictionary of column names and their new values.
        record_id (int): ID of the record to update.
    """
    connection = get_connection(db_name)
    if connection:
        try:
            with connection.cursor() as cursor:
                # Build the UPDATE query
                set_clause = ", ".join([f"{col} = %s" for col in data.keys()])
                query = f"UPDATE {table_name} SET {set_clause} WHERE shop_id = %s"
                
                # Add the id to the values tuple
                values = list(data.values())
                values.append(record_id)
                
                cursor.execute(query, tuple(values))
                connection.commit()
                print(f"Data updated successfully in '{table_name}' for ID {record_id}.")
        except pymysql.MySQLError as e:
            print(f"Error updating data in '{table_name}': {e}")
        finally:
            connection.close()

def update_data_by_column(db_name, table_name, data, condition_column, condition_value):
    """
    Updates data in a specified table based on a condition column.

    Parameters:
        db_name (str): Name of the database.
        table_name (str): Name of the table to update data in.
        data (dict): Dictionary of column names and their new values.
        condition_column (str): Name of the column to use in WHERE clause.
        condition_value: Value to match in the condition column.
    """
    connection = get_connection(db_name)
    if connection:
        try:
            with connection.cursor() as cursor:
                # Build the UPDATE query
                set_clause = ", ".join([f"{col} = %s" for col in data.keys()])
                query = f"UPDATE {table_name} SET {set_clause} WHERE {condition_column} = %s"
                
                # Add the condition value to the values tuple
                values = list(data.values())
                values.append(condition_value)
                
                cursor.execute(query, tuple(values))
                connection.commit()
                print(f"Data updated successfully in '{table_name}' for {condition_column} = {condition_value}.")
        except pymysql.MySQLError as e:
            print(f"Error updating data in '{table_name}': {e}")
        finally:
            connection.close()

# from db_operations import create_table, insert_data
#
# # Table name
# table_name = "employees"
#
# # Columns for the table (name and type)
# columns = {
#     "id": "INT AUTO_INCREMENT PRIMARY KEY",
#     "name": "VARCHAR(100)",
#     "age": "INT",
#     "department": "VARCHAR(50)"
# }
#
# # Data to insert
# data = {
#     "name": "John Doe",
#     "age": 30,
#     "department": "IT"
# }
#
# # Create the table
# create_table(table_name, columns)
#
# # Insert data into the table
# insert_data(table_name, data)

def get_links(conn, query):
    pass

def update_link_status(conn, query):
    pass

def save_page(page, page_dir, page_name, extension="html", zip=True):
    pass

def clean_text(text):
    pass