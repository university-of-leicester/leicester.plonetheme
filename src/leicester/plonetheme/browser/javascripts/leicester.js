jq(document).ready(function() {
    jq('img.overlay')
        .prepOverlay({
            subtype: 'image',
            urlmatch: '/@@images/.+$',
            urlreplace: '/image',
            });
			
});
