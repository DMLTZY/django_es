# -*- coding: utf-8 -*-
import json
import requests

from django.conf import settings


def search(request, page=1, page_size=20, field='text'):
    """
    去es中查找
    :param request: 搜索框内容数组
    :param page: 搜索的页号
    :param page_size: 每页展示数量
    :param field: 搜索字段
    :return:
    """
    num = len(request)
    must_list = []
    for i in range(num):
        must_list.append({
            "match": {field: request[i]}
        })

    data = {
        "from": (page - 1) * page_size,
        "size": page_size,
        "query": {
            "bool": {
                "must": must_list
            }
        }
    }
    res = requests.post('{}_search'.format(settings.ES_HOST),
                        data=json.dumps(data))

    if res.status_code == 200:
        res = json.loads(res.text)
        return res.get('hits')
    else:
        return False
