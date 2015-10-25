$(document).ready(function(){

    //history of gif table:
    new Vue({
      el: '#vueApp',
      data: {
        todos: [
          { text: 'GIF #1' },
          { text: 'GIF #2' },
          { text: 'GIF #3' }
        ]
      }
    })

    // var reader = new XMLHttpRequest() || new ActiveXObject('MSXML2.XMLHTTP');

    // function loadFile() {
    //     reader.open('get', 'test.rtf', true); 
    //     reader.onreadystatechange = displayContents;
    //     reader.send(null);
    // }

    // function displayContents() {
    //     if(reader.readyState==4) {
    //         var el = document.getElementById('main');
    //         el.innerHTML = reader.responseText;
    //     }
    // }

var gifHistory = []
var subredditScores = {
                      'gifs': 0, 'physicsgifs': 0, 'naturegifs': 0, 
                      'instant_regret': 0, 'rectiongifs': 0, 'aviationgifs': 0,
                      'dashcamgifs': 0, 'educationalgifs': 0, 'holdmybeer': 0,
                      'nevertellmetheodds': 0, 'nonononoaww': 0, 'oceangifs': 0,
                      'spacegifs': 0, 'startledcats': 0, 'wellthatsucks': 0, 'mechanical_gifs': 0
                      }

var jsonFile;

function getURL() {
    
    // $.getJSON("js/test.json", function(file) {
    //   // console.log(file);
    //   console.log("got here");
    //   returnFile = "hi";
    // });

    jsonFile = $.getJSON("js/gif_urls.json");
}

getURL();
jsonFile.done( function() {
  jsonFile = jsonFile.responseJSON;
  console.log(jsonFile);  
});

{debugger}
var index = 0;
var subredditCounter = 0;
var url = jsonFile['gifs'][index];
var subreddit = 'gifs';
var keys = Object.keys(jsonFile);
document.getElementById("next").src = url;

    //swiping functionality:
    $(".buddy").on("swiperight",function(){
      $(this).addClass('rotate-left').delay(700).fadeOut(1);
      $('.buddy').find('.status').remove();

      $(this).append('<div class="status like">Like!</div>');

      subredditScores[subreddit]+=1 
      if(index >= jsonFile[subreddit].length){
        index = 0;



        if(subreddit_counter < keys.length){
          subredditCounter+=1;
        }else{
          subredditCounter = 0;
        }

        subreddit = keys(jsonFile)[subreddit_counter];

        $('.buddy:nth-child(1)').removeClass ('rotate-left rotate-right').fadeIn(300);
       } else {
        subredditScores[subreddit] -= 1
        if(subredditScores[subreddit] <= -3){
          subredditCounter+=1
          index = 0
          subreddit = keys(jsonFile)[subredditCounter]
        }
        $(this).next().removeClass('rotate-left rotate-right').fadeIn(400);
       }
    });  

   $(".buddy").on("swipeleft",function(){
    $(this).addClass('rotate-right').delay(700).fadeOut(1);
    $('.buddy').find('.status').remove();
    $(this).append('<div class="status dislike">Dislike!</div>');

    if ( $(this).is(':last-child') ) {
     $('.buddy:nth-child(1)').removeClass ('rotate-left rotate-right').fadeIn(300);
     } else {
        $(this).next().removeClass('rotate-left rotate-right').fadeIn(400);
    } 
  });

});