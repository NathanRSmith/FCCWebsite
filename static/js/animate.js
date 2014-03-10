jQuery(document).ready(function($) {

	 /* some animate effect on hovers from animate.css  you can add more!!! more info http://daneden.me/animate/ */
   
	$(".a-flash").hover(
		function () {
		$(this).addClass("animated flash");
		},
		function () {
		$(this).removeClass("animated flash");
		}
	);
	$(".a-bounce").hover(
		function () {
		$(this).addClass("animated bounce");
		},
		function () {
		$(this).removeClass("animated bounce");
		}
	);
	
	$(".a-shake").hover(
		function () {
		$(this).addClass("animated shake");
		},
		function () {
		$(this).removeClass("animated shake");
		}
	);
	$(".a-tada").hover(
		function () {
		$(this).addClass("animated tada");
		},
		function () {
		$(this).removeClass("animated tada");
		}
	);
	$(".a-swing").hover(
		function () {
		$(this).addClass("animated swing");
		},
		function () {
		$(this).removeClass("animated swing");
		}
	);
	$(".a-wobble").hover(
		function () {
		$(this).addClass("animated wobble");
		},
		function () {
		$(this).removeClass("animated wobble");
		}
	);
	$(".a-wiggle").hover(
		function () {
		$(this).addClass("animated wiggle");
		},
		function () {
		$(this).removeClass("animated wiggle");
		}
	);
	$(".a-pulse").hover(
		function () {
		$(this).addClass("animated pulse");
		},
		function () {
		$(this).removeClass("animated pulse");
		}
	);
  
  	$(".a-flip").hover(
		function () {
		$(this).addClass("animated flip");
		},
		function () {
		$(this).removeClass("animated flip");
		}
	);
  
	
});