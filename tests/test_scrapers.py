from backend.scrapers import Asura

import pytest

@pytest.fixture
def asura_scraper():
    return Asura("https://asura.gg/manga/solo-leveling/")

def test_asura(asura_scraper):
    # pick a completed manhwa from asurascans
    data = asura_scraper.get()
    
    expected = {'status': 'Completed', 'latest_chapter': 179, 
     'title': 'Chapter 179',
     'last_updated': 'December 29, 2021', 
     'url': 'https://asura.gg/solo-leveling-chapter-179-end/', 'slug': 'solo-leveling'}

    assert data == expected