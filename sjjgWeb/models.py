#-*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from ckeditor.fields import RichTextField



# Create your models here.

#试卷信息表
class Tests(models.Model):
    num = models.SmallIntegerField(verbose_name='试卷编号')
    bool_score = models.SmallIntegerField(verbose_name='每道判断题分值',default=3)
    testName = models.CharField(verbose_name='试卷介绍',default='试卷',max_length=30)
    choice_score = models.SmallIntegerField(verbose_name='选择题分值',default=3)
    max_time = models.SmallIntegerField(verbose_name='考试时间')
    is_open = models.BooleanField(verbose_name='是否开卷',default=True)
    class Meta:
        verbose_name = '在线测试试卷'
        verbose_name_plural = verbose_name
        ordering = ['-num']
    def __unicode__(self):
        return u'试卷'+ unicode(self.num)


#选择题表
class Choice_question(models.Model):
    correct_choice = (('A','A'),('B','B'),('C','C'),('D','D'),('E','E'),('F','F'))
    num = models.SmallIntegerField(verbose_name='题目号')
    question = models.CharField(max_length=200,verbose_name='题目')
    choice_A = models.CharField(max_length=100,verbose_name='选项A',blank=True,null=True)
    choice_B = models.CharField(max_length=100,verbose_name='选项B',blank=True,null=True)
    choice_C = models.CharField(max_length=100,verbose_name='选项C',blank=True,null=True)
    choice_D = models.CharField(max_length=100,verbose_name='选项D',blank=True,null=True)
    choice_E = models.CharField(max_length=100,verbose_name='选项E',blank=True,null=True)
    choice_F = models.CharField(max_length=100,verbose_name='选项F',blank=True,null=True)
    correct = models.CharField(choices=correct_choice,max_length=2,verbose_name='答案')
    test = models.ForeignKey(Tests)
    class Meta:
        verbose_name = '选择题'
        verbose_name_plural = verbose_name
        ordering = ['num']

    def __str__(self):
        return str(self.num)+self.question[5]+"..."

#判断题表
class Bool_question(models.Model):
    bool_choice = ((True,'正确'),(False,'错误'))
    num = models.SmallIntegerField(verbose_name='题目号')
    question = models.CharField(max_length=150,verbose_name='问题')
    correct = models.BooleanField(verbose_name='正确答案',default=True,choices=bool_choice)
    test = models.ForeignKey(Tests)
    class Meta:
        verbose_name = '判断题'
        verbose_name_plural = verbose_name
        ordering = ['num']

#问答题表
class Answer_question(models.Model):
    num = models.SmallIntegerField(verbose_name='题目号')
    question = models.CharField(max_length=150,verbose_name='问题')
    correct = models.CharField(max_length=500,verbose_name='答案',blank=True,null=True)
    test = models.ForeignKey(Tests)
    class Meta:
        verbose_name = '问答题'
        verbose_name_plural = verbose_name
        ordering = ['num']


#管理员或者具有该权限的老师
class User(AbstractUser):
    sex = models.BooleanField(default=True,verbose_name='性别')
    picture = models.ImageField(verbose_name='头像',blank=True,null=True)
    class Meta:
        verbose_name = '所有用户'
        verbose_name_plural = verbose_name
#作业表


#学生表
class Student(User):
    s_class = models.CharField(verbose_name='班级',max_length='10',blank=True,null=True,default='未填写班级')
    class Meta:
        verbose_name = '学生'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.last_name+self.first_name + u'--班级:'+ self.s_class + u'--用户名:'+self.username
#上传作业的表
class uploadHomework(models.Model):
    content = models.FileField(upload_to='./upload/homework',verbose_name='作业文件')
    homeworkId = models.CharField(max_length=10)
    student = models.ForeignKey(Student)
    class Meta:
        verbose_name = '作业上传'
        verbose_name_plural = verbose_name

#学生的分数表
class Score(models.Model):
    testId = models.ForeignKey(Tests)
    student = models.ForeignKey(Student,related_name='sscore_set')
    score = models.SmallIntegerField(verbose_name='学生成绩')
    addTime = models.DateTimeField(verbose_name='提交时间',default=timezone.now)
    class Meta:
        verbose_name = '学生分数'
        verbose_name_plural = verbose_name





#精品课程表
class MyCourse(models.Model):
    courseName = models.CharField(max_length=10)
    courseIntro = models.TextField(max_length=2000)
    teachProgramming = models.FileField(upload_to='./upload/MyCourse')
    experimentPro = models.FileField(upload_to='./upload/MyCourse')

