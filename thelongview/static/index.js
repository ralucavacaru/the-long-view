$(document).ready(function () {	
	$('.target-div').hide();

	$('.show').click(function () {
	    if (! ($(this).hasClass('active'))) {
	    	$('.target-div').hide();
	    	$('#div' + $(this).attr('target')).slideDown();
	    	$('.show').removeClass("active");
	    	$(this).addClass("active");
	    }
	});

	$('.hide').click(function () {
	    $('.target-div').slideUp();
	    $('.show').removeClass("active");
	});
});