import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()


CREATE_EXOPLANET_TABLE = '''
CREATE TABLE IF NOT EXISTS exoplanets(
    id SERIAL PRIMARY KEY, 
    planet_name TEXT, 
    dist_from_earth INTEGER, 
    planet_mass TEXT,
    stellar_magnitude DECIMAL,
    discovery_date INTEGER
    );

'''

csv_path = os.getenv('CSV_PATH')
ADD_EXOPLANETS = f'''
COPY exoplanets(
        planet_name, 
        dist_from_earth, 
        planet_mass,
        stellar_magnitude,
        discovery_date
    )
    FROM '{csv_path}'
    DELIMITER ','
    CSV HEADER;
'''


def connect_db():
    try:
        conn = psycopg2.connect(
            user ='postgres',
            password= os.getenv('DB_PASSWORD'),
            host='localhost',
            database='exo'
        )
    except ConnectionError as exc:
        raise RuntimeError('Failed to open database') from exc

    return conn
    

def create_table(conn): 
    with conn:
        cursor = conn.cursor()
        cursor.execute(CREATE_EXOPLANET_TABLE)
        cursor.close()


def add_planets(conn):
    with conn:
        cursor = conn.cursor()
        cursor.execute(ADD_EXOPLANETS)
        cursor.close()