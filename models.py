import sqlite3

# create a database connection
conn = sqlite3.connect('messages.db')

# create a table to store incoming messages
conn.execute('''CREATE TABLE incoming_messages
             (ID INT PRIMARY KEY NOT NULL,
             SENDER TEXT NOT NULL,
             RECIPIENT TEXT NOT NULL,
             MESSAGE TEXT NOT NULL);''')

# insert a message into the incoming_messages table
conn.execute("INSERT INTO incoming_messages (ID, SENDER, RECIPIENT, MESSAGE) \
              VALUES (1, 'user1', 'user2', 'Hello, user2!')")
conn.commit()

# create a table to store sent messages
