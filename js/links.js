// smart links

// https://stackoverflow.com/questions/3646914/how-do-i-check-if-file-exists-in-jquery-or-pure-javascript
// function UrlExists(url) {
//     var http = new XMLHttpRequest();
//     try {
//         http.open('HEAD', url, false);
//         http.send();
//     } catch {
//         console.clear();
//     }
//     return http.status != 404;
// }
async function UrlExists(url, curr) {
    try {
        const save = curr;
        const response = await fetch(url, {
            method: 'HEAD',
            mode: 'cors',
            caches: 'no-cache',
            credentials: 'same-origin'
        })
        // if (url == 'https://cs61a.org/resources.html') {
        //     alert(response.status);
        // }
        // alert(response.status);
        // return 5;
        return [response.ok, save];
        alert(response.ok);
        return true;
    } catch {
        // alert("here");
        console.log("Unexpected fetch error.")
        return false;
    }

    console.log(response);
    console.log(response.status == 404);
    return response.status != 404;
}


// alert(UrlExists('https://feross.org/resume/'));
// alert(UrlExists('https://cs61a.org/lab/sol-lab07/'));
// const xhr = new XMLHttpRequest();
// https://medium.com/@dtkatz/3-ways-to-fix-the-cors-error-and-how-access-control-allow-origin-works-d97d55946d9
// https://github.com/Rob--W/cors-anywhere/#documentation
const proxy = 'https://cors-anywhere.herokuapp.com/'
// const proxy = ''

// const url2 = 'https://cors-anywhere.herokuapp.com/https://cs61a.org/lab/sol-lab06/';

// xhr.open('GET', url2, false);
// // xhr.onreadystatechange = alert;
// xhr.send();
// alert(xhr.status == 404);
// https://stackoverflow.com/questions/5897122/accessing-elements-by-type-in-javascript
var attributes = document.getElementsByTagName('a');
var href;
var curr;
// function RequestFail (curr) {
//     curr.removeAttribute('href');
// }
async function Smartify(){
    for (var i = 0; i < attributes.length; i += 1) {
        curr = attributes[i];
        if (curr.hasAttribute('href')) {
            href = attributes[i].getAttribute('href');
            // alert(href);
            if (href.includes('cs61a.org')) {
                // alert(href);
                const exists = UrlExists(proxy + attributes[i].href, i);
                // exists.then( (val) => alert(val));
                // attributes[val[1]].removeAttribute('href')
                //alert('ignored')
                exists.then((val) => !val[0] ? attributes[val[1]].removeAttribute('href') : 1);
                // alert('done');
                // alert(exists);
                // if (!exists) {
                //     curr.removeAttribute('href');
                // }
            } else {
                // continue;
                if (href.length >= 6) {
                    // if (href.includes('assets')) {
                    if (href.substring(0, 6) === 'assets') {
                        var url = attributes[i].href;
                        if (url.length >= 4) {
                            if (url.substring(0, 4) === 'http') {
                                // alert(url);
                                const exists = UrlExists(attributes[i].href, i);
                                exists.then((val) => !val[0] ? attributes[val[1]].removeAttribute('href') : 1);
                                
                                // var exists = UrlExists(attributes[i].href);
                                // if (!exists) {
                                //     curr.removeAttribute('href');
                                //     // alert(url);
                                //     // alert('here');
                                // }

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
}
Smartify();
// for (var i = 0; i < attributes.length; i += 1) {
//     curr = attributes[i];
//     if (curr.hasAttribute('href')) {
//         href = attributes[i].getAttribute('href');
//         // alert(href);
//         if (href.includes('cs61a.org')) {
//             var exists = UrlExists(proxy + attributes[i].href);
//             if (!exists) {
//                 curr.removeAttribute('href');
//             }
//         } else {
//             if (href.length >= 6) {
//                 // if (href.includes('assets')) {
//                 if (href.substring(0, 6) === 'assets') {
//                     var url = attributes[i].href;
//                     if (url.length >= 4) {
//                         if (url.substring(0, 4) === 'http') {
//                             // alert(url);
//                             var exists = UrlExists(attributes[i].href);
//                             if (!exists) {
//                                 curr.removeAttribute('href');
//                                 // alert(url);
//                                 // alert('here');
//                             }
//                             // alert(UrlExists(attributes[i].href));
//                         }
//                     }
//                     // var asset = new File('/' + href);
//                     // alert(href);
//                     // if (asset.exists()) {
//                     //     alert('found')
//                     // } else {
//                     //     alert('skipped');
//                     // }
//                 }
//             }
//         }

//             // alert(attributes[i].href.substring(0, 6));
//             // alert(href.substring(0, 6));
//             // alert('assets')
//             // if (href.substring(0, 6) === 'assets') {
//             //     alert(href);
//             // }
//             // alert('here');
//         // }

//     }
// }
