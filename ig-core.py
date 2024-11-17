import json
import os

def get_valid_filepath(prompt):
    while True:
        path = input(prompt)
        if os.path.isfile(path):
            return path
        else:
            print(f"File '{path}' tidak ditemukan. Silakan coba lagi.")

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

def load_json_data(file_path):
    with open(file_path) as f:
        data = json.load(f)
    return data

def extract_usernames(data):
    usernames = []
    if isinstance(data, list):
        for item in data:
            if 'string_list_data' in item:
                for entry in item['string_list_data']:
                    usernames.append(entry['value'])
            elif 'relationships_following' in item:
                for entry in item['relationships_following']:
                    for subentry in entry['string_list_data']:
                        usernames.append(subentry['value'])
    elif isinstance(data, dict):
        if 'string_list_data' in data:
            for item in data['string_list_data']:
                usernames.append(item['value'])
        elif 'relationships_following' in data:
            for item in data['relationships_following']:
                for subentry in item['string_list_data']:
                    usernames.append(subentry['value'])
    return usernames

def generate_html(followers, following, output_path):
    good_people = [i for i in following if i in followers]
    not_following_back = [i for i in following if i not in good_people]
    not_followed_by_me = [i for i in followers if i not in following]

    html_content = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
   <link data-default-icon="https://static.cdninstagram.com/rsrc.php/v3/yI/r/VsNE-OHk_8a.png" rel="icon" sizes="192x192" href="https://static.cdninstagram.com/rsrc.php/v3/yI/r/VsNE-OHk_8a.png" />
        <title>Instagram Follower Analysis</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: wheat;
                color: #333;
                line-height: 1.6;
                padding: 20px;
                margin: 0;
                font-size:1.5vh;
            }}
            .container {{
                max-width: 1200px;
                margin: 0 auto;
                padding: 20px;
                background-color: #fff;
                border-radius: 12px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
            }}
            h1, h2 {{
                color: #444;
                text-align: center;
                font-size:25px;
            }}
            .tabs {{
                display: flex;
                justify-content: center;
                margin-bottom: 20px;
                background-color: wheat;
                border-radius: 20vh;
                margin: 20px;
                padding:33px;
            }}
            .tab {{
                padding: 10px 20px;
                cursor: pointer;
                background-color: #f0f0f0;
                border: none;
                outline: none;
                transition: background-color 0.3s;
                border-radius: 8px;
                margin: 0 5px;
            }}
            .tab:hover, .tab.active {{
                background-color: #ddd;
            }}
            .tab-content {{
                display: none;
            }}
            .tab-content.active {{
                display: block;
            }}
            input[type="text"] {{
                width: 45%;
                padding: 10px;
                margin-bottom: 10px;
                border: 1px solid #ddd;
                border-radius: 8px;
                justify-content: center;
            }}
            .scroll-list {{
                max-height: 400px;
                overflow-y: auto;
                border: 1px solid #ddd;
                border-radius: 8px;
                padding: 10px;
            }}
            ul {{
                list-style-type: decimal;
                padding-left: 20px;
                margin: 0;
            }}
            li {{
                margin-bottom: 5px;
            }}
            a {{
                color: #0066cc;
                text-decoration: none;
            }}
            a:hover {{
                text-decoration: underline;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Instagram Follower Analysis</h1>
            <h2>Total Following: {len(following)} | Total Followers: {len(followers)}</h2>
            
            <div class="tabs">
                <button class="tab active" onclick="openTab(event, 'mutualFollowers')">Mutual Followers</button>
                <button class="tab" onclick="openTab(event, 'notFollowingBack')">Not Following Back</button>
                <button class="tab" onclick="openTab(event, 'notFollowedByMe')">Not Followed By Me</button>
            </div>

            <div id="mutualFollowers" class="tab-content active">
                <input type="text" id="searchMutual" onkeyup="filterList('searchMutual', 'mutualList')" placeholder="Search mutual followers...">
                <div class="scroll-list">
                    <ul id="mutualList">
                        {generate_list_items(good_people)}
                    </ul>
                </div>
            </div>

            <div id="notFollowingBack" class="tab-content">
                <input type="text" id="searchNotFollowing" onkeyup="filterList('searchNotFollowing', 'notFollowingList')" placeholder="Search not following back...">
                <div class="scroll-list">
                    <ul id="notFollowingList">
                        {generate_list_items(not_following_back)}
                    </ul>
                </div>
            </div>

            <div id="notFollowedByMe" class="tab-content">
                <input type="text" id="searchNotFollowed" onkeyup="filterList('searchNotFollowed', 'notFollowedList')" placeholder="Search not followed by me...">
                <div class="scroll-list">
                    <ul id="notFollowedList">
                        {generate_list_items(not_followed_by_me)}
                    </ul>
                </div>
            </div>
        </div>

        <script>
            function openTab(evt, tabName) {{
                var i, tabContent, tabLinks;
                tabContent = document.getElementsByClassName("tab-content");
                for (i = 0; i < tabContent.length; i++) {{
                    tabContent[i].style.display = "none";
                }}
                tabLinks = document.getElementsByClassName("tab");
                for (i = 0; i < tabLinks.length; i++) {{
                    tabLinks[i].className = tabLinks[i].className.replace(" active", "");
                }}
                document.getElementById(tabName).style.display = "block";
                evt.currentTarget.className += " active";
            }}

            function filterList(inputId, listId) {{
                var input, filter, ul, li, a, i, txtValue;
                input = document.getElementById(inputId);
                filter = input.value.toUpperCase();
                ul = document.getElementById(listId);
                li = ul.getElementsByTagName("li");
                for (i = 0; i < li.length; i++) {{
                    a = li[i].getElementsByTagName("a")[0];
                    txtValue = a.textContent || a.innerText;
                    if (txtValue.toUpperCase().indexOf(filter) > -1) {{
                        li[i].style.display = "";
                    }} else {{
                        li[i].style.display = "none";
                    }}
                }}
            }}
        </script>
    </body>
    </html>
    '''

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

def generate_list_items(users):
    return '\n'.join([f'<li><a href="https://www.instagram.com/{user}" target="_blank">{user}</a></li>' for user in users])

def main():
    followers_file = get_valid_filepath("Masukkan path file followers (contoh: /storage/emulated/0/ig/f/followers_1.json): ")
    following_file = get_valid_filepath("Masukkan path file following (contoh: /storage/emulated/0/ig/f/following.json): ")

    followers_data = load_json_data(followers_file)
    following_data = load_json_data(following_file)

    followers = extract_usernames(followers_data)
    following = extract_usernames(following_data)

    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = get_valid_directory("Masukkan lokasi untuk menyimpan file output (contoh: /storage/emulated/0/ig/) [Tekan Enter untuk menggunakan lokasi script]: ", default_directory=script_dir)
    output_filename = input("Masukkan nama file output (tanpa ekstensi): ")

    output_path = os.path.join(output_dir, output_filename + ".html")
    generate_html(followers, following, output_path)

    print(f"Output berhasil disimpan di: {output_path}")

if __name__ == "__main__":
    main()
