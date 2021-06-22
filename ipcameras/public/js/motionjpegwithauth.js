/**
 * Implementation of a Motion JPEG with requests requiring Digest Authentication.
 * 
 */
 async function authMJPEG(id) {
    const url = "http://24.241.65.53:8081/?action=stream";
    const JPEG_MAGIG_NUMBER = [0xff, 0xd8, 0xff];

    var image = $(id), src;

    // if element is not found do nothing
    if (!image.length) return;

    //const url = image.attr("src");

    fetch(url)
    .then(response => {

        if (!response.ok) {
            throw Error(response.status+' '+response.statusText)
        }

        if (!response.body) {
            throw Error('ReadableStream not yet supported in this browser.')
        }

        console.log("readable stream");
        //console.log(response.body);
        
        const reader = response.body.getReader();

        const read = () => {

            reader.read().then( function processFrames ({done, value}) {
                if (done) {
                    controller.close();
                    return;
                }
                
                var startIndex;
                var jpegs = [];

                for (let index = 0; index < value.length; index++) {
                    
                    if (value[index] === JPEG_MAGIG_NUMBER[0] && value[index + 1] === JPEG_MAGIG_NUMBER[1] && value[index + 2] === JPEG_MAGIG_NUMBER[2]) {
                        if (index > 0 && typeof startIndex === 'number') {
                            //jpegs.push(new Blob([value.subarray(startIndex, index)], {type: 'image/jpeg'}));
                            document.getElementById('image').src = URL.createObjectURL(new Blob([value.subarray(startIndex, index)], {type: 'image/jpeg'}));
                            //frames++;
                            console.log("image added");
                        }
                        startIndex = index;
                    }
                    
                }

                // Read some more, and call this function again
                return reader.read().then(processFrames);
            }).catch(error => {
                console.error(error);
            })
        }
        
        read();
        
    }).catch(error => {
        console.error('There has been a problem with your fetch operation:', error);
})


    
}

