import requests

from requests.exceptions import ReadTimeout, ConnectionError, RequestException
import logging


def get(url, params=None, timeout=5):
    requests.adapters.DEFAULT_RETRIES = 5  # 增加重连次数
    s = requests.session()
    s.keep_alive = False

    try:
        return requests.get(url, params=params, timeout=timeout)
    except ConnectionError:
        logging.exception('ConnectionError, %s', url)
        # pass
    except RequestException:
        logging.exception('RequestException, %s', url)
        # pass


def get_json(url, params=None, timeout=8):
    resp = get(url, params=params, timeout=timeout)
    if resp.status_code != 200:
        logging.warning('http request wrong happen {}'.format(resp.reason))
        return ''
    return resp.json()


def post(url, data=None, json=None, timeout=5):
    requests.adapters.DEFAULT_RETRIES = 5
    s = requests.session()
    s.keep_alive = False

    try:
        return requests.post(url, data=data, json=json, timeout=timeout)
    except ConnectionError:
        logging.exception('ConnectionError, %s', url)
        # pass
    except RequestException:
        logging.exception('RequestException, %s', url)
        # pass
