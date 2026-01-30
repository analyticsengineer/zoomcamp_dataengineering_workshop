#!/usr/bin/env python
# coding: utf-8

import psycopg2
import pandas as pd
from psycopg2.extras import execute_values
import numpy



df = pd.read_csv('student_performance.csv')

df.head()

len(df)

# Checking data information

df.info()

# Putting the data into PostgreSQL

df.columns = [
    "student_id",
    "datetime",
    "gender",
    "race/ethnicity",
    "parental level of education",
    "lunch",
    "test preparation course",
    "math score",
    "reading score",
    "writing score"
]

conn = psycopg2.connect(
    host="localhost",
    port=5433,
    database="ng_education",
    user="postgres",
    password="anuoluwapo"
)

print("psycopg2 connected successfully")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS
student_performance (
     student_id                  TEXT PRIMARY KEY,
     datetime                    TIMESTAMP,
     gender                      TEXT,
     race_ethnicity              TEXT,
     parental_level_of_education TEXT,
     lunch                       TEXT,
     test_preparation_course     TEXT,
     math_score                  INTEGER,
     reading_score               INTEGER,
     writing_score               INTEGER
);
""")


records = df.to_numpy().tolist()

insert_sql = """
INSERT INTO student_performance (
    student_id, datetime,
    gender, race_ethnicity, parental_level_of_education,
    lunch, test_preparation_course, math_score, reading_score, writing_score
)
VALUES %s
"""

execute_values(cur, insert_sql, records)

conn.commit()
cur.close()
conn.close()

print("Data loaded successfully")




