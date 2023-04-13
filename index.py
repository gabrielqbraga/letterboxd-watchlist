import requests, json, csv, time

YOUR_API_KEY = 'INSERT_YOUR_API_HERE'


tic = time.perf_counter()


with open('watchlist.csv', 'r') as fin:
    csvreader = csv.reader(fin)
    rows = []
    for row in csvreader:
        rows.append(row)
    rows.pop(0)
    watchlist = [None]*len(rows)
    for i in range(len(rows)):
        watchlist[i] = (rows[i][1])





def searchid(moviename, api_key):
    x = requests.get ('https://api.themoviedb.org/3/search/movie?api_key='+str(api_key)+'&query='+str(moviename).replace(' ','+'))
    movieresults = json.loads(x.text)
    movieinfo = movieresults['results']
    moviedetails = movieinfo[0]
    movieid = moviedetails['id']
    global movietitle
    movietitle=moviename
    return movieid
    #print(movieid)


def search(movieid, api_key):
    x = requests.get('https://api.themoviedb.org/3/movie/'+str(movieid)+'/watch/providers?api_key='+str(api_key))
    streaminglist = json.loads(x.text)
    streaminglistresults = streaminglist['results']
    
    if 'BR' in streaminglistresults:
        brstreaminglist = streaminglistresults['BR']
    
        if 'flatrate' in brstreaminglist:
            flatrate = brstreaminglist['flatrate']
            for entry in flatrate:
                print (movietitle+' - '+entry['provider_name'])
                fout.write(movietitle+' - '+entry['provider_name']+'\n')
        else:
            print(movietitle+" is not available in any streaming service")
            fout.write(movietitle+" is not available in any streaming service\n")
    else:
        print(movietitle+" is not available in any streaming service")
        fout.write(movietitle+" is not available in any streaming service\n")


with open('results.txt', 'a') as fout:
    for i in watchlist:
        search (searchid(i, API_KEY = YOUR_API_KEY), API_KEY = YOUR_API_KEY)



tac = time.perf_counter()
print(f'Finished in {tac-tic:.4f} seconds')
