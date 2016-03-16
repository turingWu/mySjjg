/**
 * Created by 林泽鹏 on 2015/11/16.
 */
function Validate(inputObj)
{

    //对象属性
    this.username = document.getElementById(inputObj.usernameId);
    this.password = document.getElementById(inputObj.passwordId);
    if (inputObj.surePasswordId!=undefined)
    {

        this.surePassword = document.getElementById(inputObj.surePasswordId);
    }else{
        this.surePassword = false
    }
    if (inputObj.emailId != undefined){
        this.email = document.getElementById(inputObj.emailId)
    }else{
        this.email = false
    }
    this.email = document.getElementById(inputObj.emailId);
    this.usernamePattern = /^[A-Za-z0-9]*$/;
    this.maxUsername = 12;
    this.minUsername = 6;
    this.maxPassword = 16;
    this.minPassword = 6;
    this.emailPattern = /^([a-zA-Z0-9]+[_|\|\.]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[_|\|\.]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$/;

    //对象方法
    if(typeof this.matchUsername != 'function')
    {
        Validate.prototype.matchUsername = function()
        {
            var  values = this.username.value;
            if (values.length<this.minUsername)
            {
                return {error:true,message:'用户名字数不足'}
            }else if (values.length>this.maxUsername)
            {
                return {error:true,message:'用户名字数太多'}
            }else if(!this.usernamePattern.test(values))
            {
                return {error:true,message:'用户名格式不对'}
            }else
            {
                return {error:false}
            }
        }
    }
    if(typeof this.matchPassword != 'function')
    {
        Validate.prototype.matchPassword = function()
        {
            var value = this.password.value;
            if(value.length<this.minPassword)
            {
                return {error:true,message:'密码长度不够'}
            }else if(value.length>this.maxPassword)
            {
                return {error:true,message:'密码太长'}
            }else{
                return {error:false}
            }
        }
    }
    if(typeof this.matchSurePassword != 'function')
    {
        Validate.prototype.matchSurePassword = function()
        {
            var value = this.surePassword.value;
            var passwordValue = this.password.value;
            if (value.length==0)
            {
                return {error:true,message:'此项不能为空'}

            }else if (value != passwordValue)
            {
                return {error:true,message:'两次输入密码不一致'}
            }
            else
            {
                return {error:false}
            }
        }
    }
    if (typeof this.matchEmail != 'function')
    {
        Validate.prototype.matchEmail = function()
        {
            var value = this.email.value;
            if(!this.emailPattern.test(value))
            {
                return {error:true,message:'请输入正确的邮箱'}
            }else
            {
                return {error:false}
            }
        }
    }

    if (typeof this.inputBlur != 'function')
    {
        Validate.prototype.inputBlur = function(fun)
        {

            this.username.onblur = fun;
            this.password.onblur = fun;
            if (this.email){
                this.email.onblur = fun;
                this.surePassword.onblur = fun;
            }
        }
    }
    if (typeof this.inputFocus != 'function')
    {
        Validate.prototype.inputFocus = function(fun)
        {

            this.username.onfocus = fun;
            this.password.onfocus = fun;
            if (!this.email){
                this.email.onfocus = fun;
                this.surePassword.onfocus = fun;
            }

        }
    }
    if (typeof this.matchThis != 'function')
    {
        Validate.prototype.matchThis = function(obj)
        {
            if(obj == this.username)
            {
                return this.matchUsername()
            }else if(obj == this.password){
                return this.matchPassword()
            }else if (obj == this.email){
                return this.matchEmail()
            }else if(obj == this.surePassword){
                return this.matchSurePassword()
            }else {
                return false
            }
        }
    }
    if (typeof this.matchAll != 'function')
    {
        Validate.prototype.matchAll = function()
        {
            if(this.matchUsername().error){
                this.username.focus();
                return false
            }else if(this.matchPassword().error){
                this.password.focus();
                return false
            }else if(this.email){
                if(this.matchSurePassword().error)
                {
                    this.surePassword.focus();
                    return false
                }else if(this.matchEmail().error)
                {
                    this.email.focus();
                    return false
                }
            }
            return 1

        }
    }
}
function removeElement(_element){

         if(_element){
             var _parentElement = _element.parentNode;
             if(_parentElement){
                 _parentElement.removeChild(_element);
             }

         }
}
function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie != '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) == (name + '=')) {
                       cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                       break;
                   }
               }
           }
           return cookieValue;
       }

