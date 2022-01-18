from django.test import TestCase

import datetime
from django.utils import timezone
from django.urls import reverse

from .models import Question




# 创建模型测试实例
class QuestionModelTests(TestCase):

    # 如果pub_date是未来的时间，那么返回应该是false
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    # 如果pub_date是晚于当前一天的时间，那么也返回false
    def test_was_published_recently_with_older_question(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        older_question = Question(pub_date=time)
        self.assertIs(older_question.was_published_recently(), False)

    # 如果pub_date是最近一天的时间，则返回true
    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

# 新增视图测试
# 公用函数创建投票问题
def create_question(question_text, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)

# 问题列表视图测试类
class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
        question = create_question(question_text="Past question", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], [question])

    def test_future_question(self):
        question = create_question(question_text="Future question", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available.")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])
        
    def test_future_question_and_past_question(self):
        """
        Even if both past and future questions exist, only past questions
        are displayed.
        """
        past_question = create_question(question_text="Past question.", days=-30)
        future_question = create_question(question_text="Future question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [past_question]
        )

    def test_two_past_questions(self):
        """
        The questions index page may display multiple questions.
        """
        question1 = create_question(question_text="Past question 1.", days=-30)
        question2 = create_question(question_text="Past question 2.", days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(
            response.context['latest_question_list'],
            [question2, question1]
        )


# 问题详情页视图测试
class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        future_question = create_question(question_text='Future question', days=5)
        response = self.client.get(reverse('polls:detail', args = (future_question.id,)))
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        past_question = create_question(question_text='Past question', days=-5)
        response = self.client.get(reverse('polls:detail', args = (past_question.id,)))
        self.assertContains(response, past_question.question_text)
