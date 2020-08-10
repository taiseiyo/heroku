function scrollToTop() {
  scrollTo(0, 0);
}

function scrollToDown() {
  let h = document.documentElement.scrollHeight;
  scrollTo(0, h);
}

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
  img.animate([{opacity: "0"}, {opacity: "1"}], 2000);
  setTimeout("slide_picture()", 5000);
}
slide_picture();

// 即時関数作ってみる
