function navToggle() {
    var x = document.getElementById("links");
    if (x.className === "hide-mobile") {
        x.className = "";
    } else {
        x.className = "hide-mobile";
    }
}