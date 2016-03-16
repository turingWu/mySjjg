#-*- coding:utf-8 -*-
from django.contrib import admin
from suit_ckeditor.widgets import CKEditorWidget
from models import *
from django.forms import ModelForm,Textarea

# Register your models here.

admin.site.register(ReFell)

class ScoreInline(admin.TabularInline):
    extra = 1
    model = Score
class HomeworkInline(admin.TabularInline):
    extra = 1
    model = uploadHomework

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    search_fields = ('username','s_class','email','first_name')
    list_display = ('username','first_name','s_class','email')
    list_filter = ('s_class',)
    date_hierarchy = 'date_joined'
    exclude = ('last_name',)
    inlines = (
        ScoreInline,
        HomeworkInline,
    )
    fieldsets = (
        ('基本信息',{'fields':('username','password','s_class','picture','email','date_joined','first_name'),
                 'description':'这是一个修改信息的栏目'}),
    )

class BoolInline(admin.TabularInline):
    extra = 1
    model = Bool_question

class AnswerForm(ModelForm):
    class Meta:
        widgets = {
            'question':Textarea(),
            'correct':Textarea(),
        }
class AnswerInline(admin.TabularInline):
    form = AnswerForm
    model = Answer_question
    extra = 1

class ChoiceInline(admin.StackedInline):
    model = Choice_question
    extra = 1


@admin.register(Tests)
class TestsAdmin(admin.ModelAdmin):
    inlines = [
        BoolInline,
        AnswerInline,
        ChoiceInline,
    ]

admin.site.register(User)


#fields
#fieldsets  （（name,{option的键值对}）(每一个这个代表一个set) 。。。（可变））
#option选项有field,descriptions,classes

#exclude——field的补集
#filter_horizontal 和 filter_vertical——分别对应多选框的添加方式.
#form:


##留言板
class ReCommentInline(admin.TabularInline):
    extra = 1
    model = ReComment
@admin.register(comment)
class CommentAdmin(admin.ModelAdmin):
    inlines = [
        ReCommentInline,
    ]

##留言板结束

#介绍信息
import views
@admin.register(Information)
class InformationAdmin(admin.ModelAdmin):
    actions = None
    readonly_fields = ('nav',)
    def add_view(self, request, form_url='', extra_context=None):
        return views.not_allow(request)



#内容发布
class PublishContentInline(admin.StackedInline):
    extra = 1
    model = PublishContent


@admin.register(PublishInformation)
class PublishInformationAdmin(admin.ModelAdmin):
    inlines = [
        PublishContentInline,
    ]
    def add_view(self, request, form_url='', extra_context=None):
        return views.not_allow(request)
    actions = None
    readonly_fields = ('nav',)

#文件上传
class FileContentInline(admin.StackedInline):
    extra = 1
    model = FileContent

@admin.register(PublishFile)
class PublishFileAdmin(admin.ModelAdmin):
    actions = None
    inlines = [
        FileContentInline,
    ]
    readonly_fields = ('nav',)
    def add_view(self, request, form_url='', extra_context=None):
        return views.not_allow(request)

#课程信息
class CourseMainInine(admin.StackedInline):
    extra = 1
    model = CourseMain

@admin.register(CoursePublish)
class CoursePublishAdmin(admin.ModelAdmin):

    readonly_fields = ('nav',)
    inlines = [
        CourseMainInine,
    ]
    def add_view(self, request, form_url='', extra_context=None):
        return views.not_allow(request)
    actions = None


