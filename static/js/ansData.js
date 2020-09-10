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

        var parent = document.getElementById("ppResult");
        var p = document.createElement("p");
        p.innerHTML = data.makeData[i].summary;
        parent.appendChild(p);

      }
    }
  })
}

//顔の形のグラフ作成
var ctx = document.getElementById('pkChart').getContext('2d');
var chart = new Chart(ctx, {
  type: 'doughnut',
  data: {
    labels: ['丸', '面長', '逆三角', '四角', '卵'],
    datasets: [{
      backgroundColor: ['rgb(241,158,194)', 'rgb(255,231,63)', 'rgb(246,173,60)', 'rgb(135,202,178)', 'rgb(64,124,192)'],
      data: [pk1, pk2, pk3, pk4, pk5]

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
    labels: ['夏', '冬', '春', '秋'],
    datasets: [{
      backgroundColor: ['rgb(23,120,255)', 'rgb(80,186,0)', 'rgb(255,105,180)', 'rgb(255,143,23)'],
      data: [pp1, pp2, pp3, pp4]

    }]
  },
  options: {}
});