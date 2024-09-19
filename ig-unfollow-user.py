import json
import os

# Fungsi untuk meminta input file dengan validasi
def get_valid_filepath(prompt):
    while True:
        path = input(prompt)
        if os.path.isfile(path):
            return path
        else:
            print(f"File '{path}' tidak ditemukan. Silakan coba lagi.")

# Fungsi untuk meminta input direktori output dengan validasi
def get_valid_directory(prompt):
    while True:
        path = input(prompt)
        if os.path.isdir(path):
            return path
        else:
            print(f"Direktori '{path}' tidak ditemukan. Silakan coba lagi.")

# Minta pengguna memasukkan path file followers dan following
followers_file = get_valid_filepath("Masukkan path file followers (contoh: /storage/emulated/0/ig/f/followers_1.json): ")
following_file = get_valid_filepath("Masukkan path file following (contoh: /storage/emulated/0/ig/f/following.json): ")

# Buka file followers
with open(followers_file) as f:
    followers_data = json.load(f)

followers = []
# Cek apakah followers_data adalah list atau dict
if isinstance(followers_data, list):
    for item in followers_data:
        if 'string_list_data' in item:
            for entry in item['string_list_data']:
                followers.append(entry['value'])
elif isinstance(followers_data, dict):
    for item in followers_data['string_list_data']:
        followers.append(item['value'])

# Buka file following
with open(following_file) as f:
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

# Minta pengguna memasukkan lokasi dan nama file untuk menyimpan output
output_dir = get_valid_directory("Masukkan lokasi untuk menyimpan file output (contoh: /storage/emulated/0/ig/output/): ")
output_filename = input("Masukkan nama file output (tanpa ekstensi): ") + ".html"

# Menyimpan hasilnya ke file HTML
output_path = os.path.join(output_dir, output_filename)
with open(output_path, 'w') as file:
    file.write('<html><head><title>Not Following Back</title><style>body {font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; background-color: #fafafa; color: #262626; margin: 0; padding: 0; text-align: center;} h1, h2, h3 {font-weight: 600; margin: 20px 0;} ul {list-style: none; padding: 0;} ul li {padding: 10px; border-bottom: 1px solid #dbdbdb;} ul li a {text-decoration: none; color: #00376b; font-weight: 500;} ul li a:hover {color: #0095f6;} header {background-color: white; border-bottom: 1px solid #dbdbdb; padding: 20px; box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);} .container {width: 90%; max-width: 600px; margin: 20px auto; background-color: white; border: 1px solid #dbdbdb; border-radius: 8px; padding: 20px;} .btn {background-color: #0095f6; color: white; border: none; border-radius: 4px; padding: 10px 20px; font-size: 14px; cursor: pointer;} .btn:hover {background-color: #007bb5;} .table-container {display: flex; justify-content: space-between;} .table {width: 45%; border: 1px solid #dbdbdb; padding: 10px; border-radius: 8px; background-color: white;} .table h3 {margin-bottom: 10px;}</style></head><body><header><h1>Not Following Back</h1></header><div class="container"><h2>Total Following: {following_count}</h2><h2>Total Followers: {followers_count}</h2><div class="table-container"><div class="table"><h3>Following yang Mengikuti Balik ({good_count}):</h3><ul>'.format(following_count=jumlah_following, followers_count=jumlah_followers, good_count=jumlah_good_people))

    # List following yang mengikuti balik
    for i in good_people:
        file.write(f'<li><a href="https://www.instagram.com/{i}">{i}</a></li>\n')
    
    file.write('</ul></div><div class="table"><h3>Following yang Tidak Mengikuti Balik ({not_following_back_count}):</h3><ul>'.format(not_following_back_count=jumlah_not_following_back))

    # List following yang tidak mengikuti balik
    for i in not_following_back:
        file.write(f'<li><a href="https://www.instagram.com/{i}">{i}</a></li>\n')
    
    file.write('</ul></div></div></div></body></html>')

print(f"Output berhasil disimpan di: {output_path}")
