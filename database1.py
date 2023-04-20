from sqlalchemy import create_engine
import os
# URL_DB  = "postgresql://tdi:qKmd8s5ze7WAYV@adventureworks.tditrain.com:5431/wells"
URL_DB  = os.getenv("URL_DB")

engine=create_engine(URL_DB)

depth_min=2000
grad_min=0.075

def query_db(depth_min,grad_min):
    """blabla"""

    engine=create_engine(URL_DB)
    
    query = f"""
    SELECT latitude,longitude,depth,gradient
    FROM wells
    WHERE depth > {depth_min} AND gradient > {grad_min}
    """

    with engine.connect() as conn:
        results = conn.execute(query).fetchall()
    conn.close()

    return results

if __name__ == '__main__':
    depth_min=2000
    grad_min=0.075
    print(query_db(depth_min,grad_min))
    