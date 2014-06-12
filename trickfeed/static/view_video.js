var TheatreApp = function(player) {
	var video = player;
    $(document).ready(function() {
        // Event handlers
        var tButton = $('.theatre-mode');
        var vOver = $('.video-overlay');
        tButton.click(function() {
            vOver.show();
	        video.playVideo();
        $(document).keydown(function(event){
        	if(event.keyCode == 27){
        		vOver.hide();
        		video.pauseVideo();
        	}
        });
            
        });
    }); 
};