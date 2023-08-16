let input = document.getElementById("input")
let button = document.getElementById("button")

button.addEventListener("click", function(){
    window.location="/view/"+input.value
    console.log("Accediendo")
})