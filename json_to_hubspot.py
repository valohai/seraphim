import json

import click


def mangle_employees(employees):
    employees = employees.replace('employees', '').strip()
    if not employees:
        return ''
    if '-' in employees:
        return employees.split('-')[0]
    return employees


@click.command()
@click.option('--group', '-g', required=True)
@click.argument('json_files', nargs=-1)
def main(group, json_files):
    datas = []
    for filename in json_files:
        with open(filename, 'r') as infp:
            datas.append(json.load(infp))
    formatted_rows = [
        {
            'Group': group,
            'Domain': d['www'],
            'Name': d['name'],
            'City': d['locations'].split(',')[0],
            'Number of Employees': mangle_employees(d['employees']),
        }
        for d in datas
    ]
    keys = list(formatted_rows[0].keys())
    print(','.join(keys))
    for row in formatted_rows:
        print(','.join(row.get(key, '') for key in keys))


if __name__ == '__main__':
    main()
