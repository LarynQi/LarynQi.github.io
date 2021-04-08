// smart links

// https://stackoverflow.com/questions/3646914/how-do-i-check-if-file-exists-in-jquery-or-pure-javascript

// https://www.freecodecamp.org/news/here-is-the-most-popular-ways-to-make-an-http-request-in-javascript-954ce8c95aaa/
// https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise
// CORS: https://stackoverflow.com/questions/40182785/why-fetch-return-a-response-with-status-0#:~:text=Effectively%2C%20the%20response%20you%20get,CORS%20had%20in%20fact%20failed.
async function UrlExists(url, i) {
    try {
        const save = i;

        const response = await fetch(url, {
            method: 'HEAD',
            mode: 'cors',
            caches: 'no-cache',
            credentials: 'same-origin'
            // headers: {
            //     'X-Requested-With': 'XMLHttpRequest'
            // }
        })
        console.log(url, response.ok, response.status)
        return [response.ok, save];
    } catch {
        console.log("Unexpected fetch error.")
        return false;
    }
}

async function Smartify(){
    // https://medium.com/@dtkatz/3-ways-to-fix-the-cors-error-and-how-access-control-allow-origin-works-d97d55946d9
    // https://github.com/Rob--W/cors-anywhere/#documentation   
    // const proxy = 'https://cors-anywhere.herokuapp.com/'
    // const proxy = 'https://cors-proxy.larynqi.com/'
    const proxy = 'https://lqi-cors-proxy.herokuapp.com/'

    // https://stackoverflow.com/questions/5897122/accessing-elements-by-type-in-javascript
    var attributes = document.getElementsByTagName('a');
    var href;
    var curr;
    for (var i = 0; i < attributes.length; i += 1) {
        curr = attributes[i];
        if (curr.hasAttribute('href')) {
            href = attributes[i].getAttribute('href');
            if (href.includes('cs61a.org')) {
                const exists = UrlExists(proxy + attributes[i].href, i);
                // const exists = UrlExists(attributes[i].href, i);
                exists.then((val) => !val[0] ? attributes[val[1]].removeAttribute('href') : 0);
            } else {
                if (href.length >= 6) {
                    if (href.substring(0, 6) === 'assets') {
                        var url = attributes[i].href;
                        if (url.length >= 4) {
                            if (url.substring(0, 4) === 'http') {
                                const exists = UrlExists(attributes[i].href, i);
                                exists.then((val) => !val[0] ? attributes[val[1]].removeAttribute('href') : 0);
                            }
                        }
                    }
                }
            }
        }
    }
}
Smartify();
