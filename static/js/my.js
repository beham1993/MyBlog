$(document).ready(function()
	{
	var cururl = document.URL;
	switch(cururl){
		case "http://127.0.0.1:8000/about_me/": {
			$(".nav_up li.third").toggleClass("current");
			break;
		}
		case "http://127.0.0.1:8000/": {
			$(".nav_up li.first").toggleClass("current");
			break;
		}
		case "http://127.0.0.1:8000/archive/": {
			$(".nav_up li.second").toggleClass("current");
			break;
		}
	}	
	/*$(".nav_up li").(function () {
		$(".nav_up li").removeClass("current");
		$(this).addClass("current");
	});*/

	$(".text_article p").css({ display: "none" });
	$(".text_article p:first-child").css({ display: "block" });
	$(".text_article p:nth-child(2)").css({ display: "block" });
}); 