$(function()
{
    //var pattern=/^\D{2,20}$/;
    //var pattern=/^([a-zA-Z0-9]+[_|\|\.]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[_|\|\.]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$/;
    //var pattern=/^\d{12}$/;
    obj = {
        usernameId:'id_studentId',
        passwordId:'id_password',
        surePasswordId:'id_surePassword',
        emailId:'id_email'
    };

    var matchObj = new  Validate(obj);

    matchObj.inputBlur(function (){
        var errors = matchObj.matchThis(this);
        if(!this.nextSibling){
            var span = document.createElement('span');
            this.parentNode.appendChild(span);
        }
        if (errors.error==true)
        {
            this.nextSibling.innerHTML = errors.message;
        }else
        {
            if(this == matchObj.username)
            {
                var data = {};
                data.username = this.value;
                var objThis = this;
                $.ajax(
                {
                    type: "get",
                    url: "/matchId/",
                    data: data,
                    cache: false,
                    success: function(data)
                    {
                        if(data==0)
                        {
                            objThis.nextSibling.innerHTML = '用户名已经存在';
                        }else
                        {
                            objThis.nextSibling.innerHTML = '';
                        }
                    }
                });
            }else{
                this.nextSibling.innerHTML = '';
            }

        }
    });
    $('#myform').submit(function()
    {
        //alert(1);
        var sdata = {};
        sdata.username = matchObj.username.value;
        var objThis = matchObj.username;
        $.ajax(
            {
                type: "get",
                url: "/matchId/",
                data: sdata,
                cache: false,
                success: function (data) {
                    if(!this.nextSibling){
                        var span = document.createElement('span');
                        matchObj.username.parentNode.appendChild(span);
                    }
                    if (data == 0) {
                        objThis.nextSibling.innerHTML = '用户名已经存在';
                        objThis.focus();
                    } else {
                        //alert(2);
                        objThis.nextSibling.innerHTML = '';
                        if (matchObj.matchAll() == 1) {
                            var mydata = {};
                            mydata.studentId = matchObj.username.value;
                            mydata.first_name = document.getElementById('id_first_name').value;
                            mydata.password = matchObj.password.value;
                            mydata.surePassword = matchObj.surePassword.value;
                            mydata.email = matchObj.email.value;
                            mydata.s_class = document.getElementById('id_s_class').value;
                            $.ajax
                            (
                                {
                                    type: "post",
                                    url: "/reg/",
                                    data: mydata,
                                    cache: false,
                                    beforeSend: function (xhr, settings) {
                                        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                                            // Only send the token to relative URLs i.e. locally.
                                            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
                                        }
                                    },
                                    success: function (data) {
                                        window.location.href="http://"+data;
                                    },
                                    errors: function () {
                                        alert('error');
                                    }
                                }
                            );
                        }
                    }
                }
            });
        return false;
    });
});
    //matchObj.username.onblur = function()
    //{
    //    var errors = matchObj.matchUsername();
    //    var span = document.createElement('span');
    //    if (errors.error==true)
    //    {
    //        this.parentNode.appendChild(span);
    //        this.nextSibling.innerHTML = errors.message;
    //    }else{
    //        removeElement(this.nextSibling);
    //    }
    //};
    //matchObj.password.onblur = function()
    //{
    //    var errors = matchObj.matchPassword();
    //    var span = document.createElement('span');
    //    if (errors.error==true)
    //    {
    //        this.parentNode.appendChild(span);
    //        this.nextSibling.innerHTML = errors.message;
    //    }else{
    //        removeElement(this.nextSibling);
    //    }
    //}

/*
* inputObj格式
* {
*   usernameId:
*   passwordId:
*   matchPasswordId:
*   emailId:
* }
* matchUsername
* matchPassword
*
* matchALL
*
* */



