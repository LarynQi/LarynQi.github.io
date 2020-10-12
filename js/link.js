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
                alert(url);
                if (url.length >= 4) {
                    if (url.substring(0, 4) === 'http') {
                        alert(url);
                        var exists = UrlExists(attributes[i].href);
                        if (!exists) {
                            curr.remove();
                        }
                        alert(UrlExists(attributes[i].href));
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

// var today = new Date(),
//     day = today.getDate(),
//     month = today.getMonth() + 1;
// if (month == 4 && day == 1) {
//     alert('A N N O U N C E M E N T S');
//     document.getElementById("a n n o u n c e m e n t s").style.fontSize = "9rem";
//     var denero = document.getElementById("denero");
//     denero.style.maxWidth = "600px";
//     denero.style.maxHeight = "800px";
//     denero.style.left = "45vw";
//     denero.style.top = "5vw";
//     denero.onclick = function () {var audio = new Audio("https://raw.githubusercontent.com/larynqi/larynqi.github.io/master/assets/audio/Announcements!.mp3"); audio.play();};
//     document.getElementById("denero-link").removeAttribute("href");
//     denero.style.cursor = "pointer";
//     // var audio = new Audio("https://raw.githubusercontent.com/larynqi/larynqi.github.io/master/assets/audio/Announcements!.mp3");
//     // audio.play()
//     // document.getElementById("denero-audio").play();
// } else {
//     var denero = document.getElementById("denero");
//     denero.onclick = function () {var audio = new Audio("https://raw.githubusercontent.com/larynqi/larynqi.github.io/master/assets/audio/announcements.mov"); audio.play();};
//     document.getElementById("denero-link").removeAttribute("href");
//     denero.style.cursor = "pointer";
//     var hug = document.getElementById("hug");
//     hug.onclick = function () {var audio = new Audio("https://raw.githubusercontent.com/larynqi/larynqi.github.io/master/assets/audio/hello.MOV"); audio.play();};
//     document.getElementById("hug-link").removeAttribute("href");
//     hug.style.cursor = "pointer";
// }