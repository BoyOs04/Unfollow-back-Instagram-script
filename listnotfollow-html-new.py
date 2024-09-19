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
not_following_back = [i for i in following if i not in good_people]

# Hitung jumlah yang mengikuti balik dan tidak mengikuti balik
jumlah_following = len(following)
jumlah_followers = len(followers)
jumlah_good_people = len(good_people)
jumlah_not_following_back = len(not_following_back)

# Menyimpan yang kamu follow tapi tidak follow balik ke file HTML
with open('/storage/emulated/0/ig/f/not_following_back.html', 'w') as file:
    file.write('<html>\n<head>\n<title>Not Following Back</title>\n</head>\n<body>\n')
    file.write(f'<h1>Total Following: {jumlah_following}</h1>\n')
    file.write(f'<h1>Total Followers: {jumlah_followers}</h1>\n')
    file.write(f'<h2>Following yang mengikuti balik: {jumlah_good_people}</h2>\n')
    file.write(f'<h2>Following yang tidak mengikuti balik: {jumlah_not_following_back}</h2>\n')
    file.write('<h3>Daftar Following yang Tidak Mengikuti Balik:</h3>\n')
    file.write('<ul>\n')
    for i in not_following_back:
        file.write(f'<li><a href="https://www.instagram.com/{i}">https://www.instagram.com/{i}</a></li>\n')
    file.write('</ul>\n')
    file.write('<h3>Daftar Following yang Mengikuti Balik:</h3>\n')
    file.write('<ul>\n')
    for i in good_people:
        file.write(f'<li><a href="https://www.instagram.com/{i}">https://www.instagram.com/{i}</a></li>\n')
    file.write('</ul>\n')
    file.write('</body>\n</html>')