//function Validate()
//    {
//        this.myform=document.getElementById("myform");
//        this.inputs=document.getElementsByTagName("input");
//        this.spans=[];
//        this.allP=document.getElementsByTagName("p");
//        //this.studentId=document.getElementById("id_studentId");
//        //this.first_name=document.getElementById("id_first_name");
//        //this.password=document.getElementById("id_password");
//        //this.surePassword=document.getElementById("id_surePassword");
//        this.submit=document.getElementById("submit");
//        var _this=this;
//
//        for(var i=0;i<this.inputs.length-1;i++)
//        {
//            var span=document.createElement("span");
//            this.allP[i].appendChild(span);
//            this.spans.push(span);
//
//            this.inputs[i].index=i;
//            this.inputs[i].onblur=function()
//            {
//                switch (this.index)
//                {
//                    case 0:
//                        _this.valiID();
//                        break;
//                    case 1:
//                        _this.valiName();
//                        break;
//                    case 2:
//                        _this.valiPassw();
//                        break;
//                    case 3:
//                        _this.valiEPassw();
//                        break;
//                    case 4:
//                        _this.valiEmail();
//                        break;
//                    default :
//                        break;
//
//                }
//            };
//        }
//
//        this.submit.onclick=function()
//        {
//            return _this.Submit();
//        };
//        //this.studentId.onblur=function(){};
//        //this.first_name.onblur=function(){};
//        //this.password.onblur=function(){};
//        //this.surePassword.onblur=function(){};
//        //this.submit.onclick=function(){};
//
//    }
//
//    Validate.prototype.Submit=function()
//    {
//        for(var i=0;i<this.inputs.length;i++)
//        {
//            if(this.inputs[i].value=="")
//            {
//                this.spans[i].innerHTML="不能为空！";
//                return false;
//            }
//        }
//        var formParam= $(this.myform).serialize();
//        $.ajax({
//            type: "post",
//            url: "url",
//            data: formParam,
//            cache: false,
//            dataType: "json",
//            success: function(data)
//            {
//                alert(data);
//            }
//        });
//        alert("已经提交！");
//    };
//    /*学号验证：12位数字*/
//    Validate.prototype.valiID=function()
//    {
//        console.log("学号验证");
//        var _this=this;
//        var value=this.inputs[0].value;
//        var pattern=/^\d{12}$/;
//        if(!pattern.test(value))
//        {
//            this.spans[0].innerHTML="输入有误！";
//            return false;
//        }else
//        {
//            $.ajax({
//                type: "get",
//                url: "url",
//                data: "id_studentId=" + value ,
//                cache: false,
//                success: function(data)
//                {
//                    _this.spans[0].innerHTML=data;
//                }
//            });
//            //spans[0].innerHTML="输入正确！";
//        }
//    };
//
//    /*姓名验证：二到四个汉字*/
//    Validate.prototype.valiName=function()
//    {
//        console.log("姓名验证");
//        var value=this.inputs[1].value;
//        var pattern=/^[\u4e00-\u9fa5]{2,4}$/;
//        if(!pattern.test(value))
//        {
//            this.spans[1].innerHTML="输入有误！";
//            return false;
//        }else
//        {
//            this.spans[1].innerHTML="输入正确！";
//        }
//    };
//
//    /*密码验证：不少于6个字符*/
//    Validate.prototype.valiPassw=function()
//    {
//        console.log("密码验证");
//        var value=this.inputs[2].value;
//        if(value=="")
//        {
//            this.spans[2].innerHTML="输入有误！";
//            return false;
//        }
//        else
//        {
//            this.spans[2].innerHTML="输入正确！";
//        }
//    };
//
//    /*确认密码验证：与所设置密码相同？*/
//    Validate.prototype.valiEPassw=function()
//    {
//        console.log("确认密码验证");
//        var value=this.inputs[3].value;
//        if(value!=this.inputs[2].value)
//        {
//            this.spans[3].innerHTML="输入有误！";
//            return false;
//        }
//        else
//        {
//            this.spans[3].innerHTML="输入正确！";
//        }
//    };
//
//    /*邮箱验证：邮箱地址填写正确了吗？*/
//    Validate.prototype.valiEmail=function()
//    {
//        console.log("邮箱验证");
//        var value=this.inputs[4].value;
//        var pattern=/^([a-zA-Z0-9]+[_|\|\.]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[_|\|\.]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$/;
//        if(!pattern.test(value))
//        {
//            this.spans[4].innerHTML="输入有误！";
//            return false;
//        }
//        else
//        {
//            this.spans[4].innerHTML="输入正确！";
//        }
//    };

