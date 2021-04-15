var dpi_x = document.getElementById('dpi').offsetWidth;
var dpi_y = document.getElementById('dpi').offsetHeight;

var width = screen.width / dpi_x;
var height = screen.height / dpi_y;

console.log("Width: "+ width);
console.log("Height: "+ height);

if(width >= 20){
    document.body.style.zoom = "125%";
}
else if(width >= 10){
    document.body.style.zoom = "60%";
}