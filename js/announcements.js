var today = new Date(),
    day = today.getDate(),
    month = today.getMonth() + 1;
if (month == 4 && day == 1) {
    alert('A N N O U N C E M E N T S');
    document.getElementById("a n n o u n c e m e n t s").style.fontSize = "9rem";
    var denero = document.getElementById("denero");
    denero.style.maxWidth = "600px";
    denero.style.maxHeight = "800px";
    denero.style.left = "45vw";
    denero.style.top = "5vw";
    denero.onclick = function () {var audio = new Audio("https://raw.githubusercontent.com/larynqi/larynqi.github.io/master/assets/audio/Announcements!.mp3"); audio.play();};
    document.getElementById("denero-link").removeAttribute("href");
    denero.style.cursor = "pointer";
    // var audio = new Audio("https://raw.githubusercontent.com/larynqi/larynqi.github.io/master/assets/audio/Announcements!.mp3");
    // audio.play()
    // document.getElementById("denero-audio").play();
} else {
    var denero = document.getElementById("denero");
    denero.onclick = function () {var audio = new Audio("https://raw.githubusercontent.com/larynqi/larynqi.github.io/master/assets/audio/announcements.mov"); audio.play();};
    document.getElementById("denero-link").removeAttribute("href");
    denero.style.cursor = "pointer";
    var hug = document.getElementById("hug");
    hug.onclick = function () {var audio = new Audio("https://raw.githubusercontent.com/larynqi/larynqi.github.io/master/assets/audio/hello.MOV"); audio.play();};
    document.getElementById("hug-link").removeAttribute("href");
    hug.style.cursor = "pointer";
    var hilfinger = document.getElementById("hilfinger");
    hilfinger.onclick = function () {var audio = new Audio("https://raw.githubusercontent.com/larynqi/larynqi.github.io/master/assets/audio/im_severus_snape.mov"); audio.play();};
    document.getElementById("hilfinger-link").removeAttribute("href");
    hilfinger.style.cursor = "pointer";
}