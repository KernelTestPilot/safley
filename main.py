from userClass import User

users = User.load_users()

user = User.create_user(1990, "Female", "Hallefors", False, "Hann inte presentera")

users.append(user)

User.save_users(users)

for u in users:
    print(u.to_dict())