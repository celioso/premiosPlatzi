import datetime

from django.test import TestCase
from django.urls.base import reverse
from django.utils import timezone
from django.contrib import admin
from django import forms
from django.forms.models import BaseInlineFormSet

from .models import Question,Choice

#se van a testear 
# Models
# Vistas
class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_questions(self):
        """"was_published_recently return False for question whose pub_date is in the future"""
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(question_text="¿quién es el mejor Course de Platzi?", pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_future_questions(self):
        """"was_published_recently return False for question whose pub_date is in the future"""
        time = timezone.now()
        present_question = Question(question_text="¿quién es el mejor Course de Platzi?", pub_date=time)
        self.assertIs(present_question.was_published_recently(), True)

    def test_was_published_recently_with_future_questions(self):
        """"was_published_recently return False for question whose pub_date is in the future"""
        time = timezone.now() - datetime.timedelta(days=-1)
        past_question = Question(question_text="¿quién es el mejor Course de Platzi?", pub_date=time)
        self.assertIs(past_question.was_published_recently(), False)

def create_question(question_text, days):
    """
    Create a question with the given "question_test", and published the given numbre of day offset to now (negative for question published in the past, positive for questions that have yet to be published)
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        """If not question exist, an appropiate message is displayed"""
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context["latest_question_list"], [])

    '''
    aporte de compañeros al reto
    def test_questions_with_future_pub_date(self):
        """Questions with date greater to timezone.now shouldn't be displayed"""
        time = timezone.now() + datetime.timedelta(days = 30)
        future_question = Question(question_text = "This is a Question for the test", pub_date = time)
        future_question.save()
        response = self.client.get(reverse('polls:index'))
        self.assertNotIn(future_question, response.context['latest_question_list'],)'''
    
    def test_future_question(self):
        """
        Question with a pub_date in the future aren't displayed on the index page.
        """
        create_question("Future question", days=30)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context["latest_question_list"],[])

    def test_past_question(self):
        """
        Question wiht a pub_date in the past are displayed on the index page
        """
        question = create_question("Past question", days=-10)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(response.context["latest_question_list"],[question])

    def test_future_question_and_past_question(self):
        """
        Even is both past and future question exist, only past question are displayed.
        """
        past_question= create_question(question_text="Past question", days=-30)
        future_question= create_question(question_text="Future question", days=30)
        response =self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(
            response.context["latest_question_list"],
            [past_question]
        )


    def text_two_past_question(self):
        """The questions index page may display multiple questions"""
        past_question1= create_question(question_text="Past question 1", days=-30)
        past_question2= create_question(question_text="Past question 2", days=-40)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(
            response.context["latest_question_list"],
            [past_question1, past_question2]
        )

    def text_two_future_question(self):
        """The questions index page may display multiple future questions"""
        future_question1= create_question(question_text="Future question 1", days=50) 
        future_question2= create_question(question_text="Future question 2", days=60)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerysetEqual(
            response.context["latest_question_list"],
            [future_question1, future_question2]
        )

class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        """
        The detail view of a question with a pub_date in the future return a 404 error not found
        """
        future_question = create_question(question_text="Future question",days=30)
        url = reverse("polls:detail", args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """
        The detail view of a question with a pub_date in the past displays the question's text
        """
        past_question = create_question(question_text="Past question",days=-30)
        url = reverse("polls:detail", args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.question_text)

#testin th lilimc8384
# Creando tests para DetailView

'''from django.contrib import admin
from .models import Question,Choice
from django import forms
from django.forms.models import BaseInlineFormSet

class AtLeastOneRequiredInlineFormSet(BaseInlineFormSet):

    def clean(self):
        """Check that at least one choice has been entered."""
        super(AtLeastOneRequiredInlineFormSet, self).clean()
        if any(self.errors):
            return
        if not any(cleaned_data and not cleaned_data.get('DELETE', False)
            for cleaned_data in self.cleaned_data):
            raise forms.ValidationError('At least one choice required.')


class ChoicesInline(admin.TabularInline):
    model = Choice
    formset= AtLeastOneRequiredInlineFormSet
    extra = 1
    exclude= ['votes']

class QuestionAdmin(admin.ModelAdmin):
    inlines=(ChoicesInline,)

    def save_formset(self, request, form, formset, change):
        instances = formset.save(commit=False)
        for obj in formset.deleted_objects:
            obj.delete()        
        for instance in instances:
            instance.save()            


admin.site.register(Question, QuestionAdmin)
#admin.site.register(Choice)'''

#testing the briamex
# toca crear un archivo nombrado froms.py
'''
from django.contrib import admin

from .models import Question, Choice
from .froms import RequiredInlineFormSet


# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    exclude = ['votes']
    extra = 2
    formset = RequiredInlineFormSet # or AtLeastOneFormSet

class QuestionAdmin(admin.ModelAdmin):
    inlines = [
        ChoiceInline,
    ]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)'''