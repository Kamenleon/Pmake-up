//顔の形のグラフ作成
var ctx = document.getElementById('pkChart').getContext('2d');
var chart = new Chart(ctx, {
  type: 'doughnut',
  data: {
    labels: ['丸(' + pk1 + '%)', '面長(' + pk2 + '%)', '逆三角(' + pk3 + '%)', '四角(' + pk4 + '%)', '卵(' + pk5 + '%)'],
    datasets: [{
      backgroundColor: ['rgb(241,158,194)', 'rgb(255,231,63)', 'rgb(246,173,60)', 'rgb(135,202,178)', 'rgb(64,124,192)'],
      data: [pk1, pk2, pk3, pk4, pk5],

    }]
  },
  options: {
  }
});

//春夏秋冬のグラフ作成
var ctx = document.getElementById('ppChart').getContext('2d');
var chart = new Chart(ctx, {
  type: 'doughnut',
  data: {
    labels: ['夏(' + pp1 + '%)', '冬(' + pp2 + '%)', '春(' + pp3 + '%)', '秋(' + pp4 + '%)'],
    datasets: [{
      backgroundColor: ['rgb(23,120,255)', 'rgb(80,186,0)', 'rgb(255,105,180)', 'rgb(255,143,23)'],
      data: [pp1, pp2, pp3, pp4]

    }]
  },
  options: {}
});

//#canvasAreaにCSS追加
$("#canvasArea").css({ 'display': 'inline-block' });

//アドバイスの出力
window.onload = function getMakeData() {

  //$.getJSON('actData.json', function (data) {
  $.getJSON("/js/makeData.json", function (data) {
    //↓actDataの配列内を検索
    for (var i = 0; i < Object.keys(data.makeData).length; i++) {
      //↓結果と一致するnameの各データを取得し、画面に出力する

      if (pkAns == data.makeData[i].pkName) {

        var parent = document.getElementById("pkResult");
        var p = document.createElement("p");
        p.innerHTML = data.makeData[i].summary;
        parent.appendChild(p);

      }

      if (ppAns == data.makeData[i].ppName) {

        var parent1 = document.getElementById("ppResult");
        var p1 = document.createElement("p");
        p1.innerHTML = data.makeData[i].summary;
        parent1.appendChild(p1);

        var parent2 = document.getElementById("fashionResult");
        var p2 = document.createElement("p");
        p2.innerHTML = data.makeData[i].fashion;
        parent2.appendChild(p2);

      }
    }
  })

  //似合う色の出力
  switch (ppAns) {
    case '春':
      $("#color1").css({ 'background-color': '#e07481' });
      $("#color2").css({ 'background-color': '#e9923a' });
      $("#color3").css({ 'background-color': '#f4e158' });
      $("#color4").css({ 'background-color': '#67b46a' });
      $("#color5").css({ 'background-color': '#e4745c' });
      $("#color6").css({ 'background-color': '#ebd262' });
      $("#color7").css({ 'background-color': '#7c93b3' });
      $("#color8").css({ 'background-color': '#d6ab64' });
      break;
    case '夏':
      $("#color1").css({ 'background-color': '#34435c' });
      $("#color2").css({ 'background-color': '#c10f57' });
      $("#color3").css({ 'background-color': '#109f76' });
      $("#color4").css({ 'background-color': '#e899bb' });
      $("#color5").css({ 'background-color': '#f0ebb5' });
      $("#color6").css({ 'background-color': '#a1cda8' });
      $("#color7").css({ 'background-color': '#e07481' });
      $("#color8").css({ 'background-color': '#8b307a' });
      break;
    case '秋':
      $("#color1").css({ 'background-color': '#db7c29' });
      $("#color2").css({ 'background-color': '#498d37' });
      $("#color3").css({ 'background-color': '#e8ca2d' });
      $("#color4").css({ 'background-color': '#c7302b' });
      $("#color5").css({ 'background-color': '#43a6a0' });
      $("#color6").css({ 'background-color': '#e2983e' });
      $("#color7").css({ 'background-color': '#d7674c' });
      $("#color8").css({ 'background-color': '#c7a564' });
      break;
    case '冬':
      $("#color1").css({ 'background-color': '#1797cf' });
      $("#color2").css({ 'background-color': '#898989' });
      $("#color3").css({ 'background-color': '#d31176' });
      $("#color4").css({ 'background-color': '#118b42' });
      $("#color5").css({ 'background-color': '#e9e683' });
      $("#color6").css({ 'background-color': '#dc6991' });
      $("#color7").css({ 'background-color': '#144493' });
      $("#color8").css({ 'background-color': '#a61e2c' });
      break;
  }
}