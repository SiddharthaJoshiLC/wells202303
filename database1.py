from sqlalchemy import create_engine

# URL_DB  = "postgresql://tdi:qKmd8s5ze7WAYV@adventureworks.tditrain.com:5431/wells"
URL_DB  = os.get_env("URL_DB")

engine=create_engine(URL_DB)

depth_min=2000
grad_min=0.075

query = f"""
    SELECT latitude,longitude,depth,gradient
    FROM wells
    WHERE depth > {depth_min} AND gradient > {grad_min}
"""

conn=engine.connect()

results=conn.execute(query).fetchall()

conn.close()

print(results)

