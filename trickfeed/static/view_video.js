//Theatre application controls
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

//User favorites controls
//Avoid hardcoding any attributes
var FavoriteApp = function(user, video) {
	var addButton = $('.button-add-to-favs');
	var removeButton = $('.button-remove-from-favs');
	var flagButton = $('.button-not-tricking');
};