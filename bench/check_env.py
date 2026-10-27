import duckdb

con = duckdb.connect()  # no filename means an in-memory DB
con.execute("INSTALL postgres; LOAD postgres;")
con.execute("INSTALL sqlite; LOAD sqlite;")

con.execute("ATTACH 'dbname=dw_bench host=localhost' AS pg (TYPE postgres);")
con.execute("ATTACH 'bench/staging.db' AS lite (TYPE sqlite);")

con.execute("DROP TABLE IF EXISTS lite.t;")
con.execute("CREATE TABLE lite.t (id INTEGER, name VARCHAR);")
con.execute("INSERT INTO lite.t VALUES (1, 'a'), (2, 'b');")

con.execute("DROP TABLE IF EXISTS pg.public.t;")
con.execute("CREATE TABLE pg.public.t AS SELECT * FROM lite.t;")
print(con.execute("SELECT * FROM pg.public.t ORDER BY id;").fetchall())