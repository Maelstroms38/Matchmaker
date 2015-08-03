from django.contrib.auth import get_user_model
from questions.model import UserAnswer

User = get_user_model()
users = User.object.all() [user1, user2]
all_user_answers = UserAnswer.objects.all().order_by("user__id")

UserAnswer.objects.filter(user=maestro)

def get_match(user_a, user_b):
	user_a_answers = UserAnswer.objects.filter(user=user=user_a)[0]
	user_b_answers = UserAnswer.objects.filter(user=user=user_b)[0]

	if user_a_answers.questiond.id == user_b_answers.question.id:
		user_a_answer = user_a_answers.my_answer
		user_a_pref = user_a_answers.tutor_answer
		user_b_answer = user_b_answers.my_answer
		user_b_pref = user_b_answers.tutor_answer

		if user_a_answer == user_b_pref:
			print "%s fits with %s's preference" %(user_a_answers.user.username, user_b_pref.user.username)
		if user_a_pref == user_b_answer:
			print "user b with a's level" %(user_a_answers.user.username, user_b_answers.user.username)
		if user_a_answer == user_b_pref && user_a_pref == user_b_answer:
			print "ideal answers for both"