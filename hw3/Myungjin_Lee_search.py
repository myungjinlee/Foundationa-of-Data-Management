#!/usr/bin/env python2.7

import sys
import mysql.connector

f_obj=sys.argv[1]
f_obj=f_obj.capitalize()

cnx=mysql.connector.connect(user='inf551', password='inf551', host='127.0.01', database='sakila')
cursor=cnx.cursor()

query="select count(*) from film, film_category, category where film.film_id=film_category.film_id and film_category.category_id=category.category_id and category.name='%s'" %f_obj
cursor.execute(query)

for i in cursor:
    print i[0]

cursor.close()
cnx.close()

