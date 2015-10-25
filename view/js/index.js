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

    jQuery.getJSON("js/test.json", function(file) {
      console.log(file);
    });
    
    document.getElementById("next").src = "http://thefw.com/files/2013/05/0hgyoKm.gif";

    //swiping functionality:
    $(".buddy").on("swiperight",function(){
      $(this).addClass('rotate-left').delay(700).fadeOut(1);
      $('.buddy').find('.status').remove();

      $(this).append('<div class="status like">Like!</div>');      
      if ( $(this).is(':last-child') ) {
        $('.buddy:nth-child(1)').removeClass ('rotate-left rotate-right').fadeIn(300);
       } else {
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