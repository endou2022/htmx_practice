# -*- coding: utf-8 -*-

#---------------------------------------------------------------------------
# 「表示」ルーチン
#---------------------------------------------------------------------------
from jinja2 import Environment, FileSystemLoader
from fastapi import APIRouter
from fastapi.responses import HTMLResponse
import mysql.connector as mydb
from prog import config

env_j2 = Environment(loader=FileSystemLoader('./templates'))

router = APIRouter(tags=['個別表示'])
# --------------------------------------------------
@router.get('/view_institution/{ID}')
def view_institution(ID:int):
	'''指定されたデータを送信する
	- ID : データの番号
	- return : 詳細データ HTML形式
	'''
	conn = mydb.connect(**config.database)
	cur = conn.cursor(dictionary=True)
	sql = ("SELECT * FROM `sightseeing` WHERE ID = %s ")
	cur.execute(sql , (ID,))
	institution = cur.fetchone()
	if cur.rowcount == 0:
		institution = {"名称":"データがありません" , "名称_カナ":"" , "住所":"" , "説明":"" , "URL":"" , "備考":""}
	cur.close()
	conn.close()

	# <dialog>の中身作成
	template = env_j2.get_template('html01.j2')
	content = template.render(institution=institution)

	# データを返す
	return HTMLResponse(content=content)
# --------------------------------------------------
