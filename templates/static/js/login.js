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

function passtoggle() {
    var y = document.getElementById("password");
    if (y.type === "password") {
      y.type = "text";
    } else {
      y.type = "password";
    }
  }