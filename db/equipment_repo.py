from db.connection import get_connection

def query_equipment(db_path, sql, params=()):
    conn = get_connection(db_path)
    cursor = conn.cursor()
    cursor.execute(sql, params)
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    conn.close()
    return columns, rows