import sys
from os.path import join, dirname, abspath
sys.path.insert(1, join(dirname(abspath(__file__)), '..'))
from config import load_db_config, FLASK_ENV
from sqlite3 import connect

def load_schema():
    cfg = load_db_config()
    dbname = cfg[FLASK_ENV]['database']
    conn = connect(dbname)
    schema = open('db/schema.sql', 'r').read()
    conn.execute(schema)
    conn.close


def seed():
    cfg = load_db_config()
    dbname = cfg[FLASK_ENV]['database']
    conn = connect(dbname)
    f = open('db/seed.sql', 'r')
    for sql in f:
      conn.execute(sql)
    f.close() 
    conn.close
