// smart links

// https://stackoverflow.com/questions/3646914/how-do-i-check-if-file-exists-in-jquery-or-pure-javascript
function UrlExists(url) {
    var http = new XMLHttpRequest();
    http.open('HEAD', url, false);
    http.send();
    return http.status != 404;
}

// https://stackoverflow.com/questions/5897122/accessing-elements-by-type-in-javascript
var attributes = document.getElementsByTagName('a');
var href;
var curr;
for (var i = 0; i < attributes.length; i += 1) {
    curr = attributes[i];
    if (curr.hasAttribute('href')) {
        href = attributes[i].getAttribute('href');
        // alert(href);
        if (href.length >= 6) {
            // if (href.includes('assets')) {
            if (href.substring(0, 6) === 'assets') {
                var url = attributes[i].href;
                if (url.length >= 4) {
                    if (url.substring(0, 4) === 'http') {
                        // alert(url);
                        var exists = UrlExists(attributes[i].href);
                        if (!exists) {
                            curr.removeAttribute('href');
                            // alert(url);
                        }
                        // alert(UrlExists(attributes[i].href));
                    }
                }
                // var asset = new File('/' + href);
                // alert(href);
                // if (asset.exists()) {
                //     alert('found')
                // } else {
                //     alert('skipped');
                // }
            }
        }
            // alert(attributes[i].href.substring(0, 6));
            // alert(href.substring(0, 6));
            // alert('assets')
            // if (href.substring(0, 6) === 'assets') {
            //     alert(href);
            // }
            // alert('here');
        // }

    }
}
