#-*- coding:utf-8 -*-
import os
from django.shortcuts import render_to_response,redirect,RequestContext,HttpResponseRedirect
from django.http import HttpResponse,Http404
from django.contrib.auth.hashers import make_password
from sjjgWeb.forms import *
from sjjgWeb.models import *
from django.contrib.auth import login,logout,authenticate
from django.views.decorators.csrf import csrf_protect
import json
from mySjjg.settings import STATICFILES_DIRS,BASE_DIR
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
# Create your views here.


def test(request):
    user = request.user.is_authenticated()
    return render_to_response('test.html',{'user':user})

def index(request):
    informationList = {}
    try:
        courseBoss = Information.objects.get(nav = '21')
        course = Information.objects.get(nav = '11')
        experiment = PublishInformation.objects.get(nav = '13')
        coursePPT = PublishFile.objects.get(nav ='32')
        coursePublish = CoursePublish.objects.get(nav = '51')
        coursePlay = CoursePublish.objects.get(nav = '52')
        publishList = CoursePublish.objects.all()

        informationList['enrollList'] = []
        for foo in publishList:
            objList = foo.coursemain_set.all()
            for indexs,messObj in enumerate(objList):
                if messObj.is_publish:
                    srcs = '/index/' +(foo.nav)[0]+'/'+(foo.nav)[1]+'/'+str(indexs+1)
                    obj = {'src':srcs,'obj':messObj}
                    informationList['enrollList'].append(obj)

        informationList['bossMess'] = courseBoss.homeShow
        informationList['courseMess'] = course.homeShow
        informationList['expList'] =experiment.publishcontent_set.all()
        informationList['PPT'] = coursePPT.filecontent_set.all()
        informationList['coursePublish'] = coursePublish.coursemain_set.all()
        informationList['coursePlay'] = coursePlay.coursemain_set.all()
        informationList['coursePublishTitle'] = []
        informationList['is_login'] = request.user.is_authenticated()

    except:
        return Http404()
    return render_to_response('index.html',informationList)


#试卷提交
def getTest(request):
    if request.method == 'GET':
        testId = request.GET['testId']
        try:
            myTest = Tests.objects.get(num = testId)
        except Exception as e:
            return HttpResponse('试卷不存在')

        choiceList = myTest.choice_question_set.all()
        boolList = myTest.bool_question_set.all()
        choiceGree = 0
        boolGree = 0
        choiceScore = myTest.choice_score
        boolScore = myTest.bool_score
        maxScore = len(choiceList)*choiceScore+len(boolList)*boolScore
        userChoiceList = []
        userBoolList = []
        userAnswerList = []
        for myIndex,foo in enumerate(choiceList):
            userAns = request.GET.get(str(myIndex+1)+'-choice','error')
            userChoiceList.append(userAns)
            if foo.correct == userAns:
                choiceGree += choiceScore
        for myIndex,foo in enumerate(boolList):
            userAns = request.GET.get((str(myIndex+1)+'-radio'),False)
            userBoolList.append(bool(userAns))
            if request.GET.get((str(myIndex+1)+'-radio'),False):
                if bool(int(userAns)) == foo.correct:
                    boolGree += boolScore
        for myIndex,foo in enumerate(myTest.answer_question_set.all()):
            userAnswerList.append(request.GET.get(str('answerArea-'+str(myIndex+1)),False))

        studentObj = Student.objects.get(username = request.user.username)
        if Score.objects.filter(testId = Tests.objects.get(num=testId),student=studentObj):
            Score.objects.update(score = choiceGree+boolGree)
        else:
            scoreObj = Score(testId=Tests.objects.get(num=testId),student=studentObj,score = choiceGree+boolGree)
            scoreObj.save()
        return information(request,'4','4',bottom=testId,endTest=True,
                           score=choiceGree+boolGree,maxScore=maxScore,
                           userChoiceList=userChoiceList,userBoolList = userBoolList,
                           userAnswerList=userAnswerList
                           )
    else:
        return HttpResponse('出错')

