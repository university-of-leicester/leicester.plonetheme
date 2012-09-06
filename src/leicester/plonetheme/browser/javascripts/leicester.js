jq(document).ready(function() {
    jq('img.image-right, img.image-right-border, img.image-left,img.image-left-border, img.image-inline')
        .prepOverlay({
            subtype: 'image',
            urlmatch: '/@@images/.+$',
            urlreplace: '/image',
            });
});
