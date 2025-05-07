from django.db import models


class AntispamDictionary(models.Model):
    word = models.CharField('Word', max_length=128, unique=True)
    value = models.SmallIntegerField('Value')
    updated_at = models.DateField('Date of updating', auto_now=True)
    created_at = models.DateField('Date of creation', auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.word


class PublicChatLog(models.Model):
    username = models.CharField('Time msg', max_length=255)
    full_time = models.CharField('Time msg', max_length=128)
    text = models.TextField('Text')
    chat_id = models.BigIntegerField('Chat id')
    msg_id = models.BigIntegerField('Msg id')
    user_id = models.BigIntegerField('User id')
    sum_spam = models.SmallIntegerField('Sum spam')
    updated_at = models.DateField('Date of updating', auto_now=True)
    created_at = models.DateField('Date of creation', auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.username
