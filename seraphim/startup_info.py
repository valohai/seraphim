import bs4
import requests

from seraphim.utils import emchunken, get_text


def _query_startup_info(startup_ids, cookies):
    params = list({
        'promotion_event_id': '',
        'tab': 'find',
        'page': 1,
    }.items()) + [('startup_ids[]', startup_id) for startup_id in startup_ids]
    resp = requests.get(
        url='https://angel.co/job_listings/browse_startups_table',
        params=params,
        headers={
            'User-Agent': 'Oispa kaljaa',
        },
        cookies=cookies,
    )
    resp.raise_for_status()
    return resp


def get_startup_info(startup_ids, cookies):
    for startup_ids in emchunken(startup_ids, 10):
        resp = _query_startup_info(startup_ids, cookies)
        yield from parse_startups_table(resp.content)


def parse_startups_table(content):
    soup = bs4.BeautifulSoup(content, 'html.parser')
    for startup in soup.find_all('div', class_='browse_startups_table_row'):
        info = {
            'id': startup['data-id'],
            'name': startup['data-name'],
            'listings': [],
            'www': startup.find('a', class_='website-link').get('href'),
            'employees': get_text(startup, 'div.employees'),
            'locations': get_text(startup, 'div.locations'),
            'tagline': get_text(startup, 'div.tagline'),
            'description': get_text(startup, 'div.details-row.product .description'),
        }
        for listing in startup.find('div', class_='collapsed-job-listings').find_all(class_='collapsed-listing-row'):
            info['listings'].append({
                'title': get_text(listing, 'div.collapsed-title'),
                'tags': get_text(listing, 'div.collapsed-tags'),
                'compensation': get_text(listing, 'div.collapsed-compensation'),
            })
        yield info
