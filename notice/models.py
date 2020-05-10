# coding:utf-8
from django.db import models


class Notice(models.Model):
    content = models.TextField(max_length=500, verbose_name='内容')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创造时间")

    def __unicode__(self):
        return u'%s' % self.content

    class Meta:
        ordering = ['-create_time']
        verbose_name = '公告'
        verbose_name_plural = verbose_name
