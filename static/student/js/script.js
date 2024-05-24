function Toggle() {
    var side_nav = document.getElementById("side-nav");

    if (side_nav.style.width === "0px") {
        side_nav.style.width = "300px";
    }
    else{
        side_nav.style.width = "0px";
    }
}
