let input = []
document.querySelectorAll('#input-btn').forEach(btn => {
    btn.addEventListener('click', event => {
        let input_text = btn.childNodes[1]
        let movie_id = btn.childNodes[3].value
        if(btn.classList == "input-btn-pill-unchecked") {
            btn.classList = "input-btn-pill-checked"
            
            input.push(movie_id)
            input_text.style.color = "#292929"
            console.log(input)
        }
        else {
            btn.classList = "input-btn-pill-unchecked"

            btn.childNodes[1].style.color = "#9A9999"
            input = input.filter((value, i, arr) => value != movie_id)
            console.log(input)
        }
    })
})

document.querySelector(".submit").addEventListener('click', () => {
    if(input.length >= 8) {
        $.ajax({
            type: "POST",
            url: '/welcome',
            dataType: false,
            contentype: "application/json",
            data: JSON.stringify(input),
            success: function () {
                alert("Thanks!"); 
            }
        })
    }
    else {
        document.querySelector(".validate").style.display = "block"
    }
})