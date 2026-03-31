import requests, json, csv, time

YOUR_API_KEY = 'INSERT_YOUR_API_HERE'

tic = time.perf_counter()

with open('watchlist.csv', 'r', encoding='utf-8') as fin:
    csvreader = csv.reader(fin)
    rows = []
    for row in csvreader:
        rows.append(row)
    if len(rows) > 0:
        rows.pop(0)
        
    watchlist = [None]*len(rows)
    for i in range(len(rows)):
        # O .strip() remove espaços em branco acidentais no começo ou fim do nome
        if len(rows[i]) > 1:
            watchlist[i] = rows[i][1].strip()

def searchid(moviename, api_key):
    global movietitle
    movietitle = moviename
    
    # Ignora se o nome do filme estiver vazio
    if not moviename:
        return None
        
    x = requests.get('https://api.themoviedb.org/3/search/movie?api_key='+str(api_key)+'&query='+str(moviename).replace(' ','+'))
    movieresults = json.loads(x.text)
    
    # Verifica se a API retornou a chave 'results' e se ela não está vazia
    if 'results' in movieresults and len(movieresults['results']) > 0:
        movieinfo = movieresults['results']
        moviedetails = movieinfo[0]
        movieid = moviedetails['id']
        return movieid
    else:
        # Se não achou, avisa no terminal e retorna None
        print(f"[{moviename}] - ID não encontrado no TMDB.")
        return None

def search(movieid, api_key):
    x = requests.get('https://api.themoviedb.org/3/movie/'+str(movieid)+'/watch/providers?api_key='+str(api_key))
    streaminglist = json.loads(x.text)
    
    # Adicionando uma verificação extra caso a API de provedores falhe
    if 'results' not in streaminglist:
        print(movietitle + " is not available in any streaming service")
        fout.write(movietitle + " is not available in any streaming service\n")
        return

    streaminglistresults = streaminglist['results']
    
    if 'BR' in streaminglistresults:
        brstreaminglist = streaminglistresults['BR']
        
        if 'flatrate' in brstreaminglist:
            flatrate = brstreaminglist['flatrate']
            for entry in flatrate:
                print(movietitle + ' - ' + entry['provider_name'])
                fout.write(movietitle + ' - ' + entry['provider_name'] + '\n')
        else:
            print(movietitle + " is not available in any streaming service")
            fout.write(movietitle + " is not available in any streaming service\n")
    else:
        print(movietitle + " is not available in any streaming service")
        fout.write(movietitle + " is not available in any streaming service\n")

# Usando encoding utf-8 para evitar erros com acentos em nomes de filmes
with open('results.txt', 'a', encoding='utf-8') as fout:
    for i in watchlist:
        if i: # Só processa se o nome do filme não for vazio (None)
            movie_id = searchid(i, api_key=YOUR_API_KEY)
            
            # Só busca os provedores se um ID válido foi retornado
            if movie_id is not None:
                search(movie_id, api_key=YOUR_API_KEY)
            else:
                fout.write(f"[{i}] - Nao encontrado na base de dados\n")

tac = time.perf_counter()
print(f'\nFinished in {tac-tic:.4f} seconds')