def information(request,root,node,bottom = 0,**kwargs):
    #通过root对应导航栏
    is_login = request.user.is_authenticated()
    if is_login:
        is_username = request.user.username
        if len(Student.objects.filter(username=is_username))==0:
            logout(request)
    courseKey = {'1':u'课程信息',
             '2':u'教学团队',
             '3':u'教学资源',
             '4':u'扩展资源',
             '5':u'资讯中心',
             '6':u'教研成果',}
    #获取导航栏结构的json文件,放在静态文件路径下的/json/nav.json文件中
    courseList = [
        ["课程介绍","课程大纲","课程实验","课程设计大纲"],
        ["课程负责人","教学团队"],
        ["教学录像","授课教案",u"课外作业"],
        ["案例库","专题讲座","资源教材","在线测试"],
        ["课程公告","课外活动"],
        ["科研成果","教研教改","课程评价"]]

    #页面的h4标题
    inforPage = ('11','12','21','14')
    publishPage = ('13','22','33','41','42','43','62')
    filePage = ('31','32')
    newPage = ('51','52','61')
    #判断是否超过总标题个数
    if int(root)<7:
        title = courseKey.get(root)
    #动态获得标题下的列表
        navList = courseList[int(root)-1]
        #如果输入域名不存在
        try:
            nodeText = navList[int(node)-1]   #子导航栏文本
            top = (int(node)-1)*50+20
        except IndexError:
            return HttpResponse('页面不存在')
    else:
        return HttpResponse('页面不存在')   #主导航栏不存在
    dicts = {'title':title,'navList':navList,'nodeText':nodeText,'top':top,'root':root,'node':node,'is_login':request.user.is_authenticated()}

    pageStr = root+node
    if pageStr in inforPage:
        try:
            introObj = Information.objects.get(nav = pageStr)
            dicts['contentObj'] = introObj
            if not introObj:
                dicts['noContent'] = '暂时没有内容'
        except Exception as e:
            dicts['contentObj'] = None
            dicts['errors'] = e
        return render_to_response('information.html',dicts)
    if pageStr in publishPage:
        try:
            introObj = PublishInformation.objects.get(nav = pageStr)
            dicts['publishList'] = introObj.publishcontent_set.all()
        except Exception as e:
            dicts['errors'] = e
            dicts['publishList'] = None
        if bottom == 0:
            if not dicts['publishList']:
                dicts['noContent'] = '暂时没有内容'
            return render_to_response('information.html',dicts)
        else:
            dicts['contentObj'] = dicts['publishList'][int(bottom)-1]
            dicts['publishList'] = None
            return render_to_response('information.html',dicts)
        #文件上传信息
    if pageStr in filePage:
        try:
            introObj = PublishFile.objects.get(nav = pageStr)
            dicts['publishList'] = introObj.filecontent_set.all()
        except Exception as e:
            dicts['errors'] = e
            dicts['publishList'] = None
        if bottom == 0:
            if not  dicts['publishList']:
                dicts['noContent'] = '暂时没有内容'
            paginator = Paginator(dicts['publishList'],5)
            try:
                page = int(request.GET.get('page',1))
                dicts['page'] = (page-1)*5
                dicts['publishList'] = paginator.page(page)
                dicts['pre'] = "上一页"
                dicts['next'] = "下一页"
            except (InvalidPage,EmptyPage,PageNotAnInteger):
                dicts['publishList'] = paginator.page(1)
            return render_to_response('information.html',dicts)
        else:
            pageNum = int(request.GET.get('page',0))
            dicts['fileYouUrl'] = dicts['publishList'][int(bottom)-1+pageNum].url
            dicts['fileName'] = dicts['publishList'][int(bottom)-1+pageNum].fileName
            dicts['fileUrl'] = dicts['publishList'][int(bottom)-1+pageNum].files
            dicts['publishList'] = None
            dicts['request'] = request
            if pageStr == '32':
                dicts['bottom'] = bottom
                return render_to_response('information.html',dicts)
            else:
                return render_to_response('coursePlayer.html',dicts)
    #发布信息
    if pageStr in newPage:
        try:
            introObj = CoursePublish.objects.get(nav = pageStr)
            dicts['newPublishList'] = introObj.coursemain_set.all()
            if len(dicts['newPublishList']) == 1:
                dicts['only'] = True
                news = dicts['newPublishList'][0]
                dicts['newTitle'] = news.title
                dicts['newDate'] = news.publishDate
                dicts['contents'] = news.content

        except Exception as e:
            dicts['errors'] = e
            dicts['newPublishList'] = None
        if bottom == 0:
            if not dicts['newPublishList']:
                dicts['noContent'] = '暂时没有内容'
            return render_to_response('information.html',dicts)
        else:
            news = dicts['newPublishList'][int(bottom)-1]
            dicts['newTitle'] = news.title
            dicts['newDate'] = news.publishDate
            dicts['contents'] = news.content
            return render_to_response('new.html',dicts)
    #试卷测试.
    if pageStr == '44':
        try:
            dicts['publishList'] = Tests.objects.all()
        except Exception as e:
            dicts['errors'] = 3
            dicts['publishList'] = None
        if request.user.is_authenticated():
            if bottom == 0:
                if not dicts['publishList']:
                    dicts['publishList'] = '暂时没有内容'
                return render_to_response('information.html',dicts)
            else:
                dicts['myTests'] = dicts['publishList'][int(bottom)-1]
                dicts['choiceList'] = dicts['myTests'].choice_question_set.all()
                dicts['boolList'] = dicts['myTests'].bool_question_set.all()
                dicts['answerList'] = dicts['myTests'].answer_question_set.all()
                dicts['stringList'] = {1:'一、选择题',2:'二、判断题',3:'三、问答题',4:'提交',5:'正确答案',6:'得分',7:'总分',
                                       8:'成绩计算的是判断和选择题，主观题自己对答案脑补',9:'你的答案'}
                if len(kwargs)>0:
                    dicts['endTest'] = kwargs['endTest']
                    dicts['score'] = kwargs['score']
                    dicts['maxScore'] = kwargs['maxScore']
                    dicts['choiceList2'] = zip(dicts['choiceList'],kwargs['userChoiceList'])
                    dicts['boolList2'] = zip(dicts['boolList'],kwargs['userBoolList'])
                    dicts['answerList2'] = zip(dicts['answerList'],kwargs['userAnswerList'])
                return render_to_response('testinline.html',dicts)
        else:
            return do_login(request,'/index/4/4/')
    if pageStr == '63':
        dicts['commentList']= comment.objects.all()
        dicts['stringList']={1:'老师回复'}
        dicts['is_admin'] = True if request.user.is_superuser else False
        paginator = Paginator(dicts['commentList'],5)
        try:
            page = int(request.GET.get('page',1))
            dicts['pre'] = "上一页"
            dicts['next'] = "下一页"
        except (InvalidPage,EmptyPage,PageNotAnInteger):
            dicts['commentList'] = paginator.page(1)
        return render_to_response('comment.html',dicts,context_instance=RequestContext(request))






