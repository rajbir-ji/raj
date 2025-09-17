import sqlite3

def get_account_number(user_id):
    conn = sqlite3.connect('HDFCbank.db')
    cursor = conn.cursor()
    cursor.execute("SELECT account_number FROM accounts WHERE user_id=?", (user_id,))
    result = cursor.fetchone()
    conn.close()
    if result:
        return result[0]
    return "Account number not found."

# Example usage
account_number = get_account_number(12340)
print("Account Number:", account_number)