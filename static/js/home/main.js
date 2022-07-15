function randint(min, max){
	return Math.floor(Math.random() * (max - min + 1)) + min;
};

function singleSplash(splash){
	$()
};

$(function(){
	$.getJSON('static/js/home/splashes.json', function(splashes){
		var splash = splashes[randint(0, (Object.keys(splashes).length - 1))];
		if(splash[0] == "single"){
			$("#splash").html("<a class=\"splashText\" href=\"" + splash[2] + "\">" + splash[1] + "</a>");
		} else if (splash[0] == "sequence") {
			num = 1
			$("#splash").html("<a class=\"splashText\">" + splash[num] + "</a>");
			$("#splash").click(function(){
				num++;
				if(num < (splash.length - 2)){
					$("#splash").html("<a class=\"splashText\">" + splash[num] + "</a>");
				} else {
					$("#splash").html("<a class=\"splashText\" href=\"" + splash[(splash.length - 1)] + "\">" + splash[num] + "</a>");
					num--;
				};
			});
		} else {
			$("#splash").html("<a class=\"splashText\" href=\"" + splash[(splash.length - 1)] + "\">" + splash[randint(1,(splash.length - 2))] + "</a>");
			console.log("It's random");
		};
	});
});
