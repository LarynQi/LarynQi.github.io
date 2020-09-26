var today = new Date(),
    day = today.getDate(),
    month = today.getMonth() + 1,
    hour = today.getHours();
if (month == 10 && day >= 1) {
    var sol06 = document.getElementById("61a-06-sol");
    if (day == 1) {
        if (hour >= 12) {
            sol06.setAttribute("href", "assets/fa20-csm/61a-6-sol.pdf");
        }
    } else {
        sol06.setAttribute("href", "assets/fa20-csm/61a-6-sol.pdf");
    }
    // sol06.href = "assets/fa20-csm/61a-6-sol.pdf";
}