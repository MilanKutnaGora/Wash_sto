import psycopg2


class Database:
    def __init__(self, config):
        self.conn = psycopg2.connect(**config)
        self.cur = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS customers (
                id SERIAL PRIMARY KEY,
                license_plate TEXT UNIQUE,
                last_visit TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        self.conn.commit()

    def is_customer(self, license_plate):
        self.cur.execute("SELECT * FROM customers WHERE license_plate = %s", (license_plate,))
        return self.cur.fetchone() is not None

    def add_customer(self, license_plate):
        self.cur.execute("INSERT INTO customers (license_plate) VALUES (%s)", (license_plate,))
        self.conn.commit()

    def __del__(self):
        self.cur.close()
        self.conn.close()