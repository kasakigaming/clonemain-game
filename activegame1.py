import os
import json
import string
import requests
import psutil
import re
import sys
from time import sleep


print("⢀⣒⠒⠆⠤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print("⢠⡛⠛⠻⣷⣶⣦⣬⣕⡒⠤⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print("⡿⢿⣿⣿⣿⣿⣿⡿⠿⠿⣿⣳⠖⢋⣩⣭⣿⣶⡤⠶⠶⢶⣒⣲⢶⣉⣐⣒⣒⣒⢤⡀⠀⠀⠀⠀⠀⠀⠀")
print("⣿⠀⠉⣩⣭⣽⣶⣾⣿⢿⡏⢁⣴⠿⠛⠉⠁⠀⠀⠀⠀⠀⠀⠉⠙⠲⢭⣯⣟⡿⣷⣘⠢⡀⠀⠀⠀⠀⠀")
print("⠹⣷⣿⣿⣿⣿⣿⢟⣵⠋⢠⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣾⣦⣾⣢⠀⠀⠀⠀")
print("⠀⠹⣿⣿⣿⡿⣳⣿⠃⠀⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⠟⠀⠀⠀⠀")
print("⠀⠀⠹⣿⣿⣵⣿⠃⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⡄⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠈⠛⣯⡇⠛⣽⣦⣿⠀⠀⠀⠀⢀⠔⠙⣄⠀⠀⠀⠀⠀⠀⣠⠳⡀⠀⠀⠀⠀⢿⡵⡀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⣸⣿⣿⣿⠿⢿⠟⠀⠀⠀⢀⡏⠀⠀⠘⡄⠀⠀⠀⠀⢠⠃⠀⠹⡄⠀⠀⠀⠸⣿⣷⡀⠀⠀⠀")
print("⠀⠀⠀⢰⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⢸⠒⠤⢤⣀⣘⣆⠀⠀⠀⡏⢀⣀⡠⢷⠀⠀⠀⠀⣿⡿⠃⠀⠀⠀")
print("⠀⠀⠀⠸⣿⣿⠟⢹⣥⠀⠀⠀⠀⠀⣸⣀⣀⣤⣀⣀⠈⠳⢤⡀⡇⣀⣠⣄⣸⡆⠀⠀⠀⡏⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠁⠁⠀⢸⢟⡄⠀⠀⠀⠀⣿⣾⣿⣿⣿⣿⠁⠀⠈⠙⠙⣯⣿⣿⣿⡇⠀⠀⢠⠃⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠇⢨⢞⢆⠀⠀⠀⡿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⣿⣿⣿⡿⡇⠀⣠⢟⡄⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⡼⠀⢈⡏⢎⠳⣄⠀⡇⠙⠛⠟⠛⠀⠀⠀⠀⠀⠀⠘⠻⠛⢱⢃⡜⡝⠈⠚⡄⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠘⣅⠁⢸⣋⠈⢣⡈⢷⠇⠀⠀⠀⠀⠀⣄⠀⠀⢀⡄⠀⠀⣠⣼⢯⣴⠇⣀⡀⢸⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠈⠳⡌⠛⣶⣆⣷⣿⣦⣄⣀⠀⠀⠀⠈⠉⠉⢉⣀⣤⡞⢛⣄⡀⢀⡨⢗⡦⠎⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠪⣿⠁⠀⠐⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⠉⠁⢸⠀⠀⠀⠄⠙⡆⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⣀⠤⠚⡉⢳⡄⠡⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⠁⣠⣧⣤⣄⣀⡀⡰⠁⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⢀⠔⠉⠀⠀⠀⠀⢀⣧⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣅⡀⠀⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⢸⠆⠀⠀⠀⣀⣼⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠋⠁⣠⠖⠒⠒⠛⢿⣆⠀⠀⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠑⠤⠴⠞⢋⣵⣿⢿⣿⣿⣿⣿⣿⣿⠗⣀⠀⠀⠀⠀⠀⢰⠇⠀⠀⠀⠀⢀⡼⣶⣤⠀⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠟⢛⣿⠀⠙⠲⠽⠛⠛⠵⠞⠉⠙⠳⢦⣀⣀⡞⠀⠀⠀⠀⡠⠋⠐⠣⠮⡁⠀")
print("⠀⠀⠀⠀⠀⠀⠀⢠⣎⡀⢀⣾⠇⢀⣠⡶⢶⠞⠋⠉⠉⠒⢄⡀⠉⠈⠉⠀⠀⠀⣠⣾⠀⠀⠀⠀⠀⢸⡀")
print("⠀⠀⠀⠀⠀⠀⠀⠘⣦⡀⠘⢁⡴⢟⣯⣞⢉⠀⠀⠀⠀⠀⠀⢹⠶⠤⠤⡤⢖⣿⡋⢇⠀⠀⠀⠀⠀⢸⠀")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠵⠗⠺⠟⠖⢈⡣⡄⠀⠀⠀⠀⢀⣼⡤⣬⣽⠾⠋⠉⠑⠺⠧⣀⣤⣤⡠⠟⠃")
print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠷⠶⠦⠶⠞⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
print("---------------------------------------------------------\n")
print("author: hlongᗜ‿ᗜ\ndiscord: hlong")
print("\n--❄️⑨🧊 active game 🧊⑨❄️--\n")


def close_steam():
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == 'steam.exe':
            try:
                proc.kill()
                print("🛑 Đã đóng steam.exe. Chuẩn bị mở lại")
                sleep(2)
            except Exception as e:
                print(f"⚠️ Không thể đóng steam.exe: {e}")


def is_steam_running():
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] and 'steam.exe' in proc.info['name'].lower():
            return True
    return False


