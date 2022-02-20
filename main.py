from scrapping import matches, schemas

if __name__ == '__main__':
    match_service = matches.MatchService("https://www.hltv.org/matches/") 

    print('Live CS:GO matches')
    for match in match_service.get_live_matches():
        print(match)

    print('\nUpcoming CS:GO matches')
    for match in match_service.get_upcoming_matches():
        print(match)