import sqlite3

conn = sqlite3.connect('school.db')
cursor = conn.cursor()

with open('queries.sql', 'r') as file:
    sql_script = file.read()

lines = [line for line in sql_script.splitlines() if not line.strip().startswith('--')]
script = "\n".join(lines)

commands = [cmd.strip() for cmd in script.split(';') if cmd.strip()]

for cmd in commands:
    try:
        if cmd.upper().startswith("SELECT"):
            cursor.execute(cmd)
            rows = cursor.fetchall()
            print('New query')
            for row in rows:
                print("-----".join(str(x) for x in row))
        else:
            cursor.execute(cmd)  
    except sqlite3.Error as e:
        print(f"Error in query: {e}")

conn.commit()
conn.close()
