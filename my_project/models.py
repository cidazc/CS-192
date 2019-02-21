from django.db import models


class Translation(models.Model):
	origin_language = models. CharField(max_length = 250)
	target_language = models. CharField(max_length = 250)
	origin_text = models. CharField(max_length = 250)
	target_text = models. CharField(max_length = 250)
	context_examples = models. CharField(max_length = 500)
	upvotes = models.IntegerField()
	downvotes = models.IntegerField()
