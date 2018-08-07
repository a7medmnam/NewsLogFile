#!/usr/bin python3
import psycopg2
import datetime

DATA_BASE_NAME = "news"

data_base = psycopg2.connect(
    database=DATA_BASE_NAME
)
execute = data_base.cursor()
# you have to create Viewcount as the readme
# first question
execute.execute("""
            select title, counter
            from viewcount
            order by counter desc
            limit 3
          """)
top_article = execute.fetchall()

# second question
execute.execute("""
            select a.name, sum(vc.counter) as overall_views
            from (select * from viewcount) as vc
            join authors as a on a.id = vc.id
            group by a.name
            order by overall_views desc
          """)
top_author = execute.fetchall()

# third question
execute.execute("""
            select to_char(date, 'FMMonth DD, YYYY'), error_percentage
            from percentage
            where error_percentage>1.0
          """)
error = execute.fetchall()

# file name as time
date = datetime.datetime.now()
file_name = "{0}_{1}_{2}_{3}_{4}_{5}.txt".format(
        str(date.year),
        str(date.month),
        str(date.day),
        str(date.hour),
        str(date.minute),
        str(date.second)
    )

# file creation for the report
with open(file_name, 'w') as results:
    # first question
    results.write("1. What are the most popular three articles of all time?\n")
    for x in top_article:
        results.write(str(x[0]) + " "  + str(x[1]) + "\n")
    # second question
    results.write(
        "\n2. Who are the most popular article authors of all time?\n")
    for x in top_author:
        results.write(str(x[0]) + " "  + str(x[1]) + "\n")
    # third question
    results.write(
        "\n3. On which days did more than 1% of requests lead to errors?\n"
    )
    for x in error:
        results.write(str(x[0]) + " " + str(x[1]) + "\n")

data_base.close()

