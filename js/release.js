var today = new Date(),
    day = today.getDate(),
    month = today.getMonth() + 1;
if (month == 9 && day >= 26) {
    var sol06 = document.getElementById("61a-06");
    // sol06.href = "assets/fa20-csm/61a-6-sol.pdf";
    sol06.setAttribute("href", "assets/fa20-csm/61a-6-sol.pdf");
}