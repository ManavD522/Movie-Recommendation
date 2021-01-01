document.querySelectorAll('.input-btn-pill').forEach(btn => {
    btn.addEventListener('click', event => {
        if(true) {
            btn.style.backgroundColor = "#EEEEEE"
            btn.style.boxShadow = "10px 10px 25px rgba(74, 243, 203, 0.15), -10px 10px 25px rgba(74, 243, 203, 0.15);"
            btn.childNodes[1].style.color = "#292929"
            console.log("clicked")
        }
        else {
            btn.style.backgroundColor = "#0c0c0c"
            btn.style.boxShadow = null;
            btn.childNodes[1].style.color = "#9A9999"
        }
    })
})