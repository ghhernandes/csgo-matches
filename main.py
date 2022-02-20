from scrapping import matches, schemas

def print_match(match: schemas.Match) -> None:
    print(f"\t({match.info.time}) {match.event.name}")
    print(f"\t\t{match.teams[0].name}")
    print(f"\t\t{match.teams[1].name}")

if __name__ == '__main__':
    match_service = matches.MatchService("https://www.hltv.org/matches/")   
    
    print('Live CS:GO matches')
    for match in match_service.get_live_matches():
        print_match(match)

    print('\nUpcoming CS:GO matches')
    for match in match_service.get_upcoming_matches():
        print_match(match)
    