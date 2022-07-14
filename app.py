from turtle import title
import requests
import subprocess
import sys

title_art = r"""

▀█▀ █▀█ █▀█ █▀█ █▀▀ █▄░█ ▀█▀ █▀▀ █▀█
░█░ █▄█ █▀▄ █▀▄ ██▄ █░▀█ ░█░ ██▄ █▀▄
"""

print(title_art + '\n')

def main():
    movie_name = input("Enter Movie Name: ")
    base_url = f"https://api.sumanjay.cf/torrent/?query={movie_name}"

    torrent_results = requests.get(url=base_url).json()

    index = 1
    magnet = []
    for result in torrent_results:
        if 'movie' in result['type'].lower():
            print(index, ") ", result['name'], "-->", result['size'])
            index += 1
            magnet.append(result['magnet'])
            
    print("/n/n")

    choice = int(input("Enter The Index of the Movie You Want: "))
    magnet_link =  magnet[choice-1]

    stream_choice = ()
    if stream_choice == 1:
        download = False
    else:
        download = True

    handler(magnet_link, download)

def handler(magnet_link, download):
    cmd = []
    cmd.append("webtorrent")
    cmd.append(magnet_link)
    if not download:
        cmd.append('--vlc')

    if sys.platform.startswith('win32'):
        subprocess.call(cmd, shell=True)
    elif sys.platform.startswith('linux'):
        subprocess.call(cmd)

main()