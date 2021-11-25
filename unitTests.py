import unittest

import webScrapeUtils


class LetterboxdScrapingTests(unittest.TestCase):
    filmList = webScrapeUtils.getLetterboxdListFilms("kalekdan", "letterboxd-tools-testlist")
    def testListScrapingFindsFilm(self):
        self.assertGreater(len(self.filmList), 0)
    def testListScrapingContainsFilm(self):
        self.assertIn("Skyfall", self.filmList)
    def testListScrapingGetsAllFilms(self):
        self.assertEqual(3, len(self.filmList))

class IMDBScrapingTests(unittest.TestCase):
    filmList = webScrapeUtils.getIMDBTopX(1)
    def testIMDBFilmCount(self):
        self.assertGreater(len(self.filmList),0)