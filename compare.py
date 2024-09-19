import json

# Buka file followers
with open('./storage/emulated/0/ig/f/followers_1.json') as f:  # sesuaikan dengan path di Termux
    followers_data = json.load(f)

followers = []
for i in followers_data['string_list_data']:
    for j in i:
        followers.append(j['value'])

# Buka file following
with open('./storage/shared/following.json') as f:  # sesuaikan dengan path di Termux
    following_data = json.load(f)

following = []
for i in following_data['relationships_following']:
    for j in i['string_list_data']:
        following.append(j['value'])

# Membandingkan followers dan following
good_people = []
for i in following:
    if i in followers:
        good_people.append(i)

# Menampilkan yang kamu follow tapi tidak follow balik
for i in following:
    if i not in good_people:
        print(f"https://www.instagram.com/{i}")
