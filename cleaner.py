import sqlite3
import time
from ML.objectDictionary import *
import os
import pandas as pd


class DB:
    def __init__(self, path, lock=None):
        """Initialize db class variables"""
        self.connection = sqlite3.connect(path, timeout=30, check_same_thread=False)
        self.cur = self.connection.cursor()
        self.lock = lock

    def insert(self, data_list):
        if data_list:
            table_name = data_list[0].table
            self.cur.executemany(
            f'''insert or ignore into {table_name}({','.join(data_list[0].__dataclass_fields__)}) values ({','.join(['?' for i in range(len(data_list[0].__dataclass_fields__))])})''',
            [tuple([getattr(row, key) for key in row.__dataclass_fields__]) for row in data_list])
            print(f"{table_name} inserted {self.cur.rowcount} rows.")

            self.connection.commit()

db = DB('../airbnb.db')
db.cur.execute("select rowid,listing_id,date from Reviews order by rowid asc;")

if __name__ =="__main__":
    seen = set()
    full_db = []
    last_listing_id = None
    for row in db.cur:
        rowid,listing_id,date = row
        if last_listing_id==None:
            #add to db
            full_db.append({"rowid":rowid,"listing_id":listing_id,"date":date})
            #mark seen
            seen.add(last_listing_id)
            #set as last seen
            last_listing_id = listing_id
            last_was_inserted = True
        elif not listing_id in seen:
            #add to db
            full_db.append({"rowid":rowid,"listing_id":listing_id,"date":date})
            #mark seen
            seen.add(last_listing_id)
            #set as last seen
            last_listing_id = listing_id
            last_was_inserted = True
        elif listing_id in seen and listing_id ==last_listing_id and last_was_inserted:
                # add to db
                full_db.append({"rowid": rowid, "listing_id": listing_id, "date": date})
                # mark seen
                seen.add(last_listing_id)
                # set as last seen
                last_listing_id = listing_id
                last_was_inserted = True
        else:
            last_was_inserted = False

    df = pd.DataFrame(full_db)
    df.to_csv("cleaned_reviews.csv",index = False)
