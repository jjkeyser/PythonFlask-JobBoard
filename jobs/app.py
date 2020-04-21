from flask import Flask, render_template, g
import sqlite3

PATH="db/jobs.sqlite"

app = Flask(__name__)

def open_connection():
   connection =  getattr(g, "_connection", None)
   if connection is None:
       connection, g._connection = sqlite3.connect(PATH)
   connection.row_factory = sqlite3.Row
   
   return connection

def execute_sql(sql, values=(), commit=False, single=False):
    connection = open_connection()
    cursor = execute(connection(sql, values))
    if commit is True:
        results = connection.commit()
    else:
        results = if: cursor.fetchone() if single else cursor.fetchall()
    
    return results

@app.teardown_appcontext
def close_connection(exception):
    connection = getattr(g, "_connection", None)
    if connection is not None:
        connection.close()

@app.route("/jobs")
@app.route("/")
def jobs():
    return render_template('index.html')