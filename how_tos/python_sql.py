import sqlite3

# 1. Connect, 2. Execute, 3. Commit/Fetch, 4. Close

def add_user(cursor :sqlite3, name: str, number: int):
    cursor.execute("INSERT INTO users (name, number) VALUES (?, ?)", (name, number))
    print(type(cursor), name, number)
    
def delete_user(cursor :sqlite3, name: str):
    # tuple, even for single item, needs a comma
    cursor.execute("DELETE FROM users WHERE name = ?", (name,))
    print(type(cursor), name)

def start():
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()

    # when creating new user entry id will not be provided
    # id will autoincrement
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT, 
                            number INTEGER
                    )
                """)
    
    input_user = input("What sql function do you want to perform? add delete ")
    if input_user == "add":
        ans1, ans2 = input("Please provide name number: ").split()
        add_user(cursor, ans1, int(ans2))
        conn.commit()
        print(cursor.execute("SELECT * FROM users"))
        print(cursor.fetchall())
        # rows = cursor.fetchall()
        conn.close()
    elif input_user == "delete":
        ans1 = input("Please provide name: ")
        delete_user(cursor, ans1)
        conn.commit()
        print(cursor.execute("SELECT * FROM users"))
        print(cursor.fetchall())
        # can use this to get the rows
        # rows = cursor.fetchall()
        conn.close()

start()