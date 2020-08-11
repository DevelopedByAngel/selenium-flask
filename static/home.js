
$(document).ready(function()
	{
		// var s=$('.thumb').attr("src");
		// if(!((s.includes("hqdefault")) || (s.includes("insta"))))
		// 	$('.thumb').attr('src','https://yt3.ggpht.com/a/AATXAJweyNKsPqMHyv5Tc_QLibwTDVpkA7RF63nbQw=s900-c-k-c0xffffffff-no-rj-mo');
		var h=$(window).height();
		var del=$('.nav-link').height();
		$('#frame').css("height",h-del+'px');
	
	});