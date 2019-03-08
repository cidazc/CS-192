from django.db import models

# Create your models here.

class Translation(models.Model):
	origin_language = models. CharField(max_length = 250, default='Filipino')
	target_language = models. CharField(max_length = 250, default='English')
	origin_text = models. CharField(max_length = 250, default='Kamusta')
	target_text = models. CharField(max_length = 250, default='How are you')
	context_examples = models. CharField(max_length = 500, default='Kamusta ka ba? -> How are you already?')
	upvotes = models.IntegerField(default=100000)
	downvotes = models.IntegerField(default=10)


class Search(models.Model):
    search_text = models.CharField(max_length=255, default='Add a value here', blank=True)
    def __str__(self):
        return '%s' % self.search_text
