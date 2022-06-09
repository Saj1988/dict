import psycopg2
conn = psycopg2.connect(
   host="localhost",
   database="database",
   user="user123",
   password="abc123"
)
# # read_dict: returns the list of all dictionary entries:
#   argument: C - the database connection.

def read_dict(Conn):
    cur = Conn.cursor()
    cur.execute("SELECT id, word, translation FROM dictionary;")
    rows = cur.fetchall()
    cur.close()
    return rows
def add_word(Conn, word, translation):
    cur = Conn.cursor()
    cur.execute(f"INSERT INTO dictionary (word, translation) VALUES ('{word}', '{translation}');")
    cur.close()
def delete_word(Conn, ID):
    cur = Conn.cursor()
    cur.execute(f"DELETE FROM dictionary WHERE id = '{ID}';")
    cur.close()
def save_dict(Conn):
    cur = Conn.cursor()
    cur.execute("COMMIT;")
    cur.close()

while True: ## REPL - Read Execute Program Loop
    cmd = input("Command: ")
    if cmd == "list":
        print(read_dict(conn))
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
