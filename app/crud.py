
from app.database import get_db_connection
from app.utils.models import profiles

def create_profile(user_name: str,first_name: str, last_name: str, email: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        profiles.create_profile,
        (user_name, first_name, last_name, email)
    )
    conn.commit()
    conn.close()

def get_profile(user_name: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(profiles.get_profile, (user_name,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return {"UserName": row[1], "First Name": row[2], "Last Name": row[3], "Email": row[4]}
    return None

def update_profile(user_name: str,first_name: str, last_name: str, email: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        profiles.update_profile,
        (first_name, last_name, email,user_name)
    )
    conn.commit()
    conn.close()

def delete_profile(user_name: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(profiles.delete_profile, (user_name,))
    conn.commit()
    conn.close()
