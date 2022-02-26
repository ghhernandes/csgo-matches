import unittest

from ...scrapping import matches

class TestScrapping(unittest.TestCase):

    def test_get_lives_match(self):
        match_service = matches.MatchService("https://www.hltv.org/matches/")
        live_matches = match_service.get_live_matches()
        self.assertIsNotNone(live_matches, "No matches found.")
        self.assertGreater(len(live_matches), 0, "0 matches returned.")