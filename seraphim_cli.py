import json
import os

import click
import sys

from seraphim.context import Context
from seraphim.search import build_search_payload, do_search_startups
from seraphim.startup_info import get_startup_info

context = None


@click.group()
@click.option('-s', '--session', required=True)
def cli(session):
    global context
    context = Context(session_cookie=session)


@cli.command(name='download', help='Download startup info as JSON')
@click.option('-d', '--directory', required=True)
@click.argument('startup_ids', nargs=-1)
def download_startups(directory, startup_ids):
    if not os.path.isdir(directory):
        os.makedirs(directory)

    for info in get_startup_info(context, startup_ids):
        with open('%s/%s.json' % (directory, info['id']), 'w') as outf:
            print('[{id}] {name}'.format_map(info))
            json.dump(info, outf)


@cli.command(name='search', help='Search for startups')
@click.option('--keyword', '-k', 'keywords', multiple=True)
@click.option('--min-salary', type=int)
@click.option('--max-salary', type=int)
@click.option('--location', '-l')
def search_startups(keywords, min_salary, max_salary, location):
    data = build_search_payload(
        keywords=keywords,
        min_salary=min_salary,
        max_salary=max_salary,
        location=location,
    )
    startup_ids = do_search_startups(context, data)
    json.dump(startup_ids, sys.stdout)


if __name__ == '__main__':
    cli()
