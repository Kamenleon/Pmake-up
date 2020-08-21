

window.onload = function getActData() {
  //ここで結果を受け取り、任意の変数に代入する
  console.log("OKKKKKKKK");
  var ans = document.getElementById("ansName").value;
  console.log(ans);
  //$.getJSON("{{ url_for('js', filename='actData.json') }}", function (data) {
    $.getJSON("http://localhost:8000/js/actData.json", function (data) {
    //↓actDataの配列内を検索
    for (var i = 0; i < Object.keys(data.actData).length; i++) {
      //↓結果と一致するnameの各データを取得し、画面に出力する
      if (ans == data.actData[i].name) {
        var parent = document.getElementById("result");
        var p = document.createElement("p");
        p.innerHTML = "生年月日：" + data.actData[i].birthday + "<br>血液型：" + data.actData[i].bloodType + "<br>代表作：" + data.actData[i].work + "<br>WikiPedia：" + data.actData[i].wiki;
        parent.appendChild(p);
      }
    }
  })
}