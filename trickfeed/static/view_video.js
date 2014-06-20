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
var FavoriteApp = function(user, video, v_array, vid_uri) {
	var user_uri = user;
	var video_uri = video;
	var v_array = v_array;
	var v_uri = vid_uri;
	v_array.push(v_uri);

	var addButton = $('.button-add-to-favs');
	var removeButton = $('.button-remove-from-favs');
	var flagButton = $('.button-not-tricking');

	//Events
	addButton.click(function() {
		var d = {"favorites": v_array}
		$.ajax({
			url: user_uri,
			dataType: "json",
			data: JSON.stringify(d),
			contentType: "application/json",
			type: "PATCH",
			success: function(){
				alert("Biscuits and gravy!");
			},
			error: function(response) {
				console.log(response.responseText);
			}
		});
	});

	removeButton.click(function() {
		var new_array = [];
		_.each(v_array, function(vid) {
			if(vid != v_uri) {
				new_array.push(vid);
			}
		});
		d = {"favorites": new_array};
		$.ajax({
			url: user_uri,
			dataType: "json",
			data: JSON.stringify(d),
			contentType: "application/json",
			type: "PATCH",
			success: function(response){
				alert("Biscuits and gravy!");
			},
			error: function(response) {
				console.log(response.responseText);
			}
		});
	});

	flagButton.click(function() {
		var d = {"is_tricking": false};
		$.ajax({
			url: v_uri,
			dataType: "json",
			data: JSON.stringify(d),
			contentType: "application/json",
			type: "PUT",
			success: function(response) {
				alert("Video flagged!");
				flagButton.hide();
			},
			error: function(response) {
				console.log(response.responseText)
			}
		})
	});
};