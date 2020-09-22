//アップロードした画像の表示
document.getElementById('file-sample').addEventListener('change', function (e) {
  // 1枚だけ表示する
  var file = e.target.files[0];

  // ファイルのブラウザ上でのURLを取得する
  var blobUrl = window.URL.createObjectURL(file);

  // img要素に表示
  var img = document.getElementById('file-preview');
  img.src = blobUrl;
});

// loading機能
$(".btn").click(function () {
  //submitを拾う
  $("form").submit(function () {
    //0.1秒後にsubmitを実行
    setTimeout(function () {
      $("form").off("submit");
      $("form").submit();
    }, 100);
    $("#overlay").fadeIn(500);
    //submitをキャンセル
    return false;
  });
});