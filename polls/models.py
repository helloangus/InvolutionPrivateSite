import datetime
from django.db import models
from django.utils import timezone


# 创建Question模型，负责描述问题和发布时间
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    # 判断是否为最近一天上传的数据
    def was_published_recently(self):
        now = timezone.now()
        return ((self.pub_date <= now) and (self.pub_date >= timezone.now()-datetime.timedelta(days=1)))

# 创建Choice模型，负责选项描述和展示当前得怕票数
class Choice(models.Model):
    # 创建外键，与Question一一对应
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text