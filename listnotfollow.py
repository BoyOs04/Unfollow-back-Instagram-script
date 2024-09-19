import json

# Buka file followers
with open('/storage/emulated/0/ig/f/followers_1.json') as f:
    followers_data = json.load(f)

followers = []
# Cek apakah followers_data adalah list atau dict
if isinstance(followers_data, list):
    # Jika followers_data adalah list, akses tiap elemen
    for item in followers_data:
        # Pastikan ada key 'string_list_data' dalam setiap dictionary
        if 'string_list_data' in item:
            for entry in item['string_list_data']:
                followers.append(entry['value'])
elif isinstance(followers_data, dict):
    # Jika followers_data adalah dict, langsung akses 'string_list_data'
    for item in followers_data['string_list_data']:
        followers.append(item['value'])

# Buka file following
with open('/storage/emulated/0/ig/f/following.json') as f:
    following_data = json.load(f)

following = []
# Cek apakah following_data adalah list atau dict
if isinstance(following_data, list):
    for item in following_data:
        if 'relationships_following' in item:
            for entry in item['relationships_following']:
                for subentry in entry['string_list_data']:
                    following.append(subentry['value'])
elif isinstance(following_data, dict):
    for item in following_data['relationships_following']:
        for subentry in item['string_list_data']:
            following.append(subentry['value'])

# Membandingkan followers dan following
good_people = [i for i in following if i in followers]

# Menyimpan yang kamu follow tapi tidak follow balik ke file teks
with open('/storage/emulated/0/ig/f/not_following_back.txt', 'w') as file:
    for i in following:
        if i not in good_people:
            file.write(f"https://www.instagram.com/{i}\n")
