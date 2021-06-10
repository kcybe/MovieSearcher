from time import sleep
import requests, clipboard, json, os;
######################################
#           Linux Clipboard          #
#          -----------------         #
# sudo apt-get install xclip         #
# sudo apt-get install xsel          #
# sudo apt-get install wl-clipboard  #
######################################

def Search(MovieTitle):
    search_link = "https://yts.mx/api/v2/list_movies.json";
    req = requests.get(search_link + f"?query_term={MovieTitle}");
    resp = json.loads(req.content);
    try:
        movies = resp['data']['movies'];
    except:
        print(f"Didn't Find Any Title Named {keyword}")
        return
    
    index_default = -1; 
    index = index_default;
    for movie in movies: 
        index += 1;
        print(f"[{index}] Title: {movie['title_long']} | Rating: {movie['rating']} | Runtime: H{round(movie['runtime'] / 60, 2)}")
        movie_choice = int(input("Movie Index => "));
        magnet_link = "magnet:?xt=urn:btih:";
        if 0 <= movie_choice <= index:
            index = index_default;
            torrents = movies[movie_choice]['torrents'];
            for torrent in torrents:
                index += 1;
                print(f"[{index}] Quality: {torrent['quality']} | Type: {torrent['type']} | Seeds: {torrent['seeds']} | Peers: {torrent['peers']} | Size: {torrent['size']} | Upload Date: {torrent['date_uploaded']} | Magnet: {magnet_link + torrent['hash']}");
            torrent_choice = int(input("Torrent Index => "))
            if 0 <= torrent_choice <= index:
                clipboard.copy(magnet_link + torrents[torrent_choice]['hash'])
                print("Successfully Copied Magnet Link.")
                sleep(1)
                return
            else:
                index = index_default;
                print("Not a Valid Choice.")
                sleep(1); Clear();
        else:
            index = index_default;
            print("Not a Valid Choice.")
            sleep(1); Clear();

def Clear():
    os.system('cls' if os.name == 'nt' else 'clear');

if __name__ == "__main__":
    while True:
        Clear()
        print("Movie Searcher | (by u/Kcybe)");
        keyword = input("Movie Title: ");
        Search(keyword);