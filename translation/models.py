from django.db import models

# Create your models here.

class Translation(models.Model):
	origin_language = models. CharField(max_length = 250, default='Filipino')
	target_language = models. CharField(max_length = 250, default='English')
	origin_text = models. CharField(max_length = 250, default='')
	target_text = models. CharField(max_length = 250, default='')
	context_examples = models. CharField(max_length = 500, default='')
	upvotes = models.IntegerField(default=0)
	downvotes = models.IntegerField(default=0)


class Search(models.Model):
    search_text = models.CharField(max_length=255, default='Add a value here', blank=True)
    def __str__(self):
        return '%s' % self.search_text

class Translation_origin_text(models.Model):
	origin_text = models. CharField(max_length = 250)
