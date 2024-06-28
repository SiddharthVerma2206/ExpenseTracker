function incomepopup() {
    document.getElementById("overlay").style.display = "block";
    document.getElementById("popupDialogforincome").style.display = "block";
}

function closeincomepopup() {
    document.getElementById("overlay").style.display = "none";
    document.getElementById("popupDialogforincome").style.display = "none";
}

document.getElementById("overlay").addEventListener("click", function() {
    closeincomepopup();
});