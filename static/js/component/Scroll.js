/**
 * Created by 林泽鹏 on 2015/10/27.
 */
function Scroll(parent,child)/*走马灯的容器，走马灯的列表集合*/
{
    this.oScroll=document.getElementById(parent);
    this.oList=document.getElementById(child);
    this.oList.innerHTML+=this.oList.innerHTML;
    this.Li=this.oList.getElementsByTagName("li")[0];
    this.timer=null;

    this.Height=this.Li.offsetHeight*(this.oList.getElementsByTagName("li").length/2);
    this.oScroll.style.height=this.Height+"px";
    if(this.oScroll.offsetHeight>=290)
    {
        this.oScroll.style.height=290+"px";
    }else{
        this.oScroll.style.height=this.Height+"px";
    }
}

Scroll.prototype.toScroll=function()
{
    var _this=this;
    this.move();
    this.loop();
    this.oScroll.onmousemove=function(){
        _this.stopMove();
    };
    this.oScroll.onmouseout=function(){
        _this.move();
    };
}

Scroll.prototype.move=function()
{
    var _this=this;
    this.timer=setInterval( function(){ _this.loop(); },60)/*通过闭包获得当前作用域*/
}

Scroll.prototype.stopMove=function()
{
    var _this=this;
    clearInterval(_this.timer);
}

Scroll.prototype.loop=function()
{
    this.oList.style.top=this.oList.offsetTop-1+"px";
    if(this.oList.offsetTop<=-(this.Height))
    {
        this.oList.style.top=0;
    }
}
