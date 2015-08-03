from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

from .models import Question, Answer, UserAnswer
from .forms import UserResponseForm
# Create your views here.
def single(request, id):
	
	if request.user.is_authenticated():

		queryset = Question.objects.all().order_by('-timestamp') 
		instance = get_object_or_404(Question, id=id)
		try:
			user_answer = UserAnswer.objects.get(user=request.user, question=instance)
		except UserAnswer.DoesNotExist:
			user_answer = UserAnswer.objects.get(user=request.user, question=instance)
		except UserAnswer.MultipleObjectsReturned:
			user_answer = UserAnswer()

		form = UserResponseForm(request.POST or None)
		if form.is_valid(): 
			print form.cleaned_data
			question_id = form.cleaned_data.get('question_id')
			answer_id = form.cleaned_data.get('answer_id')

			importance_level = form.cleaned_data.get('importance_level')
			tutor_importance_level = form.cleaned_data.get('tutor_importance_level')
			tutor_answer_id = form.cleaned_data.get('tutor_answer_id')

			question_instance = Question.objects.get(id=question_id)
			answer_instance = Answer.objects.get(id=answer_id)

			user_answer = UserAnswer() #create answer instacne
			user_answer.user = request.user
			user_answer.question = question_instance
			user_answer.my_answer = answer_instance
			user_answer.my_answer_importance = importance_level
			if tutor_answer_id != -1:
				tutor_answer_instance = Answer.objects.get(id=tutor_answer_id)
				user_answer.tutor_answer = tutor_answer_instance
				user_answer.tutor_importance = tutor_importance_level
			else:
				user_answer.tutor_answer = None
				user_answer.tutor_importance = "No Experience"
			user_answer.save()

			#UserAnswer.objects.create()

			next_q = Question.objects.order_by("?").first() #? is random
			return redirect("question_single", id=next_q.id) #redirect to next question
		context = {
			"form": form,
			"instance": instance,
			"user_answer": user_answer,
		}
		return render(request, "questions/single.html", context)
	else:
		raise Http404

def home(request):
	if request.user.is_authenticated():
		form = UserResponseForm(request.POST or None)
		if form.is_valid(): 
			print form.cleaned_data
			question_id = form.cleaned_data.get('question_id')
			answer_id = form.cleaned_data.get('answer_id')
			question_instance = Question.objects.get(id=question_id)
			answer_instance = Answer.objects.get(id=answer_id)

		queryset = Question.objects.all().order_by('-timestamp') #.filter(full_name__iexact="Justin")
		#print(SignUp.objects.all().order_by('-timestamp').filter(full_name__iexact="Justin").count())
		instance = queryset[1]
		context = {
			"form": form,
			"instance": instance,
		}
		return render(request, "questions/home.html", context)
	else:
		raise Http404