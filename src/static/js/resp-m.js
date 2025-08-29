$(document).ready(function(){
   	$('.responsive-menu-ic').click(function() {
   		$('.responsive-menu').fadeIn(800);
   	})
   	$('.resp-m a').click(function() {
   		$('.responsive-menu').fadeOut(800);
   	})
});