def find_steam_exe():
    print("🔍 Đang tìm steam.exe...")
    for drive in string.ascii_uppercase:
        drive_path = f"{drive}:\\"
        if os.path.exists(drive_path):
            for root, dirs, files in os.walk(drive_path):
                if 'steam.exe' in files:
                    steam_path = os.path.join(root, 'steam.exe')
                    print(f"✅ Tìm thấy steam.exe tại: {steam_path}")
                    return steam_path
    return None


def resource_path(relative_path):
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def get_game_details(appid):
    try:
        detail_url = f"https://store.steampowered.com/api/appdetails?appids={appid}"
        detail_response = requests.get(detail_url)
        detail_data = detail_response.json().get(str(appid), {}).get('data', {})
        
        if not detail_data:
            print("⚠️ Không lấy được chi tiết game")
            return None
        
        result = {
            "main_game": {
                "name": detail_data.get('name', f"App {appid}"),
                "appid": appid,
                "type": "game"
            },
            "dlcs": []
        }
        
        if 'dlc' in detail_data:
            for dlc_appid in detail_data['dlc']:
                dlc_url = f"https://store.steampowered.com/api/appdetails?appids={dlc_appid}"
                dlc_response = requests.get(dlc_url)
                dlc_data = dlc_response.json().get(str(dlc_appid), {}).get('data', {})
                
                if dlc_data:
                    result["dlcs"].append({
                        "name": dlc_data.get('name', f"DLC {dlc_appid}"),
                        "appid": dlc_appid,
                        "type": "dlc"
                    })
        
        return result
        
    except Exception as e:
        print(f"⚠️ Lỗi khi lấy chi tiết game: {e}")
        return None


def search_game_and_dlc(game_name):
    try:
        
        unwanted_keywords = ["benchmark tool", "prologue", "demo"]
        
        
        search_url = f"https://store.steampowered.com/a i/storesearch/?term={game_name}&l=english&cc=us"
        response = requests.get(search_url)
        response.raise_for_status()
        results = response.json().get('items', [])
        
        if not results:
            print("⚠️ Không tìm thấy game trong Steam Database")
            return None
        
        
        main_game = None
        dlcs = []
        
        
        for item in results:
            name = item['name']
            lower_name = name.lower()
            if any(keyword in lower_name for keyword in unwanted_keywords):
                continue
            if game_name.lower() in lower_name:
                main_game = {
                    "name": name,
                    "appid": item['id'],
                    "type": "game"
                }
                break
        if not main_game:
            for item in results:
                name = item['name']
                lower_name = name.lower()
                
                if not any(keyword in lower_name for keyword in unwanted_keywords):
                    main_game = {
                        "name": name,
                        "appid": item['id'],
                        "type": "game"
                    }
                    break
        
        if not main_game:
            print("⚠️ Không tìm thấy game chính")
            return None
        
        
        clean_main_name = re.sub(r'[™®]', '', main_game['name']).strip()
        
        
        game_details = get_game_details(main_game['appid'])
        if game_details and game_details.get("dlcs"):
            for dlc in game_details["dlcs"]:
                lower_dlc_name = dlc['name'].lower()
                if any(keyword in lower_dlc_name for keyword in unwanted_keywords):
                    continue
                
                
                clean_dlc_name = re.sub(r'[™®]', '', dlc['name']).strip()
                
                
                if clean_dlc_name.startswith(clean_main_name):
                    
                    if not any(d['appid'] == dlc['appid'] for d in dlcs):
                        dlcs.append(dlc)
        
        return {
            "main_game": main_game,
            "dlcs": dlcs
        }
        
    except Exception as e:
        print(f"⚠️ Lỗi khi tìm game: {e}")
        return None

