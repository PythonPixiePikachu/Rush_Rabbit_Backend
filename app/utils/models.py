class profiles:
    create_profile = "INSERT INTO profile (user_name,first_name,last_name,email) VALUES (?, ?, ?,?)"
    get_profile = "SELECT * FROM profile WHERE user_name = ?"
    update_profile = "UPDATE profile SET first_name = ?, last_name = ?, email = ? WHERE user_name = ?"
    delete_profile = "DELETE FROM profile WHERE user_name = ?"