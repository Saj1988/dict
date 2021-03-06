import psycopg2
conn = psycopg2.connect(
   host="localhost",
   database="database",
   user="user123",
   password="abc123"
)
# # read_dict: returns the list of all dictionary entries:
#   argument: C - the database connection.

def read_dict(C):
    cur = C.cursor()
    cur.execute("SELECT id, word, translation FROM dictionary;")
    rows = cur.fetchall()
    cur.close()
    return rows
def add_word(C, word, translation):
    cur = C.cursor()
    cur.execute(f"INSERT INTO dictionary (word, translation) VALUES ('{word}', '{translation}');")
    cur.close()
def delete_word(C, ID):
    cur = C.cursor()
    cur.execute(f"DELETE FROM dictionary WHERE id = '{ID}';")
    cur.close()
def save_dict(C):
    cur = C.cursor()
    cur.execute("COMMIT;")
    cur.close()

while True: ## REPL - Read Execute Program Loop
    cmd = input("Command: ")
    if cmd == "list":
        for i, wd, trans in read_dict(conn):
            print(f"{i}: {wd} - {trans}")
    elif cmd == "add":
        name = input("  Word: ")
        phone = input("  Translation: ")
        add_word(conn, name, phone)
    elif cmd == "delete":
        ID = input("  ID: ")
        delete_word(conn, ID)
    elif cmd == "quit":
        save_dict(conn)
        exit()

def main():
    while True: ## REPL - Read Execute Program Loop
        cmd = input("Command: ")
        if cmd == "list":
            print(read_dict(conn))
        elif cmd == "add":
            name = input("  Word: ")
            phone = input("  Translation: ")
            add_word(conn, name, phone)
            print(f" Added word {name}")
        elif cmd == "delete":
            ID = input("  ID: ")
            delete_word(conn, ID)
        elif cmd == "quit":
            save_dict(conn)
            exit()
        
main()