@csrf_protect
def register(request):
    if request.method == 'POST':
        regF = RegisterForm(request.POST)
        if regF.is_valid():
            #注册
            user = Student(username =regF.cleaned_data['studentId'],
                                              first_name = regF.cleaned_data['first_name'],
                                              email = regF.cleaned_data["email"],
                                              password = make_password(regF.cleaned_data['password']),
                                              s_class = regF.cleaned_data["s_class"],
                                              )
            user.save()
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request,user)
            url = request.POST.get('myUrl')
            if url:
                return HttpResponse(url)
            else:
                return HttpResponse(request.get_host()+'/index')

        else:
            return HttpResponse(0)
    else:
        regF = RegisterForm()
    return render_to_response('register.html',locals(),context_instance=RequestContext(request))

#确认用户信息
#o r m模型
def matchId(request):
    if request.method == 'GET':
        username = request.GET['username']
        if username:
            try:
                obj = Student.objects.filter(username = username)
                if obj:
                    messages = 0
                else:
                    messages = 1
            except Exception as e:
                messages = e
                return Http404()
            return HttpResponse(messages)
        else :
            return index(request)

#登陆功能
@csrf_protect
def do_login(request,url=''):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            #登陆功能
            username = login_form.cleaned_data["studentId"]
            password = login_form.cleaned_data["password"]
            user = authenticate(username = username,password = password)
            if user is not None and len(Student.objects.filter(username=username))!=0:
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                login(request,user)
                if request.POST.get('source_url'):
                    url = request.POST.get('source_url')
                    return redirect(request.POST.get('source_url'))
                else:
                    if url:
                        return HttpResponseRedirect(url)
                    else:
                        return HttpResponseRedirect('/index')
            else:
                #改动

                url = request.POST.get('source_url','')
                return render_to_response('login.html',{'reason':'登陆验证失败','url':url},context_instance=RequestContext(request))

    else:
        login_form = LoginForm()
    return render_to_response('login.html',locals(),context_instance=RequestContext(request))

