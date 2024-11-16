import json
import os

# Fungsi untuk meminta input file dengan validasi
def get_valid_filepath(prompt):
    while True:
        path = input(prompt)
        if os.path.isfile(path):                                                                     return path                                                                          else:
            print(f"File '{path}' tidak ditemukan. Silakan coba lagi.")

# Fungsi untuk meminta input direktori output dengan validasi
def get_valid_directory(prompt, default_directory=None):
    while True:
        path = input(prompt)
        if path == "":
            if default_directory:
                return default_directory
            else:
                print("Lokasi penyimpanan tidak dapat kosong.")
        elif os.path.isdir(path):
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
not_followed_by_me = [i for i in followers if i not in following]

# Hitung jumlah yang mengikuti balik dan tidak mengikuti balik
jumlah_following = len(following)
jumlah_followers = len(followers)
jumlah_good_people = len(good_people)
jumlah_not_following_back = len(not_following_back)
jumlah_not_followed_by_me = len(not_followed_by_me)

# Minta pengguna memasukkan lokasi dan nama file untuk menyimpan output
script_dir = os.path.dirname(os.path.abspath(__file__))  # Mendapatkan direktori script
output_dir = get_valid_directory("Masukkan lokasi untuk menyimpan file output (contoh: /storage/emulated/0/ig/) [Tekan Enter untuk menggunakan lokasi script]: ", default_directory=script_dir)
output_filename = input("Masukkan nama file output (tanpa ekstensi): ")

# Menyimpan hasilnya ke file HTML dengan tiga tabel dan CSS
output_path = os.path.join(output_dir, output_filename + ".html")
with open(output_path, 'w') as file:
    file.write(f'''<html>
<head>
    <title>Instagram Results</title>
    <style>
        body {{
            font-family: Montserrat, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            background-color: #f5deb3;  /* Wheat color */
            color: #4e4e4e;
            margin: 0;
            padding: 0;
            text-align: center;
        }}

        h1, h2, h3 {{
            font-weight: 600;
            margin: 20px 0;
        }}

        table {{
            width: 45%;
            border-collapse: collapse;
            margin: 20px auto;
            background-color: white;
            border: 1px solid #dbdbdb;
            border-radius: 8px;
            display: inline-block;
            vertical-align: top;
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

        /* CSS untuk search bar */
        #searchBar, #searchBar2, #searchBar3 {{
            margin: 20px;
            padding: 10px;
            width: 80%;
            max-width: 600px;
            font-size: 16px;
            border: 1px solid #dbdbdb;
            border-radius: 4px;
        }}
    </style>
    <script>
        function filterTable(inputId, tableId) {{
            var input, filter, table, tr, td, i, txtValue;
            input = document.getElementById(inputId);
            filter = input.value.toUpperCase();
            table = document.getElementById(tableId);
            tr = table.getElementsByTagName("tr");

            for (i = 1; i < tr.length; i++) {{
                td = tr[i].getElementsByTagName("td")[1];
                if (td) {{
                    txtValue = td.textContent || td.innerText;
                    if (txtValue.toUpperCase().indexOf(filter) > -1) {{
                        tr[i].style.display = "";
                    }} else {{
                        tr[i].style.display = "none";
                    }}
                }}
            }}
        }}
    </script>
</head>
<body>
    <h1>Results</h1>
    <h2>Total Following: {jumlah_following}</h2>
    <h2>Total Followers: {jumlah_followers}</h2>
    <h3>Jumlah Pengikuti Balik ({jumlah_good_people}) dan yang Tidak Mengikuti Balik ({jumlah_not_following_back})</h3>

    <!-- Search bar untuk tabel Pengikut Balik -->
    <input type="text" id="searchBar" onkeyup="filterTable('searchBar', 'goodPeopleTable')" placeholder="Cari nama...">

    <!-- Tabel Pengikut Balik -->
    <table id="goodPeopleTable">
        <thead>
            <tr>
                <th>No</th>
                <th>Mengikuti Balik</th>
            </tr>
        </thead>
        <tbody>''')

    for index, person in enumerate(good_people, start=1):
        file.write(f'<tr><td>{index}</td><td><a href="https://www.instagram.com/{person}">{person}</a></td></tr>\n')

    file.write('</tbody></table>')

    # Tabel Following yang Tidak Mengikuti Balik
    file.write(f'''
    <!-- Search bar untuk tabel Following yang Tidak Mengikuti Balik -->
    <input type="text" id="searchBar2" onkeyup="filterTable('searchBar2', 'notFollowingBackTable')" placeholder="Cari nama...">

    <table id="notFollowingBackTable">
        <thead>
            <tr>
                <th>No</th>
                <th>Following yang Tidak Mengikuti Balik</th>
            </tr>
        </thead>
        <tbody>''')

    for index, person in enumerate(not_following_back, start=1):
        file.write(f'<tr><td>{index}</td><td><a href="https://www.instagram.com/{person}">{person}</a></td></tr>\n')

    file.write('</tbody></table>')

    # Tabel Tidak Diikuti Tapi Mengikuti
    file.write(f'''
    <!-- Search bar untuk tabel Tidak Diikuti Tapi Mengikuti -->
    <input type="text" id="searchBar3" onkeyup="filterTable('searchBar3', 'notFollowedByMeTable')" placeholder="Cari nama...">

    <table id="notFollowedByMeTable">
        <thead>
            <tr>
                <th>No</th>
                <th>Tidak Diikuti Tapi Mengikuti</th>
            </tr>
        </thead>
        <tbody>''')

    for index, person in enumerate(not_followed_by_me, start=1):
        file.write(f'<tr><td>{index}</td><td><a href="https://www.instagram.com/{person}">{person}</a></td></tr>\n')

    file.write('</tbody></table>')

    # Tambahkan output jumlah yang tidak diikuti balik
    file.write(f'''
    <h3>Jumlah Pengguna yang Tidak Diikuti Balik: {jumlah_not_followed_by_me}</h3>
</body></html>''')

print(f"Output berhasil disimpan di: {output_path}")