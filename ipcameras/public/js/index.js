frappe.ready(function() {

  $('#mjpeg_wrapper').clipchamp_mjpeg_player(
    'http://24.241.65.53:8081/?action=stream',
    24, // frames per second
    true, // autoloop
    function(wrapperElement, playerInterface) {
      // call playerInterface.finish() to stop the playback
    }); 

});