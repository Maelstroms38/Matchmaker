from django import forms

from .models import LEVELS, Answer, Question

class UserResponseForm(forms.Form):
	question_id = forms.IntegerField()
	answer_id = forms.IntegerField()
	importance_level = forms.ChoiceField(choices=LEVELS)
	tutor_answer_id = forms.IntegerField()
	tutor_importance_level = forms.ChoiceField(choices=LEVELS)

	def clean_answer_id(self):
		answer_id = self.cleaned_data.get('answer_id')
		try:
			obj = Answer.objects.get(id=answer_id)
		except:
			raise forms.ValidationError('There was an error, please try again')
		return answer_id

	def clean_question_id(self):
		question_id = self.cleaned_data.get('question_id')
		try:
			obj = Question.objects.get(id=answer_id)
		except:
			raise forms.ValidationError('There was an error, please try again')
		return question_id
	def tutor_clean_answer_id(self):
		tutor_answer_id = self.cleaned_data.get('tutor_answer_id')
		try:
			obj = Answer.objects.get(id=tutor_answer_id)
		except:
			if tutor_answer_id == -1:
				return tutor_answer_id
			else:
				raise forms.ValidationError('There was an error, please try again')
		return tutor_answer_id