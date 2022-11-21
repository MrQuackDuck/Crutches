let bodyHeight = document.querySelector("html").offsetHeight

if (bodyHeight < 800) {
    footer = document.querySelector("footer")
    footer.style.position = "fixed"
    footer.style.bottom = "0"
}