from userClass import User

users = User.load_users()

user = User.create_user(1957, "Female", "Jönköping", False, "Inte tid")

users.append(user)

User.save_users(users)

for u in users:
    print(u.to_dict())