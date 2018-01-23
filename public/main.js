
// $('.grade-wrapper').on("click", function(e){
  //e.preventDefault()
  //$(this).find("div").slideToggle("slow", function () {
  //});
//})

// const button1 = document.querySelector("#script1");
// const button2 = document.querySelector("#script2");
// const button3 = document.querySelector("#script3");
// const button4 = document.querySelector("#script4");

// button1.addEventListener("click", () => fetchStartEndpoint(button1.dataset.filename));
// button2.addEventListener("click", () => fetchStartEndpoint(button2.dataset.filename));
// button3.addEventListener("click", () => fetchStartEndpoint(button3.dataset.filename));
// button4.addEventListener("click", () => fetchStartEndpoint(button4.dataset.filename));
// the below function is what retrieves the scripts and is called
// in the functions in the buttons
function fetchStartEndpoint(fileName) {
  fetch(`/start/${fileName}`)
    .catch(error => console.log(error));
}
//below are the functions that are connected to the scripts
//these just retrieve the buttons that run the scripts based
//on the lesson and are linked to the permanent table.
$(document).ready(function(){
  $(".SunMotion").click(function(){
    $("#SunMotion").toggleClass("invisible visible",);
  });
  $(".Hologram").click(function(){
    $("#Hologram").toggleClass("invisible visible",);
  });
  $(".Halloween").click(function(){
    $("#Halloween").toggleClass("invisible visible",);
  });
  $(".Stories").click(function(){
    $("#Stories").toggleClass("invisible visible",);
  });
  $(".Compound").click(function(){
    $("#Compound").toggleClass("invisible visible",);
  });
  $(".LightVsPig").click(function(){
    $("#LightVsPig").toggleClass("invisible visible",);
  });
  $(".Geometry").click(function(){
    $("#Geometry").toggleClass("invisible visible",);
  });
  $(".Weather").click(function(){
    $("#Weather").toggleClass("invisible visible",);
  });
  $(".Biomes").click(function(){
    $("#Biomes").toggleClass("invisible visible",);
  });
  $(".Music").click(function(){
    $("#Music").toggleClass("invisible visible",);
  });
  $(".Constellations").click(function(){
    $("#Constellations").toggleClass("invisible visible",);
  });
});

//the bellow functions are linked by id to the script buttons
//each script has a check number and that calls the function
//that runs teh script when clicked.

document.getElementById("check1").style.display = 'none';
function check1() {
  var x = document.getElementById("check1");
  if (x.style.display === 'none') {
        x.style.display = 'inline';
  } else {
    x.style.display = 'none';
    document.getElementById("check1").checked = false;
  }
   // Uncomment below and change snow to the correct file name you want to trigger in python_scripts
   // Do the same for all the others below. 
  fetchStartEndpoint("fire.py") 
}
document.getElementById("check3").style.display = 'none';
function check3() {
  var x = document.getElementById("check3");
  if (x.style.display === 'none') {
        x.style.display = 'inline';
  } else {
    x.style.display = 'none';
    document.getElementById("check3").checked = false;
  }
  fetchStartEndpoint("24HourCycle.py")
}
document.getElementById("check4").style.display = 'none';
function check4() {
  var x = document.getElementById("check4");
  if (x.style.display === 'none') {
        x.style.display = 'inline';
  } else {
    x.style.display = 'none';
    document.getElementById("check4").checked = false;
  }
  fetchStartEndpoint("dayMode.py")
}
document.getElementById("check5").style.display = 'none';
function check5() {
  var x = document.getElementById("check5");
  if (x.style.display === 'none') {
        x.style.display = 'inline';
  } else {
    x.style.display = 'none';
    document.getElementById("check5").checked = false;
  }
  fetchStartEndpoint("eveningMode.py")
}

document.getElementById("check7").style.display = 'none';
function check7() {
  var x = document.getElementById("check7");
  if (x.style.display === 'none') {
        x.style.display = 'inline';
  } else {
    x.style.display = 'none';
    document.getElementById("check7").checked = false;
  }
  fetchStartEndpoint("sunny.py")
}

document.getElementById("check8").style.display = 'none';
function check8() {
  var x = document.getElementById("check8");
  if (x.style.display === 'none') {
        x.style.display = 'inline';
  } else {
    x.style.display = 'none';
    document.getElementById("check8").checked = false;
  }
  fetchStartEndpoint("rain.py")
}

document.getElementById("check9").style.display = 'none';
function check9() {
  var x = document.getElementById("check9");
  if (x.style.display === 'none') {
        x.style.display = 'inline';
  } else {
    x.style.display = 'none';
    document.getElementById("check9").checked = false;
  }
  fetchStartEndpoint("snow.py")
}

document.getElementById("check10").style.display = 'none';
function check10() {
  var x = document.getElementById("check10");
  if (x.style.display === 'none') {
        x.style.display = 'inline';
  } else {
    x.style.display = 'none';
    document.getElementById("check10").checked = false;
  }
  fetchStartEndpoint("partlyCloudy.py")
}
document.getElementById("check12").style.display = 'none';
function check12() {
  var x = document.getElementById("check12");
  if (x.style.display === 'none') {
        x.style.display = 'inline';
  } else {
    x.style.display = 'none';
    document.getElementById("check12").checked = false;
  }
  fetchStartEndpoint("red.py")
}

document.getElementById("check13").style.display = 'none';
function check13() {
  var x = document.getElementById("check13");
  if (x.style.display === 'none') {
        x.style.display = 'inline';
  } else {
    x.style.display = 'none';
    document.getElementById("check13").checked = false;
  }
  fetchStartEndpoint("green.py")
}
document.getElementById("check14").style.display = 'none';
function check14() {
  var x = document.getElementById("check14");
  if (x.style.display === 'none') {
        x.style.display = 'inline';
  } else {
    x.style.display = 'none';
    document.getElementById("check14").checked = false;
  }
  fetchStartEndpoint("blue.py")
}
document.getElementById("check15").style.display = 'none';
function check15() {
  var x = document.getElementById("check15");
  if (x.style.display === 'none') {
        x.style.display = 'inline';
  } else {
    x.style.display = 'none';
    document.getElementById("check15").checked = false;
  }
  fetchStartEndpoint("cyan.py")
}
document.getElementById("check16").style.display = 'none';
function check16() {
  var x = document.getElementById("check16");
  if (x.style.display === 'none') {
        x.style.display = 'inline';
  } else {
    x.style.display = 'none';
    document.getElementById("check16").checked = false;
  }
  fetchStartEndpoint("yellow.py")
}
document.getElementById("check17").style.display = 'none';
function check17() {
  var x = document.getElementById("check17");
  if (x.style.display === 'none') {
        x.style.display = 'inline';
  } else {
    x.style.display = 'none';
    document.getElementById("check17").checked = false;
  }
  fetchStartEndpoint("magenta.py")
}

