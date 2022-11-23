let bodyHeight = document.querySelector("html").offsetHeight

if (bodyHeight < 900) {
    footer = document.querySelector("footer")
    footer.style.position = "fixed"
    footer.style.bottom = "0"
}