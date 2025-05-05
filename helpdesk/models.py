from django.db import models

from personal.models import Workstation, Operator


class Application(models.Model):
    category = models.CharField('Category', max_length=64)
    location = models.CharField('Location', max_length=32, blank=True, null=True)
    operator = models.ForeignKey(
        Operator,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    workstation = models.ForeignKey(
        Workstation,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    description = models.TextField('Description', default='', blank=True)
    # screenshot = models.ImageField(
    #     upload_to='screenshot_application/%d-%m-%Y',
    #     storage=UUIDFileStorage(),
    #     blank=True,
    #     null=True,
    # )
    screenshot_url = models.TextField(
        'Screenshot',
        default='',
        blank=True,
    )
    executor = models.ForeignKey(
        Operator,
        related_name='Executor',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    signer = models.ForeignKey(
        Operator,
        related_name='Signer',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    # cancel | new | waiting | process | complete
    status = models.CharField(
        'Status',
        max_length=32,
        default='new'
    )
    report_id = models.BigIntegerField(
        'Report message id',
        blank=True,
        null=True
    )
    layout = models.CharField('Layout', max_length=16, blank=True, null=True)
    step = models.PositiveSmallIntegerField('Step', default=1, blank=True, null=True)
    owner_tg = models.PositiveSmallIntegerField('Owner tg', blank=True, null=True)
    updated_at = models.DateField('Date of updating', auto_now=True)
    created_at = models.DateField('Date of creation', auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.category


class Button(models.Model):
    title = models.CharField('Title btn', max_length=32)
    type = models.CharField('Type btn', max_length=32, default='category', blank=True, null=True)
    order = models.PositiveSmallIntegerField('Order btn', default=1, blank=True, null=True)
    size = models.CharField('Size btn', max_length=16, default='small', blank=True, null=True)
    departament = models.CharField('Departament', max_length=32, blank=True, null=True)
    layout = models.CharField('Layout category', max_length=16, blank=True, null=True)
    problems = models.ManyToManyField('Button', blank=True)
    updated_at = models.DateField('Date of updating', auto_now=True)
    created_at = models.DateField('Date of creation', auto_now_add=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

