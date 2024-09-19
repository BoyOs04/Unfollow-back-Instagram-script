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

# Menyimpan hasilnya ke file HTML dengan tabel dan CSS
output_path = os.path.join(output_dir, output_filename)
with open(output_path, 'w') as file:
    file.write(f'''<html>
<head>
    <title>Result</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            background-color: #fafafa;
            color: #262626;
            margin: 0;
            padding: 0;
            text-align: center;
        }}

        h1, h2, h3 {{
            font-weight: 600;
            margin: 20px 0;
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px auto;
            background-color: white;
            border: 1px solid #dbdbdb;
            border-radius: 8px;
            overflow: hidden;
        }}

        th, td {{
            padding: 10px;
            border-bottom: 1px solid #dbdbdb;
            text-align: left;
        }}

        th {{
            background-color: #f0f0f0;
            font-weight: bold;
        }}

        tr:hover {{
            background-color: #f9f9f9;
        }}

        a {{
            text-decoration: none;
            color: #00376b;
            font-weight: 500;
        }}

        a:hover {{
            color: #0095f6;
        }}
    </style>
</head>
<body>
    <h1>Not Following Back</h1>
    <h2>Total Following: {jumlah_following}</h2>
    <h2>Total Followers: {jumlah_followers}</h2>
    <h3>Following yang Mengikuti Balik ({jumlah_good_people}) dan yang Tidak Mengikuti Balik ({jumlah_not_following_back})</h3>
    <table>
        <thead>
            <tr>
                <th>Following yang Mengikuti Balik</th>
                <th>Following yang Tidak Mengikuti Balik</th>
            </tr>
        </thead>
        <tbody>''')

    # Menentukan panjang kolom untuk tabel
    max_len = max(jumlah_good_people, jumlah_not_following_back)
    for i in range(max_len):
        following_back = good_people[i] if i < len(good_people) else ""
        not_following_back = not_following_back[i] if i < len(not_following_back) else ""
        file.write(f'<tr><td><a href="https://www.instagram.com/{following_back}">{following_back}</a></td><td><a href="https://www.instagram.com/{not_following_back}">{not_following_back}</a></td></tr>\n')

    file.write('</tbody></table></body></html>')

print(f"Output berhasil disimpan di: {output_path}")
