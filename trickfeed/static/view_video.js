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
var FavoriteApp = function(user, video, v_array) {
	var user_uri = user;
	var video_uri = video;
	var v_array = v_array;
	v_array.push(video_uri);

	var addButton = $('.button-add-to-favs');
	var removeButton = $('.button-remove-from-favs');
	var flagButton = $('.button-not-tricking');

	//Events
	addButton.click(function() {
		$.ajax({
			url: user_uri,
			data: {"favorites": v_array},
			dataType: "json",
			contentType: "application/json",
			type: "PUT",
			success: function(){
				alert("Biscuits and gravy!");
			},
			error: function(response) {
				console.log(response.responseText);
			}
		});
	});
};