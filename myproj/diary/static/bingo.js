let arr = new Array(72);
let serial_num = 1; // 連番用

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
