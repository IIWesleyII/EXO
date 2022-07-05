from db import create_table, connect_db, add_planets
from flask import Flask

app = Flask(__name__)

app.route('/')
def home():
    return ''


if __name__ == '__main__':
    # create connection to db
    conn = connect_db()

    # create tables
    create_table(conn)

    # add planets
    #add_planets(conn)

    app.run(debug=True)