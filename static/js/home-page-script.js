let flag = [false,false,false,false,false,false,false,false,false,]
let input = []
// document.querySelectorAll('.input-btn-pill').forEach(btn => {
//     btn.addEventListener('click', event => {
//         if(true) {
//             btn.style.backgroundColor = "#EEEEEE"
//             btn.style.boxShadow = "10px 10px 25px rgba(74, 243, 203, 0.15), -10px 10px 25px rgba(74, 243, 203, 0.15);"
//             btn.childNodes[1].style.color = "#292929"
//             console.log("clicked")
//         }
//         else {
//             btn.style.backgroundColor = "#0c0c0c"
//             btn.style.boxShadow = null;
//             btn.childNodes[1].style.color = "#9A9999"
//         }
//     })
// })

document.querySelector("#i1").addEventListener("click",() => {
    btn = document.getElementById("i1")
    input_text = btn.childNodes[1]
    if(!flag[0]) {
        btn.style.backgroundColor = "#EEEEEE"
        btn.style.boxShadow = "10px 10px 25px rgba(74, 243, 203, 0.15), -10px 10px 25px rgba(74, 243, 203, 0.15);"
        input_text.style.color = "#292929"
        flag[0] = true
        input.push(input_text.innerHTML)
        console.log(input)
    }
    else {
        btn.style.backgroundColor = "#0c0c0c"
        btn.style.boxShadow = null;
        input_text.style.color = "#9A9999"
        flag[0] = false
        input = input.filter((value,index,arr) => value != input_text.innerHTML)
        console.log(input)
    }
})

document.querySelector("#i2").addEventListener("click",() => {
    btn = document.getElementById("i2")
    input_text = btn.childNodes[1]
    if(!flag[1]) {
        btn.style.backgroundColor = "#EEEEEE"
        btn.style.boxShadow = "10px 10px 25px rgba(74, 243, 203, 0.15), -10px 10px 25px rgba(74, 243, 203, 0.15);"
        input_text.style.color = "#292929"
        flag[1] = true
        input.push(input_text.innerHTML)
        console.log(input)
    }
    else {
        btn.style.backgroundColor = "#0c0c0c"
        btn.style.boxShadow = null;
        input_text.style.color = "#9A9999"
        flag[1] = false
        input = input.filter((value,index,arr) => value != input_text.innerHTML)
        console.log(input)
    }
})

document.querySelector("#i3").addEventListener("click",() => {
    btn = document.getElementById("i3")
    input_text = btn.childNodes[1]
    if(!flag[2]) {
        btn.style.backgroundColor = "#EEEEEE"
        btn.style.boxShadow = "10px 10px 25px rgba(74, 243, 203, 0.15), -10px 10px 25px rgba(74, 243, 203, 0.15);"
        input_text.style.color = "#292929"
        flag[2] = true
        input.push(input_text.innerHTML)
        console.log(input)
    }
    else {
        btn.style.backgroundColor = "#0c0c0c"
        btn.style.boxShadow = null;
        input_text.style.color = "#9A9999"
        flag[2] = false
        input = input.filter((value,index,arr) => value != input_text.innerHTML)
        console.log(input)
    }
})

document.querySelector("#i4").addEventListener("click",() => {
    btn = document.getElementById("i4")
    input_text = btn.childNodes[1]
    if(!flag[3]) {
        btn.style.backgroundColor = "#EEEEEE"
        btn.style.boxShadow = "10px 10px 25px rgba(74, 243, 203, 0.15), -10px 10px 25px rgba(74, 243, 203, 0.15);"
        input_text.style.color = "#292929"
        flag[3] = true
        input.push(input_text.innerHTML)
        console.log(input)
    }
    else {
        btn.style.backgroundColor = "#0c0c0c"
        btn.style.boxShadow = null;
        input_text.style.color = "#9A9999"
        flag[3] = false
        input = input.filter((value,index,arr) => value != input_text.innerHTML)
        console.log(input)
    }
})

