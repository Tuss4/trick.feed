var TheatreApp = function(vid_id) {
    $(document).ready(function() {

        // Event handlers
        var tButton = $('.theatre-mode');
        var vOver = $('.video-overlay');
        tButton.click(function() {
            vOver.show();
	        console.log(player);
            function onPlayerReady(event) {
            	event.target.playVideo();
            };
        $(document).keydown(function(event){
        	if(event.keyCode == 27){
        		vOver.hide();
        	}
        });
            
        });
    }); 
}; 