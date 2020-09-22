var today = new Date(),
    day = today.getDate(),
    month = today.getMonth() + 1;
if (month == 4 && day == 1) {
    alert('A N N O U N C E M E N T S');
    document.getElementById("a n n o u n c e m e n t s").style.fontSize = "9rem";
    var denero = document.getElementById("denero")
    denero.style.maxWidth = "600px";
    denero.style.maxHeight = "800px";
    denero.style.left = "45vw";
    denero.style.top = "5vw";
}
