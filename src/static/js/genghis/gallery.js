/* Pretty Photo for Gallery*/

/*

var photoImages = new Array();
var photoNames = new Array();
var photoDescriptions = new Array();

$("a[class^='prettyPhoto']").each(function() {
	var id = $(this).attr('id').substr(11);
	photoImages.push($('img#photo-' + id).attr('src'));
	photoNames.push($('input#photo-name-' + id).val());
	photoDescriptions.push($('input#photo-description-' + id).val());
});

$().prettyPhoto.open(photoImages, photoNames, photoDescriptions);

*/

$("a[class^='prettyPhoto']").prettyPhoto({
	overlay_gallery: false,
	social_tools: false,
	allow_resize: true,
	animation_speed: 'fast'
});