def write_appids(idgame, depot_data, lua_path):
    found_ids = []
    key_main = depot_data.get(str(idgame))
    if key_main:
        found_ids.append(f'addappid({idgame},1,"{key_main}")')
    else:
        found_ids.append(f'addappid({idgame},1)')

   
    for i in range(idgame + 1, idgame + 10):
        key = depot_data.get(str(i))
        if key:
            found_ids.append(f'addappid({i},1,"{key}")')

    if found_ids:
        with open(lua_path, 'a', encoding='utf-8') as lua_file:
            if os.path.getsize(lua_path) > 0:
                lua_file.write("\n--\n")
            for line in found_ids:
                lua_file.write(line + "\n")
        print("✅ Đã ghi")
    else:
        print("⚠️ Không tìm thấy ID nào trong thư viện")


def write_single_appid(appid, depot_data, lua_path):
    key = depot_data.get(str(appid))
    with open(lua_path, 'a', encoding='utf-8') as lua_file:
        if os.path.getsize(lua_path) > 0:
            lua_file.write("\n--\n")
        if key:
            lua_file.write(f'addappid({appid},1,"{key}")\n')
        else:
            lua_file.write(f'addappid({appid},1)\n')
    print(f"✅ Đã thêm appid: {appid}")


def is_game_added(appid, lua_path):
    if not os.path.exists(lua_path):
        return False
        
    pattern = re.compile(rf'addappid\s*\(\s*{appid}\s*,')
    
    with open(lua_path, 'r', encoding='utf-8') as f:
        for line in f:
            if pattern.search(line):
                return True
    return False


