# -*- coding: utf-8 -*-

#---------------------------------------------------------------------------
# 「編集」ルーチン
#---------------------------------------------------------------------------
from jinja2 import Environment, FileSystemLoader
from fastapi import APIRouter , Form
from fastapi.responses import HTMLResponse , PlainTextResponse
import mysql.connector as mydb
from prog import config

env_j2 = Environment(loader=FileSystemLoader('./templates'))

router = APIRouter(tags=['編集'])
# --------------------------------------------------
@router.get('/edit_institution/{ID}')
def edit_institution(ID:int):
	'''指定されたデータを、編集フォームを作って送信する
	- ID : データの番号
	- return : 詳細データ HTML形式
	'''
	conn = mydb.connect(**config.database)
	cur = conn.cursor(dictionary=True)
	sql = ("SELECT * FROM `sightseeing` WHERE ID = %s ")
	cur.execute(sql , (ID,))
	institution = cur.fetchone()
	if cur.rowcount == 0:
		institution = {"ID":-1 , "名称":"データがありません" , "名称_カナ":"" , "住所":"" , "説明":"" , "URL":"" , "備考":"" , "登録日":"" , "更新日時":"" , "更新回数":0}
	cur.close()
	conn.close()

	# <dialog>の中身作成
	template = env_j2.get_template('html02.j2')
	content = template.render(institution=institution)

	# データを返す
	return HTMLResponse(content=content)
# --------------------------------------------------
@router.put('/update_institution')
def update_institution(ID:int=Form() , name:str=Form() , kana:str=Form() , addr:str=Form() , exp:str=Form(None) , url:str=Form(None) , note:str=Form(None) , version:int=Form()):
	'''指定されたデータを更新する
	- ID : データの番号
	- name : 名称
	- kana : ヨミガナ
	- addr : 住所
	- exp : 説明
	- url : URL
	- note : 備考
	- version : 更新回数 排他制御(同時実行制御)（楽観ロック）
	- return : 更新した場合：行のデータ。更新しなかった場合：更新しない理由
	クライアント側で'<tr'が含まれているかどうかで、更新／不更新を判断する
	'''
	conn = mydb.connect(**config.database)
	cur = conn.cursor(dictionary=True)
	sql = ("UPDATE `sightseeing` SET "
		   "`名称` = %s , "
		   "`名称_カナ` = %s , "
		   "`住所` = %s , "
		   "`説明` = %s , "
		   "`URL` = %s , "
		   "`備考` = %s , "
		   "`更新回数` = `更新回数` + 1 "
		   "WHERE (`ID` = %s) AND (`更新回数` = %s) " )
	param = (name , kana , addr , exp , url , note , ID , version)
	cur.execute(sql , param)
	if cur.rowcount != 1:
		cur.close()
		conn.close()
		return PlainTextResponse("データを更新しませんでした。\n情報が変更されていないか、別のＰＣで変更されている可能性があります。")

	# 更新したデータを返す
	sql = ("SELECT * FROM `sightseeing` WHERE ID = %s ")
	cur.execute(sql , (ID,))
	institution = cur.fetchone()
	template = env_j2.get_template('html00-2.j2')
	content = template.render(institution=institution)
	cur.close()
	conn.close()

	return HTMLResponse(content)
# --------------------------------------------------
