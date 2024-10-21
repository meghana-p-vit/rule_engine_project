import psycopg2
from psycopg2.extras import RealDictCursor

def get_db_connection():
    conn = psycopg2.connect(
        dbname="rule_engine_db",
        user="postgres",
        password="Megha*2904",
        host="db",
        port="5432"
    )
    return conn

def save_rule_to_db(rule_text):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("INSERT INTO rules (rule_text) VALUES (%s) RETURNING id", (rule_text,))
        rule_id = cursor.fetchone()[0]
        conn.commit()

        cursor.close()
        conn.close()
        return rule_id
    except Exception as e:
        print(f"Error saving rule: {e}")
        return None

def fetch_rule_from_db(rule_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)

        cursor.execute("SELECT * FROM rules WHERE id = %s", (rule_id,))
        rule = cursor.fetchone()

        cursor.close()
        conn.close()
        return rule
    except Exception as e:
        print(f"Error fetching rule: {e}")
        return None
