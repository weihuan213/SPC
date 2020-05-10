from django.http import HttpResponse
from .models import Notice
import json


def _get_notice():
    """get notice"""
    notice = Notice.objects.all().order_by('-create_time')
    if notice.count() > 0:
        notice = notice[0]
        return notice.content + '<p style="text-align:right;margin-top:0.5em;">%s</p>' % notice.create_time.strftime(
            "%Y-%m-%d")
    else:
        return u'暂无公告'


def get_notice(request):
    data = {}
    data['code'] = '0'
    data['message'] = 'OK'
    data['notice'] = _get_notice()

    # 返回json数据
    return HttpResponse(json.dumps(data), content_type="application/json")