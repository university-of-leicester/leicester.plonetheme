jq(document).ready(function() {
    jq('img.image-right .overlay, img.image-right-border .overlay, img.image-left .overlay,img.image-left-border .overlay, img.image-inline .overlay')
        .prepOverlay({
            subtype: 'image',
            urlmatch: '/@@images/.+$',
            urlreplace: '/image',
            });
			
});
