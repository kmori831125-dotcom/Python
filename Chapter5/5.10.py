current_users = ['Admin', 'Alice', 'Bob', 'Carol', 'Dave']
new_users = ['alice', 'Eve', 'BOB', 'Frank', 'Grace']

# current_users の小文字版のコピーを作る
current_users_lower = []
for user in current_users:
    current_users_lower.append(user.lower())

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry, '{new_user}' is already taken. Please enter another username.")
    else:
        print(f"'{new_user}' is available.")