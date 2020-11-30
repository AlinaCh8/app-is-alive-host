import requests
from requests.exceptions import Timeout


def is_alive_host(hostname):

    hostname = hostname.replace('https://', '').replace('http://',
                                                        '').split('/')[0]
    hostname = 'http://' + hostname

    try:
        request_status = requests.get(hostname, timeout=3)
        status = requests.head(hostname)
        #if 100 <= status.status_code < 400:
            #print('Ошибки нет')
        #else:
            #print('Ошибка')
    except Timeout:
        print('Время ожидания запроса истекло')

    return 100 <= status.status_code < 400


is_alive_host('https://panoraven.com/bird')