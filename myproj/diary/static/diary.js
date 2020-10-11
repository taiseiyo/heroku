function scrollToTop() {
  scrollTo(0, 0);
}

function scrollToDown() {
  let h = document.documentElement.scrollHeight;
  scrollTo(0, h);
}

let num = 0;
function slide_picture() {
  let pic = new Array(
    "../../../static/star.jpg",
    "../../../static/star2.jpg",
    "../../../static/castle.jpg",
  );

  if (num == 2) {
    num = 0;
  } else {
    num = num + 1;
  }
  document.getElementById("mypic").src = pic[num];
  // const img = document.querySelector("#mypic");
  const img = document.getElementById("mypic");
  img.animate([{opacity: "0.4"}, {opacity: "1"}], 10000);
}

setInterval(slide_picture, 10000);

let value = 0;
let imgWidth = -750;
let flag = true;
function animation_background() {
  document.getElementById("skinBody").style.backgroundPosition = value + "px";
  if (flag == true) {
    value = value - 1;
    if (value == imgWidth) {
      flag = false;
    }
  } else if (flag == false) {
    value = value + 1;
    if (value == 0) {
      flag = true;
    }
  }
}

setInterval(animation_background, 20);
