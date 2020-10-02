let arr = new Array(72);
let serial_num = 1; // 連番用
let flag = false; //ループを止めるスイッチ用

for (let i = 0; i < arr.length; i++) {
  arr[i] = serial_num;
  serial_num++;
}

let a = arr.length;

//シャッフルアルゴリズム
while (a) {
  let j = Math.floor(Math.random() * a);
  let t = arr[--a];
  arr[a] = arr[j];
  arr[j] = t;
}

let ids = ["id1", "id2", "id3", "id4", "id5", "id6", "id7", "id8", "id9"];

function display_suzi() {
  let min = 1;
  let max = 72;
  let a = Math.floor(Math.random() * (max + 1 - min)) + min;
  document.getElementById("id10").textContent = a;
}

let music;

function startMusic() {
  music = new Audio();
  music.src =
    "https://raw.githubusercontent.com/taiseiyo/heroku/master/myproj/diary/static/music/shining_star.mp3";
  music.play(); // 再生
}

function stopMusic() {
  music.pause(); // 停止
}

function startBingo() {
  testTimer = setInterval("display_suzi()", 10);
}

function stopBingo() {
  clearInterval(testTimer);
  console.log(document.getElementById("id10").textContent);
}
