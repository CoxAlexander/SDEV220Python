import SQLAlchemy  
engine = SQLAlchemy.create_engine("sqlite:///books.db")
conn = engine.connect()
sql = SQLAlchemy.text("SELECT title from book")
rows = conn.execute(sql)
for row in rows:
    print("title:", row[0])
conn.close()
engine.dispose()
