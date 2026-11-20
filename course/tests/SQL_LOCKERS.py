SOLUTION_FILE = 'solution.sql'

import unittest
from collections import Counter
from pathlib import Path
import sqlite3

def run_query(tables, columns, ordered, expected):
    source = Path("solution.sql").read_text(encoding="utf-8")
    with sqlite3.connect(":memory:") as db:
        for name, (schema, rows) in tables.items():
            db.execute(f"CREATE TABLE {name} ({schema})")
            if rows:
                slots = ", ".join("?" for value in rows[0])
                db.executemany(f"INSERT INTO {name} VALUES ({slots})", rows)
        db.commit()
        db.execute("PRAGMA query_only = ON")
        def authorize(action, arg1, arg2, database, trigger):
            readable = action == sqlite3.SQLITE_READ and database == "main" and arg1 in tables
            function = action == sqlite3.SQLITE_FUNCTION and arg2 not in {"load_extension", "randomblob", "zeroblob"}
            return sqlite3.SQLITE_OK if readable or function or action == sqlite3.SQLITE_SELECT else sqlite3.SQLITE_DENY
        db.set_authorizer(authorize)
        cursor = db.execute(source)
        actual_columns = tuple(column[0].lower() for column in cursor.description or ())
        if actual_columns != columns:
            raise AssertionError(f"Ожидаются столбцы {columns}, получены {actual_columns}")
        actual = cursor.fetchmany(len(expected) + 1)
        if (actual != expected if ordered else Counter(actual) != Counter(expected)):
            raise AssertionError(f"Ожидаются строки {expected!r}, получены {actual!r}")

class Examples(unittest.TestCase):
    def test_case_1(self):
        run_query({'cards': ('id INTEGER, name TEXT', [(3, 'Миша'), (4, 'Аня')]), 'assignments': ('card_id INTEGER, locker TEXT', [(4, 'C8'), (8, 'B7')])}, ('name', 'locker'), False, [('Миша', None), ('Аня', 'C8')])

class SQL_LOCKERS(unittest.TestCase):
    def test_case_1(self):
        run_query({'cards': ('id INTEGER, name TEXT', [(3, 'Миша'), (4, 'Аня')]), 'assignments': ('card_id INTEGER, locker TEXT', [(4, 'C8'), (8, 'B7')])}, ('name', 'locker'), False, [('Миша', None), ('Аня', 'C8')])
    def test_case_2(self):
        run_query({'cards': ('id INTEGER, name TEXT', [(9, 'Инга'), (2, 'Нина')]), 'assignments': ('card_id INTEGER, locker TEXT', [])}, ('name', 'locker'), False, [('Инга', None), ('Нина', None)])
