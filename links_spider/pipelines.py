# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3

class LinksSpiderPipeline(object):
    def __init__(self):
        self.setupDBCon()

    def setupDBCon(self):
        self.con = sqlite3.connect("links.db")
        self.cur = self.con.cursor()
        self.createSchema()

    def createSchema(self):
        self.cur.execute("""CREATE TABLE if not exists link
        (
          source_date      TEXT,
          source_link      TEXT,
          status           TEXT,
          target_link      TEXT
        )""")

    def closeDB(self):
        self.con.close()

    def __del__(self):
        self.closeDB()

    def process_item(self, item, spider):
        if item.__class__.__name__ == 'LinkItem':
            self.storeInDB_link(item)
        return item

    def storeInDB_link(self, item):
        self.cur.execute(\
            "INSERT INTO link(source_date, source_link,status, target_link)\
            VALUES(?, ?, ?, ?)",\
            (item.get('source_date', ''), item.get('source_link', ''), item.get('status', ''), item.get('target_link', '')))

        print('Link Added in Database')
        self.con.commit()



