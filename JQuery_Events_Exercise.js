//which method
$('input').eq(0).keypress(function(){
  if(event.which === 13){
    $('h3').toggleClass('turnBlue')
  }
})


//on() method acts like addEventListener in vanilla JS.
$('h1').on('mouseenter',function(){
  $(this).toggleClass('turnBlue')
})


//Effets and Animations
$('input').eq(1).on('click',function(){
  $('.container').slideUp(3000)
})
