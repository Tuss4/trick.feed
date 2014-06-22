var Search = function(titles) {
    var title_list = titles
	$(document).ready(function() {
    search_input.typeahead({
            hint: true,
            highlight: true,
            minLength: 1
        },
        {
            name: 'titles',
            displayKey: 'value',
            source: substringMatcher(titles)
        });
	});

    // String matcher adapted from
    // http://twitter.github.io/typeahead.js/examples/

    var substringMatcher = function(strs) {
        return function findMatches(q, cb) {
            var matches, substringRegex;
            matches = [];
            substrRegex = new RegExp(q, 'i');
            $.each(strs, function(i, str) {
                if (substrRegex.test(str)) {
                    matches.push({ value: str });
                }
            });
            cb(matches);
        };
    };

    // Typeahead logic
    var search_input = $('#video-search');
}