def do_logout(request):
    logout(request)
    return HttpResponseRedirect('/index')

import time
def upload_image(request):
    if request.method == 'POST':
        callback = request.GET.get('CKEditorFuncNum')
        # try:
        path = "upload/" + time.strftime("%Y%m%d%H%M%S",time.localtime())
        path2 = os.path.join(BASE_DIR,'upload')

        f = request.FILES["upload"]
        file_name2 = path2+"\\"+time.strftime("%Y%m%d%H%M%S",time.localtime())+"_" +f.name
        file_name = path + "_" + f.name
        des_origin_f = open(file_name2, "wb+")
        for chunk in f:
            des_origin_f.write(chunk)
        des_origin_f.close()
        # except Exception, e:
        #     print e
        res = r"<script>window.parent.CKEDITOR.tools.callFunction("+callback+",'/"+file_name+"', '');</script>"
        return HttpResponse(res)
    else:
        raise Http404()

#文件下载
from django.http import StreamingHttpResponse
from django.core.servers.basehttp import FileWrapper
def big_file_download(request):
    # do something...

    url = '/upload/' + request.GET['url']

    the_file_name = BASE_DIR+url

    wrapper = FileWrapper(file(the_file_name))
    response = StreamingHttpResponse(wrapper,content_type='application/octet-stream')
    response['Content-Length'] = os.path.getsize(the_file_name)
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(the_file_name)
    return response


@csrf_protect
def upHomework(request):
    is_login = request.user.is_authenticated()
    if is_login:
        is_username = request.user.username
        if len(Student.objects.filter(username=is_username))==0:
            logout(request)
    if is_login:
        if request.method == 'POST':
            upForm = HomeworkForm(request.POST,request.FILES)
            if upForm.is_valid():
                homeworkName = upForm.cleaned_data['homeworkName']
                content = upForm.cleaned_data['content']
                studentObj = Student.objects.get(username = request.user.username)
                upHomewordObj = uploadHomework(homeworkId = homeworkName,content = content,student = studentObj)
                upHomewordObj.save()
                return render_to_response('jump.html')
        else:

            upForm = HomeworkForm()
            return render_to_response('uploadHomework.html',locals(),context_instance=RequestContext(request))
    else:
        return do_login(request,url='/homework')

@csrf_protect
def connectUs(request):
    if request.method == 'POST':
        if request.POST.get('content',False):
            ok = ReFell(content = request.POST['content'],connect = request.POST.get('connect',''))
            ok.save()
        return HttpResponse('反馈成功')
    else:
        return render_to_response('connectUs.html',context_instance=RequestContext(request))

@csrf_protect
def do_comment(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            mycontent = request.POST.get('content','')
            commentObj = comment(content = mycontent,user = Student.objects.get(username = request.user.username))
            commentObj.save()
            return HttpResponseRedirect('/index/6/3/')
        return HttpResponseRedirect('/login')
    else:

        return do_login(request,url='/index/6/3/')


def not_allow(request):
    "用来定义重写admin的add函数关闭admin的add接口"
    return render_to_response('notAllow.html',locals())

