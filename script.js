console.log("Hello World");
document.write("Hello World")
console.log(259);
document.write('<span style="color: red;font-size:50px">Hello World</span>')




// function textbreak(){
//     var h1 = document.querySelector("h1")
//     var h1Text = h1.textContent
//     var splittedText = h1Text.split("")

//     var clutter = ""
//     splittedText.forEach(function(elem){
//     clutter += `<span>${elem}</span>`
// })

// h1.innerHTML = clutter
// }
// textbreak()


gsap.from("h1",{
    y:-150,
    delay:1,
    duration:1,
    ease:"bounce.out",
})