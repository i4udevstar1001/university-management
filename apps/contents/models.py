from django.db import models

from . import managers
from ..accounts.models import User
from ..core.models import TimeStampedModel


class News(TimeStampedModel):

    title = models.CharField(
        max_length=100
    )

    body = models.TextField(
        null=True,
        blank=True
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='as_news_author'
    )

    is_published = models.BooleanField(
        default=False
    )

    is_deleted = models.BooleanField(
        default=False
    )

    audiences = models.ManyToManyField(
        User
    )

    objects = models.Manager()
    availables = managers.AvailableNewsManager()
    deleteds = managers.DeletedNewsManager()
    publisheds = managers.PublishedNewsManager()
    pendings = managers.PendingNewsManager()

    def __str__(self):
        return f'{self.id} - {self.title}'


class NewsAudiences(models.Model):

    news = models.ForeignKey(
        News,
        on_delete=models.CASCADE
    )

    audience = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    is_read = models.BooleanField(
        default=False
    )

    recent_read_on = models.DateTimeField(
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.news} - ({self.audience})'


class Notifications(TimeStampedModel):

    STATUS_SENT = 'S'
    STATUS_PENDING = 'P'
    STATUS = (
        (STATUS_SENT, '已发送'),
        (STATUS_PENDING, '未发送'),
    )

    title = models.CharField(
        max_length=100
    )

    body = models.TextField()

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='as_notifications_author'
    )

    status = models.CharField(
        max_length=1,
        choices=STATUS,
        default=STATUS_PENDING
    )

    is_deleted = models.BooleanField(
        default=False
    )

    audiences = models.ManyToManyField(
        User
    )

    objects = models.Manager()
    sents = managers.SentNotificationsManager()
    pendings = managers.PendingNotificationsManager()
    availables = managers.AvailableNotificationsManager()
    deleteds = managers.DeletedNotificationsManager()

    def __str__(self):
        return f'{self.id} - {self.title}'


class NotificationsAudiences(models.Model):

    notification = models.ForeignKey(
        Notifications,
        on_delete=models.CASCADE
    )

    audience = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    is_read = models.BooleanField(
        default=False
    )

    recent_read_on = models.DateTimeField(
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.notification} - ({self.audience.name})'
