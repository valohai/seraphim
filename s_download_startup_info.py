import json

import click
import os

from seraphim.startup_info import get_startup_info


@click.command()
@click.option('-s', '--session', required=True)
@click.option('-d', '--directory', required=True)
@click.argument('startup_ids', nargs=-1)
def main(session, directory, startup_ids):
    cookies = {
        '_angellist': session,
    }
    if not os.path.isdir(directory):
        os.makedirs(directory)

    for info in get_startup_info(startup_ids, cookies):
        with open('%s/%s.json' % (directory, info['id']), 'w') as outf:
            print('[{id}] {name}'.format_map(info))
            json.dump(info, outf)


if __name__ == '__main__':
    main()
