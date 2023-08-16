let user = document.getElementById("user")
let password = document.getElementById("passwd")
let button = document.getElementById("button")
let auth = false
let uploadbutton = document.getElementById("upload")

button.addEventListener("click", function(){
    if(user.value==="Mark45"&& password.value==="1234"){
        console.log("Correcto, Acceso Aceptado")
        auth = true
        window.location ="/dashboard"
        
    }
    else{
        console.log("Acceso denegado")
    }
})



if(window.location==="/dashboard" && auth===false){
    window.location = "/"
}