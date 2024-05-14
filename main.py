import requests, time

print("\034[1;35;40m\n")
print("""
 _   _ _ _        _ 
| \ | (_) |      (_)
|  \| |_| | _____ _ 
| . ` | | |/ / __| |
| |\  | |   <\__ \ |
\_| \_/_|_|\_\___/_|
                        
""")

def shorten_url(url):
    api_url = "https://tinyurl.com/api-create.php?url=" + url
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.text
    else:
        return "Epäonnistui"

long_url = input("Pitkä Linkki: ")

short_url = shorten_url(long_url)
print("Lyhyt Linkki:", short_url)
time.sleep(5)



