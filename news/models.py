from django.db import models

class NewsItem(models.Model):
    by = models.CharField(max_length=100, null=True)
    item_id = models.IntegerField()
    time = models.DateTimeField(editable=True, auto_now_add=True)
    title = models.CharField(max_length=200, null=True)
    score = models.BigIntegerField(default=0, null=True)
    item_type = models.CharField(max_length=100)
    url = models.URLField(max_length=500, null=True)
    api_created = models.BooleanField(default=False, null=True, blank=True)
    kids = models.ManyToManyField('self', blank=True)

    class Meta:
        verbose_name = "Latest News"
        verbose_name_plural = "Latest News"
        ordering = ['-time']

    def __str__(self):
        return f"{self.title} by {self.by}"
