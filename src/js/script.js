window.addEventListener('keydown',function(event){
   console.log(event.which);    
    
   if(event.which===65){
   clickA();
//    document.querySelector('.title').className = 'wow bounceIn';  
   } 
    
    if(event.which===83){
    clickS();
        
   } 
    
    if(event.which===68){
        clickD();
    }
    
    
    if(event.which===70){
        clickF();
    }
    
    if(event.which===71){
        clickG();
    }
    
    if(event.which===72){
        clickH();
    }
    
    
    if(event.which===74){
        clickJ();
    }
    
    if(event.which===75){
        clickK();
    }
    
    if(event.which===76){
        clickL();
    }
    
});


function clickA(){
    document.querySelector('#A').className = 'beat-box-keydown';
   var audioA = document.querySelector('audio[data-key="65"]');  
    audioA.currentTime=0;
    audioA.play();
}

function unclickA(){
    document.querySelector('#A').className = 'beat-box';
}


function clickS(){
    document.querySelector('#S').className = 'beat-box-keydown';
   var audioS = document.querySelector('audio[data-key="83"]');  
    audioS.currentTime=0;
    audioS.play();
}

function unclickS(){
    document.querySelector('#S').className = 'beat-box';
}

function clickD(){
    document.querySelector('#D').className='beat-box-keydown';
        var audioD=document.querySelector('audio[data-key="68"]');
        audioD.currentTime=0;
        audioD.play();
}

function unclickD(){
    document.querySelector('#D').className = 'beat-box';
}


function clickF(){
    document.querySelector('#F').className='beat-box-keydown';
        var audioF=document.querySelector('audio[data-key="70"]');
        audioF.currentTime=0;
        audioF.play();
}

function unclickF(){
    document.querySelector('#F').className = 'beat-box';
}


function clickG(){
    document.querySelector('#G').className='beat-box-keydown';
        var audioG=document.querySelector('audio[data-key="71"]');
        audioG.currentTime=0;
        audioG.play();
}
    

function unclickG(){
    document.querySelector('#G').className = 'beat-box';
}


function clickH(){
    document.querySelector('#H').className='beat-box-keydown';
        var audioH=document.querySelector('audio[data-key="72"]');
        audioH.currentTime=0;
        audioH.play();
}

function unclickH(){
    document.querySelector('#H').className = 'beat-box';
}


function clickJ(){
    document.querySelector('#J').className='beat-box-keydown';
        var audioJ=document.querySelector('audio[data-key="74"]');
        audioJ.currentTime=0;
        audioJ.play();
}

function unclickJ(){
    document.querySelector('#J').className = 'beat-box'; 
}


function clickK(){
    document.querySelector('#K').className='beat-box-keydown';
        var audioK=document.querySelector('audio[data-key="75"]');
        audioK.currentTime=0;
        audioK.play();
}


function unclickK(){
    document.querySelector('#K').className = 'beat-box';
}


function clickL(){
    document.querySelector('#L').className='beat-box-keydown';
        var audioL=document.querySelector('audio[data-key="76"]');
        audioL.currentTime=0;
        audioL.play();
}

function unclickL(){
    document.querySelector('#L').className = 'beat-box';  
}



window.addEventListener('keyup',function(e){
unclickA();
unclickS();
unclickD();
unclickF();
unclickG();
unclickH();
unclickJ();   
unclickK();
unclickL();  
});