let arr = Array(1, 72)
  .fill()
  .map((_, i) => i);

let a = arr.length;

//シャッフルアルゴリズム
while (a) {
  let j = Math.floor(Math.random() * a);
  let t = arr[--a];
  arr[a] = arr[j];
  arr[j] = t;
}

let ids = ["id1", "id2", "id3", "id4", "id5", "id6", "id7", "id8", "id9"];
