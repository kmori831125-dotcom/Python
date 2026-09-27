users = {
    "aeinstein": {
        "first": "albert",
        "last": "einstein",
        "location": "princeton"
    },
    "mcurie": {
        "first": "marie",
        "last": "curie",
        "location": "paris"
    }
}

users["inewrtown"] = {
    "first": "isaac",
    "last": "newton",
    "location": "cambridge",
    "email": "isaac.newton@example.com"
}

print(f"Total user count is: {len(users)}\n")

for username in sorted(users.keys()):
    user_info = users[username]
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    email = user_info.get('email', 'No email registered')

    print(f"Username: {username}")
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
    print(f"\tEmail: {email}\n")