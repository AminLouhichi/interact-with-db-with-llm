import pyodbc

# Connect to the database

# Initialize an empty list to store the rows


# Retrieve data from dbo.Columns table and append to the list as tuples
def database():
    cnxn = pyodbc.connect(r'Driver=SQL Server;Server=server;Database=data;Trusted_Connection=yes;')
    cursor = cnxn.cursor()

    cursor.execute("SELECT * FROM dbo.Databases")
    db_name = []
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        db_name.append((row.DataBaseName))

    # Close the connection
    cnxn.close()

    # Print the list of tuples
    for row in db_name:
        print(row)
    return db_name

def create_context(db) :
   
    # Connect to the database
    cnxn = pyodbc.connect(r'Driver=SQL Server;Server=DESKTOP-5BV9H95;Database=Data_Ready;Trusted_Connection=yes;')
    cursor = cnxn.cursor()

    # Initialize variables to track the current table being processed
    current_table = None
    sql_table_creations = {}
    tables=[]

    # Retrieve data from dbo.Columns table
    cursor.execute(f"SELECT * FROM dbo.Columns where DataBaseName = ?", db)
    while True:
        row = cursor.fetchone()
        if row is None:
            break
        
        # Extract column values
        database_name = row.FullTableName
        column_name = row.ColumnName
        column_type = row.ColumnType
        is_pk = row.IsPK
        is_fk = row.IsFK
        
        # Start a new table if it's the first column for a new table
        if current_table != database_name:
            current_table = database_name
            sql_table_creations[current_table] = []
        
        # Append column definition to the current table
        sql_table_creations[current_table].append((column_name, column_type, is_pk, is_fk))
        tables.append(current_table)

    # Close the connection
    cnxn.close()

    # Create a list to store the SQL table creation statements
    sql_statements = []

    # Append the SQL table creation statements to the list
    for database_name, columns in sql_table_creations.items():
        sql_statement = f"CREATE TABLE {database_name} (\n"
        for column_name, column_type, is_pk, is_fk in columns:
            pk_str = " PRIMARY KEY" if is_pk else ""
            sql_statement += f"\t{column_name} {column_type}{pk_str},\n"
        sql_statement = sql_statement[:-2] + "\n)"
        sql_statements.append(sql_statement)

    # Print or use the SQL statements as needed
    for sql in sql_statements:
        print(sql)
    return sql_statements ,set(tables)

