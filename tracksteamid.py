from steam.client import SteamClient
from steam.enums import EResult

username = input("nhap tk steam: ")
password = input("nhap mk steam: ")

client = SteamClient()
print(f"🔑 Đăng nhập {username}…")
result = client.login(username, password)
if result != EResult.OK:
    print("❌ Login failed:", result)
    input("check lai file!")

steamid64 = client.steam_id.as_64
friendcode = steamid64 - 76561197960265728
print(f"✅ SteamID64: {steamid64} | FriendCode: {friendcode}")