
$("#register").on("click", function () {
	$(".register").siblings().hide();
	$(".register").slideToggle();
});
$("#login").on("click", function () {
	$(".login").siblings().hide();
	$(".login").slideToggle();
});
$("#reset").on("click", function () {
	$(".reset").siblings().hide();
	$(".reset").slideToggle();
});

$("#myBtn").click(function(){
	$(".form").hide();
    });