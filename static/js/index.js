<!-- JQUERY -->
		<script src="https://code.jquery.com/jquery-3.1.0.min.js"></script>
		

		<!-- JAVASCRIPT -->
		<script>
			jQuery("document").ready(function($){
		    var menu = $('.cabecalho');
		    $(window).scroll(function () {
		        if ($(this).scrollTop() > 136) {
		            menu.addClass("f-menu");
		        } else {
		            menu.removeClass("f-menu");
		        }
		    });
});