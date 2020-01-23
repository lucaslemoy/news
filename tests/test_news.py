import unittest

from client import News

class NewsTest(unittest.TestCase):
    def test_french_headlines(self):
        news = News()
        articles = news.headlines("fr")
        self.assertEqual(type(articles), list)
        self.assertGreater(len(articles), 0)