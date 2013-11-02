var audio = new Audio();

$(document).on('ready', function(){
	$('.btn-play').on('click', function(e){
		var data = $(this).attr('data-audio');
		if( $(this).html()=='<i class="icon-stop"></i> Detener' ){
			audio.pause();
			$(this).html('<i class="icon-play"></i> Reproducir');
		} else {
			$('.btn-play').html('<i class="icon-play"></i> Reproducir');
			audio.src = data;
			audio.load();
			audio.play();
			$(this).html('<i class="icon-stop"></i> Detener');
		}
		e.preventDefault();
	});
});