def main():
    steam_path = find_steam_exe()
    if not steam_path:
        print("❌ Không tìm thấy steam.exe")
        input("👉 Nhấn phím bất kỳ để thoát...")
        return

    steam_dir = os.path.dirname(steam_path)
    config_dir = os.path.join(steam_dir, 'config')
    stplugin_path = os.path.join(config_dir, 'stplug-in')
    os.makedirs(stplugin_path, exist_ok=True)

    lua_path = os.path.join(stplugin_path, 'nomore.lua')
    depotkeys_path = resource_path("depotkeys.json")

    if not os.path.isfile(depotkeys_path):
        print("❌ Không tìm thấy depotkeys.json")
        input("👉 Nhấn phím bất kỳ để thoát...")
        return

    try:
        with open(depotkeys_path, 'r', encoding='utf-8') as f:
            depot_data = json.load(f)
    except Exception as e:
        print(f"❌ Lỗi khi đọc JSON: {e}")
        input("👉 Nhấn phím bất kỳ để thoát...")
        return

    while True:
        print("--")
        print("1. Thêm game bằng ID")
        print("2. Tìm kiếm game bằng ID")
        print("3. Tìm kiếm game bằng tên")
        print("4. Thêm DLC")
        print("5. Thoát và khởi động Steam")
        
        choice = input("👉 Lựa chọn: ").strip()
        
        if choice == '1':
            while True:
                try:
                    idgame = int(input("\n🎮 Nhập ID game: "))
                    write_appids(idgame, depot_data, lua_path)
                    
                    cont = input("🔄 Bạn có muốn tiếp tục không? (y/n): ").strip().lower()
                    if cont != 'y':
                        break
                except ValueError:
                    print("❌ ID không hợp lệ.")
        
        elif choice == '2':
            appid_str = input("🔍 Nhập ID game để tìm kiếm: ").strip()
            if not appid_str.isdigit():
                print("❌ ID không hợp lệ.")
                continue
                
            appid = int(appid_str)
            print("\n🔍 Đang tìm kiếm thông tin game trên Steam...")
            game_info = get_game_details(appid)
            
            if not game_info:
                print("❌ Không tìm thấy thông tin game")
                continue
                
            main_game = game_info.get("main_game", {})
            dlcs = game_info.get("dlcs", [])
            
            print("\n" + "--")
            print(" KẾT QUẢ TÌM KIẾM ")
            print("--")
            print(f"Game chính: {main_game.get('name')} - {main_game.get('appid')} - {main_game.get('type')}")
            
            if dlcs:
                print("\nDLCs:")
                for dlc in dlcs:
                    print(f"- {dlc.get('name')} - {dlc.get('appid')} - {dlc.get('type')}")
            else:
                print("\nℹ️ Không tìm thấy DLC nào")
            
            print("\n" + "--")
            print("1. Thêm game chính")
            print("2. Thêm game + tất cả DLC")
            print("3. Quay lại")
            
            sub_choice = input("👉 Lựa chọn: ").strip()
            
            if sub_choice == '1':
                write_appids(main_game['appid'], depot_data, lua_path)
            elif sub_choice == '2':
                write_appids(main_game['appid'], depot_data, lua_path)
                for dlc in dlcs:
                    write_single_appid(dlc['appid'], depot_data, lua_path)
        
        elif choice == '3':
            game_name = input("🎮 Nhập tên game: ").strip()
            
            print("\n🔍 Đang tìm kiếm thông tin game trên Steam...")
            game_info = search_game_and_dlc(game_name)
            
            if not game_info:
                print("❌ Không tìm thấy thông tin game")
                continue
                
            main_game = game_info.get("main_game", {})
            dlcs = game_info.get("dlcs", [])
            
            print("\n" + "--")
            print(" KẾT QUẢ TÌM KIẾM ")
            print("--")
            print(f"Game chính: {main_game.get('name')} - {main_game.get('appid')} - {main_game.get('type')}")
            
            if dlcs:
                print("\nDLCs:")
                for dlc in dlcs:
                    print(f"- {dlc.get('name')} - {dlc.get('appid')} - {dlc.get('type')}")
            else:
                print("\nℹ️ Không tìm thấy DLC nào")
            
            print("\n" + "--")
            print("1. Thêm game chính")
            print("2. Thêm game + tất cả DLC")
            print("3. Quay lại")
            
            sub_choice = input("👉 Lựa chọn: ").strip()
            
            if sub_choice == '1':
                write_appids(main_game['appid'], depot_data, lua_path)
            elif sub_choice == '2':
                write_appids(main_game['appid'], depot_data, lua_path)
                for dlc in dlcs:
                    write_single_appid(dlc['appid'], depot_data, lua_path)
        
        elif choice == '4':
            main_appid = input("🎮 Nhập appid của game chính: ").strip()
            if not main_appid.isdigit():
                print("❌ AppID không hợp lệ")
                continue
                
            if not is_game_added(int(main_appid), lua_path):
                print("❌ Chưa thêm game chính, vui lòng thêm game trước")
                continue
                
            dlc_appid = input("🧩 Nhập appid DLC: ").strip()
            if not dlc_appid.isdigit():
                print("❌ AppID không hợp lệ")
                continue
                
            write_single_appid(int(dlc_appid), depot_data, lua_path)
        
        elif choice == '5':
            break
            
        else:
            print("❌ Lựa chọn không hợp lệ")

    print("\n🎉 Hoàn tất! Đã cập nhật game thành công")
    if is_steam_running():
        print("✅ Steam đang chạy. ĐANG TỰ ĐỘNG TẮT STEAM")
        close_steam()
    
    print("Đang khởi động steam...")
    try:
        os.startfile(steam_path)
        print("🚀 Đã mở Steam thành công.\n👉 Vui lòng kiểm tra trong thư viện!")
    except Exception as e:
        print(f"⚠️ Không thể mở Steam: {e}")

    input("👉 Nhấn phím bất kỳ để thoát...")

if __name__ == "__main__":
    main()