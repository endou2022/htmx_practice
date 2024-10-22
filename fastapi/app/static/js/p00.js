//---------------------------------------------------------------------------
//htmxの練習
//---------------------------------------------------------------------------
/**
 * Ajaxの戻り値を判断して１行を書き換える
 */
function change_institution(event) {
	close_dialog();
	if (event.detail.xhr.status == 200) {
		// 成功時の処理
		responseText = event.detail.xhr.responseText;
		if (responseText == 'データを削除しました') {
			return;
		}
		if (!responseText.includes('<tr')) {	// 応答に<trを含んでいなければ行を変更しない＝エラーなので、preventDefault()で処理を中止する
			alert(responseText);
			console.table(event.detail.xhr);
			event.preventDefault();
		}
	} else {
		// 失敗時の処理
		alert("サーバーとの通信に失敗しました");
		console.table(event.detail.xhr);
		event.preventDefault();
	}
}
//---------------------------------------------------------------------------
/**
 * 詳細ダイアローグボックスを開く
 */
function show_dialog() {
	htmx.find("#detail").showModal();
	//	document.getElementById("detail").showModal();
}
//---------------------------------------------------------------------------
/**
 * 詳細ダイアローグボックスを閉じる
 */
function close_dialog() {
	htmx.find("#detail").close();
}
//---------------------------------------------------------------------------
