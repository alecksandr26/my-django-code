from django.test import TestCase
from django.utils import timezone
from django.urls.base import reverse
import datetime
from .models import Question


class QuestionModelTests(TestCase):
    def test_was_published_recetly_with_future_questions(self):
        """Test the Questions model"""
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(question_text="Quien es el mejor course director", pub_date=time)
        
        # Do a simple assert and check if this is an error
        self.assertIs(future_question.was_recent(), False)


    def test_was_now_questions(self):
        """Test this questions"""
        time = timezone.now()
        now_question = Question(question_text = "Is this recent?", pub_date=time)
        self.assertIs(now_question.was_recent(), True)


    def test_wasnt_recent_question(self):
        """Test old questions"""

        time = timezone.now() - datetime.timedelta(days=30)
        old_question = Question(question_text = "Is this an old question?", pub_date = time)
        self.assertIs(old_question.was_recent(), False)



class HomeViewTests(TestCase):
    def test_no_questions(self):
        """if no questions exist, an appropiet message is displayed"""
        response = self.client.get(reverse("home"))
        # Test the response code
        self.assertEqual(response.status_code, 200)

        # Test that we don't have question
        self.assertQuerysetEqual(response.context['object_list'], [])


    def test_questions_not_empty(self):
        """Testing question with future"""
        time = timezone.now()
        future_question = Question(question_text = "This is a test question for the future", pub_date = time)
        future_question.save()
        
        response = self.client.get(reverse('home'))
        self.assertNotEqual([], response.context['object_list'])
        

        
