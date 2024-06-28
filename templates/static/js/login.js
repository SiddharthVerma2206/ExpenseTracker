function loginpop() {
    document.getElementById("overlay").style.display = "block";
    document.getElementById("loginpop").style.display = "block";
}

function closeloginpop() {
    document.getElementById("overlay").style.display = "none";
    document.getElementById("loginpop").style.display = "none";
}

document.getElementById("overlay").addEventListener("click", function() {
    closeloginpop();
});