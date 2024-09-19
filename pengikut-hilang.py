import json

# Fungsi untuk membaca follower dari file JSON
def baca_follower_dari_json(file_path):
    with open(file_path) as f:
        data = json.load(f)
    followers = []
    if isinstance(data, list):
        for item in data:
            if 'string_list_data' in item:
                for entry in item['string_list_data']:
                    followers.append(entry['value'])
            elif 'relationships_following' in item:
                for entry in item['relationships_following']:
                    for subentry in entry['string_list_data']:
                        followers.append(subentry['value'])
    elif isinstance(data, dict):
        if 'string_list_data' in data:
            for item in data['string_list_data']:
                followers.append(item['value'])
        elif 'relationships_following' in data:
            for item in data['relationships_following']:
                for subentry in item['string_list_data']:
                    followers.append(subentry['value'])
    return set(followers)  # Mengembalikan sebagai set untuk efisiensi

# Membaca follower dari file lama dan file baru
followers_lama = baca_follower_dari_json('/storage/emulated/0/ig/f/followers_lama.json')
followers_baru = baca_follower_dari_json('/storage/emulated/0/ig/f/followers_baru.json')

# Menambahkan URL Instagram
followers_lama = {'www.instagram.com/' + follower for follower in followers_lama}
followers_baru = {'www.instagram.com/' + follower for follower in followers_baru}

# Mencetak follower yang ada di file baru tetapi hilang dari file lama
hilang_dari_lama = followers_baru - followers_lama

# Fungsi untuk membuat HTML dengan link Instagram
def buat_html(followers, output_file):
    html_content = '<!DOCTYPE html>\n<html>\n<head>\n<title>Follower yang Hilang</title>\n</head>\n<body>\n'
    html_content += '<h1>Follower yang hilang dari file lama:</h1>\n<ul>\n'
    for follower in followers:
        html_content += f'<li><a href="{follower}" target="_blank">{follower}</a></li>\n'
    html_content += '</ul>\n</body>\n</html>'
    with open(output_file, 'w') as file:
        file.write(html_content)

# Buat HTML dan simpan
buat_html(hilang_dari_lama, '/storage/emulated/0/ig/f/follower_hilang.html')

print("HTML telah dibuat dengan nama 'follower_hilang.html'")
