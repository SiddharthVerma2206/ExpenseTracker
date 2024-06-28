function signupop() {
    document.getElementById("overlay").style.display = "block";
    document.getElementById("signupop").style.display = "block";
}

function closesignupop() {
    document.getElementById("overlay").style.display = "none";
    document.getElementById("signupop").style.display = "none";
}

document.getElementById("overlay").addEventListener("click", function() {
    closesignupop();
});