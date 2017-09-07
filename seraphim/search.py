from seraphim.context import Context

'''
tab:find
filter_data[keywords][]:deep learning
filter_data[salary][min]:100
filter_data[salary][max]:200
filter_data[locations][]:1692-San Francisco, CA
filter_data[roles][]:Software Engineer
filter_data[types][]:full-time
'''


def build_search_payload(*, keywords=(), min_salary=None, max_salary=None, location=None):
    if min_salary or max_salary:
        if not min_salary:
            min_salary = 0
        if not max_salary:
            max_salary = 200

    data = [('tab', 'find')]
    for keyword in keywords:
        data.append(('filter_data[keywords][]', keyword))
    if min_salary:
        data.append(('filter_data[salary][min]', min_salary))
    if max_salary:
        data.append(('filter_data[salary][max]', max_salary))
    if location:
        data.append(('filter_data[locations][]', location))
    return data


def do_search_startups(context: Context, data: dict):
    context.acquire_csrf_token()
    resp = context.session.post(
        url='https://angel.co/job_listings/startup_ids',
        data=data,
        headers={'X-Requested-With': 'XMLHttpRequest'},
    )
    resp.raise_for_status()
    return resp.json()['ids']
