import sqlite3

db_locale='database.db'

connie= sqlite3.connect(db_locale)
c= connie.cursor()

c.execute("""
CREATE TABLE users (
    username Text not null ,
    password TEXT not null
)
""")

connie.commit()
connie.close()
