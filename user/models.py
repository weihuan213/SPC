from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='用户')
    nickname = models.CharField(max_length=20, verbose_name='昵称')

    def __str__(self):
        return "<profile:%s for %s>" % (self.nickname, self.user.username)

    class Meta:
        verbose_name = '昵称'
        verbose_name_plural = verbose_name


def get_nickname(self):
    if Profile.objects.filter(user=self).exists():
        profile = Profile.objects.get(user=self)
        return profile.nickname
    else:
        return ''


def have_nickname(self):
    return Profile.objects.filter(user=self).exists()


User.get_nickname = get_nickname
User.have_nickname = have_nickname