document.querySelector("#i5").addEventListener("click",() => {
    btn = document.getElementById("i5")
    input_text = btn.childNodes[1]
    if(!flag[4]) {
        btn.style.backgroundColor = "#EEEEEE"
        btn.style.boxShadow = "10px 10px 25px rgba(74, 243, 203, 0.15), -10px 10px 25px rgba(74, 243, 203, 0.15);"
        input_text.style.color = "#292929"
        flag[4] = true
        input.push(input_text.innerHTML)
        console.log(input)
    }
    else {
        btn.style.backgroundColor = "#0c0c0c"
        btn.style.boxShadow = null;
        input_text.style.color = "#9A9999"
        flag[4] = false
        input = input.filter((value,index,arr) => value != input_text.innerHTML)
        console.log(input)
    }
})

document.querySelector("#i6").addEventListener("click",() => {
    btn = document.getElementById("i6")
    input_text = btn.childNodes[1]
    if(!flag[5]) {
        btn.style.backgroundColor = "#EEEEEE"
        btn.style.boxShadow = "10px 10px 25px rgba(74, 243, 203, 0.15), -10px 10px 25px rgba(74, 243, 203, 0.15);"
        input_text.style.color = "#292929"
        flag[5] = true
        input.push(input_text.innerHTML)
        console.log(input)
    }
    else {
        btn.style.backgroundColor = "#0c0c0c"
        btn.style.boxShadow = null;
        input_text.style.color = "#9A9999"
        flag[5] = false
        input = input.filter((value,index,arr) => value != input_text.innerHTML)
        console.log(input)
    }
})

document.querySelector("#i7").addEventListener("click",() => {
    btn = document.getElementById("i7")
    input_text = btn.childNodes[1]
    if(!flag[6]) {
        btn.style.backgroundColor = "#EEEEEE"
        btn.style.boxShadow = "10px 10px 25px rgba(74, 243, 203, 0.15), -10px 10px 25px rgba(74, 243, 203, 0.15);"
        input_text.style.color = "#292929"
        flag[6] = true
        input.push(input_text.innerHTML)
        console.log(input)
    }
    else {
        btn.style.backgroundColor = "#0c0c0c"
        btn.style.boxShadow = null;
        input_text.style.color = "#9A9999"
        flag[6] = false
        input = input.filter((value,index,arr) => value != input_text.innerHTML)
        console.log(input)
    }
})

document.querySelector("#i8").addEventListener("click",() => {
    btn = document.getElementById("i8")
    input_text = btn.childNodes[1]
    if(!flag[7]) {
        btn.style.backgroundColor = "#EEEEEE"
        btn.style.boxShadow = "10px 10px 25px rgba(74, 243, 203, 0.15), -10px 10px 25px rgba(74, 243, 203, 0.15);"
        input_text.style.color = "#292929"
        flag[7] = true
        input.push(input_text.innerHTML)
        console.log(input)
    }
    else {
        btn.style.backgroundColor = "#0c0c0c"
        btn.style.boxShadow = null;
        input_text.style.color = "#9A9999"
        flag[7] = false
        input = input.filter((value,index,arr) => value != input_text.innerHTML)
        console.log(input)
    }
})

document.querySelector("#i9").addEventListener("click",() => {
    btn = document.getElementById("i9")
    input_text = btn.childNodes[1]
    if(!flag[8]) {
        btn.style.backgroundColor = "#EEEEEE"
        btn.style.boxShadow = "10px 10px 25px rgba(74, 243, 203, 0.15), -10px 10px 25px rgba(74, 243, 203, 0.15);"
        input_text.style.color = "#292929"
        flag[8] = true
        input.push(input_text.innerHTML)
        console.log(input)
    }
    else {
        btn.style.backgroundColor = "#0c0c0c"
        btn.style.boxShadow = null;
        input_text.style.color = "#9A9999"
        flag[8] = false
        input = input.filter((value,index,arr) => value != input_text.innerHTML)
        console.log(input)
    }
})