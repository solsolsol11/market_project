from django.forms import ModelForm

from qna.models import Question


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['body']