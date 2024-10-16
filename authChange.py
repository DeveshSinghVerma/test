import sqlite3

AUTH_KEY  = "LIVE_AUTH_KEY_RYTFGYTUGHVJB"
AUTH_KEY_SECRET =  "LIVE_AUTH_KEY_SECRET_FDGHYIUOYTDFGHJUKYILYTJDFUKIOYFHTMGYJUIY"
def login(user_input):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    
    # Vulnerable to SQL injection
    query = f"SELECT * FROM users WHERE username = '{user_input}'"
    
    cursor.execute(query)
    result = cursor.fetchall()
    
    if result:
        print("Login successful")
    else:
        print("Login failed")

# Example usage
user_input = input("Enter username: ")  # Try something like ' OR 1=1 -- to bypass login
login(user_input)
