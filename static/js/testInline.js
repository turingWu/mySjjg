/**
 * Created by Administrator on 2016/1/14.
 */

//(function(){
//    var aUl=document.getElementsByClassName("testChoiceUl");
//    var ULen=aUl.length;
//    console.log(aUl);
//    for(var i=0;i<ULen;i++){
//        aUl[i].index=i;
//        var inputs=aUl[i].getElementsByTagName("input");
//        var inputsLen=inputs.length;
//        for(var i=0;i<inputsLen;i++){
//            console.log(inputs[i]);
//        }
//    }
//
//})();
var isChecked=function(cla){
    var checkedCount=[];
    var parent=document.getElementsByClassName(cla);
    //console.log(parent);
    //for(var i=0;i<parent.length;i++){
        var aInputs=document.getElementsByTagName("input");
        //console.log(aInputs.length);
        for(var i=0;i<aInputs.length;i++){
            if(aInputs[i].checked){
                checkedCount.push(aInputs[i]);
                console.log(aInputs[i].value);
            }
        }
    //}
    if(checkedCount.length!=parent.length){
        //console.log("ok!");
        alert('请答完题后再提交！');
        return false;
    }
};

//(function(){
//    var formBtn=document.getElementById("test-go");
//    formBtn.onclick=function(){
//        if(isChecked("testChoice")==true){
//            alert("111");
//        }else{
//            this.disable=true;
//        }
//    };
//})();
//$(function(){
//    $('.testForm').submit(function(){
//        for(var i=0;i<len;i++){
//            if(){
//                alert('qing');
//                return false
//            }
//        }
//    })
//});