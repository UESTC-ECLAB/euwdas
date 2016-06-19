$(function()
{
	UESTC.initMenu();
	UESTC.initBlockImage();
	$('.slideshow').each(UESTC.initSlideshow);

});



UESTC = {};
UESTC.isTouchDevice = ("createTouch" in document);
UESTC.isIE = !!navigator.userAgent.match(/Trident/i);

UESTC.initMenu = function()
{
	$('#navi ul.navigations > li').mouseenter(function()
	{
		$(this).find('ul').stop().slideDown(200);
	}).mouseleave(function()
	{
		$(this).find('ul').stop().slideUp(200);
	});
};
UESTC.initBlockImage = function(){
	var length = $(".block-image-item").length;
	var current = 0;
	var play = function(num){
		$(".block-image-item").hide();
		$($(".block-image").find(".block-image-item")[num]).show();
	};
	play(0);
	var next = function(){
		if(current == length-1){
			current = 0;
		}else{
			current = current+1;
		}
		play(current);
	};

	var  prev = function(){
		if(current == 0){
			current = length-1;
		}else{
			current = current -1;
		}
		play(current);
	};

	setInterval(function(){
		next();
	},7000);

}

UESTC.initSlideshow = function()
{
	var $slides = $(this);
	var animationType = $slides.attr('data-type');
	var interval = $slides.attr('data-interval');
	var animationTime = $slides.attr('data-animation-time') || 300;

	var timer;
	var animating = false;

	var length = $(".slide").length;

	function slide(isNext)
	{
		if (animating) return;
		animating = true;
		var $current = $slides.find('.slide.active');
		var $next = isNext ? $current.next('.slide') : $current.prev('.slide');
		if ($next.length == 0) $next = isNext ? $slides.find('.slide').first() : $slides.find('.slide').last();
		$next.addClass(isNext?'next':'prev');
		animate($current,$next,isNext ? 1 : -1,function()
		{
			$current.removeClass('active');
			$next.addClass('active').removeClass(isNext?'next':'prev');
			animating = false;
		});
	}

	function slideTo(index)
	{
		if (animating) return;
		index = parseInt(index,10);
		if (index < 1) index = 1;
		var $current = $slides.find('.slide.active');
		var $next = $slides.find('.slide').eq(index -1 );
		if ($next.is($current)) return;
		$next.addClass('next');
		animating = true;
		animate($current,$next,1,function()
		{
			$current.removeClass('active');
			$next.addClass('active').removeClass('next');
			animating = false;
		});
	}



	function animate($dom,$next,direction,cb)
	{
		try{ clearTimeout(timer);}catch(e){}
		if (animationType == 'fade')
		{
			$dom.fadeOut(animationTime,cb);
			$next.show();//.fadeIn(animationTime);
		}
		else if (animationType == 'horizontal')
		{
			var w = $dom.parent().width();
			$dom.animate({left: -1*w*direction },animationTime,cb);
			$next.css({left:w*direction}).animate({left:0});
		}
		else if (animationType == 'vertical')
		{
			var h = $dom.parent().height();
			$dom.animate({'top': -1*h*direction },animationTime,cb);
			$next.css({'top':h*direction}).animate({'top':0});
		}
		else
		{
			cb();
		}
		if ($slides.find('.indicators').length > 0)
		{
			var slides = $slides.find('.slide');
			for(var i=0;i<slides.length;i++)
			{
				if (slides.eq(i).is($next))
				{
					$slides.find('.indicator.active').removeClass('active');
					$slides.find('.indicator[data-slide='+(i+1)+']').addClass('active');
					break;
				}
			}
		}
	}

	function initTimer()
	{
		try{
			clearTimeout(timer);
		}catch(e){}

		timer = setTimeout(function()
		{
			slide(1);
			initTimer();
		},interval);
	}

	if (interval && interval > 0)
	{


		if(length <=1){
			return;
		}
		interval = parseInt(interval,10);

		$slides.mouseenter(function()
		{
			try{ clearTimeout(timer);}catch(e){}
		}).mouseleave(function()
		{
			initTimer();
		});

		initTimer();
	}

	$slides.find('.arrows > a').click(function(evt)
	{
		evt.preventDefault();
		var isNext = $(this).is('.next');
		slide(isNext);
	});

	$slides.find('.indicators > a').click(function(evt)
	{
		evt.preventDefault();
		var index = $(this).attr('data-slide') || '1';
		slideTo(index);
	});

	if ($slides.find('.slide.active').length == 0) $slides.find('.slide').eq(0).addClass('active');

};


$(function(){
	//tab
	$(".tab").find(".item-title").on("mouseover",function(){
		$(".tab").find(".item-title").removeClass("active");
		$(this).addClass("active");
		$(".tab").find(".content-list").hide();


		var target = $(this).attr("data-basic-key");
		$("."+target+"").stop().fadeIn();
	})
})