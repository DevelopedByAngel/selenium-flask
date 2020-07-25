// $('input').on("input",function()
// 	{
// 		var val=$('input').val();
// 		$('div').css('border-radius',val+'px');
// 		$('div').css('transform','rotateZ('+val+'deg)');
// 		$('div').css('background-image','linear-gradient(-'+val+'deg,blue,#78cff5)')
// 	});
// $('div').draggable();
$(document).ready(function()
	{
		// var s=$('.thumb').attr("src");
		// if(!((s.includes("hqdefault")) || (s.includes("insta"))))
		// 	$('.thumb').attr('src','https://yt3.ggpht.com/a/AATXAJweyNKsPqMHyv5Tc_QLibwTDVpkA7RF63nbQw=s900-c-k-c0xffffffff-no-rj-mo');
		var h=$(window).height();
		$('#frame').css("height",h+'px');
	
	});
$('#menu').on("click",function()
	{
		// below gives css given
		if($('table').css('display')=='none'){
		        $('table').slideDown("normal",function(){});
		       	$('td').css("box-shadow","");
		    	$('#td1').css("box-shadow","inset 2px 2px 5px black,inset -2px -2px 5px black");
		    	$('.full').css("box-shadow","")
				$('.full').css("border","10px double rgba(255,255,255,0.4)")
				$('.full').css("background-color","")
}
		else{

		    	$('table').slideUp("fast",function(){});
		    }
	});
$('td').on("mouseover",function()
	{
		$("td").css("box-shadow","");
		$(this).css("box-shadow","inset 2px 2px 5px black,inset -2px -2px 5px black");
	});
$('td').click(function()
	{
				    	$('table').slideUp("fast",function(){});

	});
$('.full').on("mouseover",function()
	{
		$('.full').css("box-shadow","")
		$('.full').css("border","10px double rgba(255,255,255,0.4)")
		$('.full').css("background-color","")
		$(this).css("border","5px solid #ffeb6b")
		$(this).css("box-shadow","inset 0 0 7px #fff196,inset 0 0 8px #fff196,inset 0 0 9px #fff196,inset 0 0 10px #fff196,inset 0 0 11px #fff196,inset 0 0 12px #fff196,inset 0 0 13px #fff196")
		$(this).css("background-color","rgba(250, 244, 207,0.3)")
	});
function c()
	{
		var height=$(document).height();
		var header=$('#header').height();
		var menu=$('#menu > img').height();
		var minus=height-(header+(menu/6));
		$('iframe').css("height",minus+"px");
	};
	function clicked(e){
			$('title').text($(e).text());
			$('.embed-responsive').css("filter","brightness(50%)")
		};
