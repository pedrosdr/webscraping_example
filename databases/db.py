import sqlite3 as sql

class Team:
    def __init__(self) -> None:
        self.conn = sql.connect('databases/db.sqlite3')

    def insert(self, name:str, year:int, wins:int, losses:int, pct:float) -> None:
        cursor = self.conn.cursor()
        try:
            query = 'INSERT INTO teams(id, name, year, wins, losses, pct) '\
                    'VALUES(NULL, ?, ?, ?, ?, ?)'
            
            cursor.execute(query, (name, year, wins, losses, pct))
            self.conn.commit()
        finally:
            cursor.close()


if __name__ == '__main__':
    # create database
    open('databases/db.sqlite3', 'w')
    
    # create table
    with sql.connect('databases/db.sqlite3') as conn:
        cursor = conn.cursor()
        try:
            query = 'CREATE TABLE teams'\
                    '('\
                    '   id INTEGER PRIMARY KEY NOT NULL,'\
                    '   name TEXT NOT NULL,'\
                    '   year INTEGER NOT NULL,'\
                    '   wins INTEGER NOT NULL,'\
                    '   losses INTEGER NOT NULL,'\
                    '   pct REAL NOT NULL'\
                    ')'
            cursor.execute(query)
            conn.commit()
        finally:
            cursor.close()
    
            
            
            