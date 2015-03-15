import sys
import requests

TIMEOUT = 4


def get_mirror_urls():
    mirror_url = 'http://mirrors.ubuntu.com/mirrors.txt'
    try:
        response = requests.get(mirror_url)
    except requests.exceptions.ConnectionError:
        print 'Connection Error: {}'.format(mirror_url)
        sys.exit(1)
    return response.content.split('\n')


def time_urls(urls):
    n_urls = len(urls)
    response_times = []
    for i, mirror_url in enumerate(urls):
        try:
            resp = requests.get(mirror_url, timeout=TIMEOUT)
        except requests.exceptions.ConnectionError:
            print 'Connection Error (skipping): {}'.format(mirror_url)
            continue
        except requests.exceptions.Timeout:
            print 'Connection Timeout (skipping): {}'.format(mirror_url)
            continue
        print '{}/{} {} {}'.format(i + 1, n_urls, resp.elapsed, mirror_url)
        response_times.append((resp.elapsed, mirror_url))
    response_times.sort()

    return response_times


def print_top(response_times, top=3):
    print 'TOP {}'.format(top)
    for i in range(top):
        try:
            elapsed, url = response_times[i]
        except IndexError:
            break
        print elapsed.microseconds, url


def main():
    urls = get_mirror_urls()
    times = time_urls(urls)
    print '-' * 79
    print_top(times, 3)
    print '-' * 79
    print times[0][1]


if __name__ == '__main__':
    main()

