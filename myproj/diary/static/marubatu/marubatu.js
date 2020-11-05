let flag = true;

function show_maru_batu(table_id, onclick_flag = true) {
  // Display maru_batu with this function.
  let tmp = document.getElementById(table_id);
  let button2 = document.getElementById("teaching_order");

  if (flag == true) {
    tmp.innerHTML = "〇";
    button2.innerHTML = "次 → 後攻 ×";
    flag = false;
  } else {
    tmp.innerHTML = "×";
    button2.innerHTML = "次 → 先攻 〇";
    flag = true;
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
}