#试题库
class TestData(models.Model):
    testsName = models.CharField(max_length=10,verbose_name='试题名字')
    content = models.FileField(upload_to='./upload/testData',verbose_name='上传试题库')
    class Meta:
        verbose_name = '试题库'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.testsName


#互动表
class comment(models.Model):
    content = models.TextField(max_length=500,verbose_name='评论内容')
    user = models.ForeignKey(User,verbose_name='评论者Id')
    commentDate = models.DateTimeField(verbose_name='评论时间',default=timezone.now)
    class Meta:
        verbose_name = '留言管理'
        verbose_name_plural = verbose_name
        ordering = ['-commentDate']
    def __unicode__(self):
        return unicode(self.user) + u'的评论'

class ReComment(models.Model):
    content = models.TextField(max_length=500,verbose_name='你的回复')
    toComment = models.ForeignKey(comment)
    class Meta:
        verbose_name = '你的回复'
        verbose_name_plural = verbose_name

#介绍性页面
class Information(models.Model):
    nav_choice = ((u'11',u'课程介绍'),(u'12',u'课程大纲'),(u'21',u'团队负责人'),(u'14',u'课程设计大纲'))
    homeShow = models.TextField(verbose_name='主页显示内容',default='未填写内容')
    nav = models.CharField(choices=nav_choice,max_length=2,unique=True,editable=True,verbose_name='对应页面模块')
    content = RichTextField(verbose_name='页面显示内容')
    class Meta:
        verbose_name = '介绍信息管理'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        dict_nav = dict(self.nav_choice)
        return  dict_nav.get(self.nav)



#内容发布
class PublishInformation(models.Model):
    nav_choice = ((u'13',u'课程实验'),(u'33',u'课外作业'),(u'41',u'案例库'),(u'42',u'专题讲座'),
                  (u'43',u'资源教材'),(u'62',u'教研教改'),(u'22',u'教学团队'))

    nav = models.CharField(choices=nav_choice,max_length=2,unique=True,editable=True,verbose_name='对应页面模块')
    class Meta:
        verbose_name = '更多内容发布'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        nav_dict = dict(self.nav_choice)
        return nav_dict.get(self.nav)


class PublishContent(models.Model):
    father = models.ForeignKey(PublishInformation)
    title  = models.CharField(max_length=20,unique=True,verbose_name='标题链接',default='没写标题')
    content = RichTextField(verbose_name='文本编辑')
    class Meta:
        verbose_name = '显示的内容'
        verbose_name_plural = verbose_name



#文件上传
class PublishFile(models.Model):
    nav_choice = ((u'31',u'教学录像'),(u'32',u'授课教案'))
    nav = models.CharField(choices=nav_choice,max_length=2,unique=True,editable=True,verbose_name='对应页面模块')

    class Meta:
        verbose_name = '录像和教案上传'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        dict_nav = dict(self.nav_choice)
        return dict_nav.get(self.nav)



class FileContent(models.Model):
    url = models.URLField(verbose_name='优酷链接',blank=True,null=True)
    father = models.ForeignKey(PublishFile)
    fileName = models.CharField(max_length=10,verbose_name='文件介绍')
    files = models.FileField(upload_to='file',blank=True,null=True)
    class Meta:
        verbose_name= '文件上传'
        verbose_name_plural = verbose_name


class CoursePublish(models.Model):
    nav_choice = ((u'51',u'课程公告'),(u'52',u'课外活动'),(u'61',u'教研成果'))
    nav = models.CharField(choices=nav_choice,max_length=2,unique=True,editable=True,verbose_name='对应页面模块')
    class Meta:
        verbose_name = '课程内容发布'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        dict_nav = dict(self.nav_choice)
        return dict_nav.get(self.nav)



class CourseMain(models.Model):
    father = models.ForeignKey(CoursePublish)
    publishDate = models.DateTimeField(verbose_name='发布时间',default=timezone.now)
    title = models.CharField(max_length=30,verbose_name='链接标题',default = '未填写标题')
    is_publish = models.BooleanField(default=False,verbose_name='是否主页显示')
    image = models.ImageField(upload_to='upload/news',verbose_name='主页显示的图片',blank=True,null=True)
    content = RichTextField(blank=True,null=True)
    class Meta:
        verbose_name = '内容发布'
        verbose_name_plural = verbose_name
        ordering = ["-publishDate"]

class ReFell(models.Model):
    content = models.TextField(verbose_name='反馈内容')
    connect = models.CharField(max_length=30,verbose_name='客户联系方式')
    class Meta:
        verbose_name = "内容反馈"
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.connect













