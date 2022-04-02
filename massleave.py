import requests

def bot_leaver(guild_id, token):
    headers={'Authorization': token}
    apilink = f"https://discord.com/api/v8/users/@me/guilds/{guild_id}"
    r = requests.delete(apilink, headers=headers)
    print("[!] Left server ")

def main():
    tokens = []

    with open("tokens.txt", "r") as tokens_file:
        lines = tokens_file.readlines()
        tokens.extend(l.replace('\n', '') for l in lines)
    guild_id = input('[!] Enter server ID: ')


    input("Hit ENTER to mass leave discord server.")
    for botzz in tokens:
        bot_leaver(guild_id, botzz)
            

if __name__ == "__main__":
    main()