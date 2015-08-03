from django.db import models
from django.conf import settings
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

# Create your models here.
class Question(models.Model):
	text = models.TextField()
	active = models.BooleanField(default=True)
	draft = models.BooleanField(default=False)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	#answers = models.ManyToManyField('Answer')

	def __unicode__(self):
		return self.text[:10]

class Answer(models.Model):
	questions = models.ForeignKey(Question)
	text = models.CharField(max_length=120)
	active = models.BooleanField(default=True)
	draft = models.BooleanField(default=False)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __unicode__(self):
		return self.text[:10]

LEVELS = (
	('Expert', 'Expert'),
	('Intermediate', 'Intermediate'),
	('Beginner', 'Beginner'),
	)

class UserAnswer(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	question = models.ForeignKey(Question)
	my_answer = models.ForeignKey(Answer, related_name='user_answer')
	my_answer_level = models.CharField(max_length=50, choices=LEVELS)
	my_points = models.IntegerField(default=-1)
	tutor_answer = models.ForeignKey(Answer, null=True, blank=True, related_name='match_answer')
	tutor_answer_level = models.CharField(max_length=50, choices=LEVELS)
	tutor_points = models.IntegerField(default=-1)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __unicode__(self):
		return self.my_answer.text[:10]
def score_importance(importance_level):
	if importance_level == "Expert":
		points = 300
	if importance_level == "Intermediate":
		points = 200
	if importance_level == "Beginner":
		points = 100
	elif importance_level == "No Experience":
		points = 0
	else:
		points = 0
	return points

@receiver(pre_save, sender=UserAnswer)
def update_user_answer_score(sender, instance, *args, **kwargs):
	my_points = score_importance(instance.my_answer_level)
	instance.my_points = my_points
	tutor_points = score_importance(instance.tutor_answer_level)
	instance.tutor_points = tutor_points
# def update_user_answer_score(sender, instance, created, *args, **kwargs):
# 	print sender
# 	print instance
# 	print created
# 	if instance.my_points == -1:
# 		my_points = score_importance(instance.my_answer_level)
# 		instance.my_points = my_points
# 		instance.save()
# 	if instance.tutor_points == -1:
# 		tutor_points = score_importance(instance.tutor_answer_level)
# 		instance.tutor_points = tutor_points
# 		instance.save()
		
# post_save.connect(update_user_answer_score, sender=UserAnswer)