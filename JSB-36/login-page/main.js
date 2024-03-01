let username = document.getElementById("username-input");
let password = document.getElementById("password-input");

let loginBtn = document.querySelector(".login-btn");

loginBtn.onclick = function () {
    if (username.value == "admin" && password.value == "admin") {
        window.location.href = "https://www.google.com/";
    } else {
        alert("That bai");
    }
};
