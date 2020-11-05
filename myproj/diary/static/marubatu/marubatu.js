let flag = true;
let id_list = ["id0", "id1", "id2", "id3", "id4", "id5", "id6", "id7", "id8"];

function show_maru_batu(table_id, onclick_flag = true) {
  // Display maru_batu with this function.
  let tmp = document.getElementById(table_id);
  let button2 = document.getElementById("teaching_order");

  if (id_list.includes(table_id) == true && flag == true) {
    tmp.innerHTML = "〇";
    button2.innerHTML = "次 → 後攻 ×";
    flag = false;
    id_list.splice(id_list.indexOf(table_id), 1);
  } else if (id_list.includes(table_id) == true && flag == false) {
    tmp.innerHTML = "×";
    button2.innerHTML = "次 → 先攻 〇";
    flag = true;
    id_list.splice(id_list.indexOf(table_id), 1);
  }
}

function playing_first() {
  for (let i = 0; i <= 8; i++) {
    let ids = document.getElementById("id" + i);
    ids.innerHTML = "△";
  }
  flag = true;
  let button2 = document.getElementById("teaching_order");
  button2.innerHTML = "次 → 先攻 〇";
  id_list = ["id0", "id1", "id2", "id3", "id4", "id5", "id6", "id7", "id8"];
}
