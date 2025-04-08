from djongo import connection

def test_connection():
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            print("Database connection successful.")
    except Exception as e:
        print(f"Database connection failed: {e}")
        raise

if __name__ == "__main__":
    test_connection()
