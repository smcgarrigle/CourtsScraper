# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# class CourtscraperPipeline:
#     def process_item(self, item, spider):
#         return item

# -*- coding: utf-8 -*-
import pymysql
# Define your item pipelines here
#

class CourtscraperPipeline(object):
    def __init__(self):
        #DB Connect
        self.conn=pymysql.connect(host="localhost", port=3306, user="root", passwd="root", db="slo",cursorclass=pymysql.cursors.DictCursor)

    def process_item(self, item, spider):
        url=item["url"]
        title=item["title"]
        headerh1=item["headerh1"]
        dv=item["dv"]
        content=item["content"]
        htmlcontent=item["htmlcontent"]

        connection = pymysql.connect(host='localhost',
                             port=3306,
                             user='root', #DONT STORE THESE IN THE REPO
                             password='root', #DONT STORE THESE IN THE REPO
                             db='slo',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor,
                             autocommit=1)
        try:
            with connection.cursor() as cursor:
                url=item["url"]
                name=item["title"]
                headerh1=item["headerh1"]
                content=item["content"]
                dv=item["dv"]
                htmlcontent=item["htmlcontent"]
                sql = "INSERT INTO `slodata` (`url`,`title`,`headerh1`,`dv`,`content`,`htmlcontent`) VALUES (%s, %s, %s, %s, %s,%s)"
                params=(url, name, headerh1, dv, content, htmlcontent)
                cursor.execute(sql,(params))

        finally:
            connection.close()
        return item

def close_spider(self,spider):
        # Close Connection
    self.conn.close()
