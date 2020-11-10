import sys
from os.path import join, dirname, abspath
sys.path.insert(1, join(dirname(abspath(__file__)), '../lib'))
from task import load_schema

if __name__== "__main__":
    load_schema()
