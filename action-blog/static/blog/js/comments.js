$(document).ready(function(){
	$(".comments").hide();
	$(".hide-comments").hide();
	$(".show-comments").click(function(){
		$(".comments").show("slow");
		$(".show-comments").hide("slow")
		$(".hide-comments").show("slow");
	});
	$(".hide-comments").click(function(){
		$(".comments").hide("slow");
		$(".show-comments").show("slow")
		$(".hide-comments").hide("slow");
	});
})