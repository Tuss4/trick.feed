var TheatreApp = function(vid_id) {
    $(document).ready(function() {
        var tButton = $('.theatre-mode');
        var vOver = $('.video-overlay');
        tButton.click(function() {
            vOver.show();
            alert(vid_id);
            var player;
            function onYouTubeIframeAPIReady() {
            	player = new YT.Player('player', {
            		height: '480',
            		width: '720',
            		videoId: vid_id,
            		events: {
            			'onReady': onPlayerReady,
            			'onStateChange': onPlayerStateChange
            		}
            	});
            };

            function onPlayerReady(event) {
            	event.target.playVideo();
            };

            
        });
    }); 
}; 