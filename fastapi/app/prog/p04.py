# -*- coding: utf-8 -*-

#---------------------------------------------------------------------------
# 「新規」ルーチン
#---------------------------------------------------------------------------
from jinja2 import Environment, FileSystemLoader
from fastapi import APIRouter , Form
from fastapi.responses import HTMLResponse
import mysql.connector as mydb
from prog import config

env_j2 = Environment(loader=FileSystemLoader('./templates'))

router = APIRouter(tags=['新規'])
# --------------------------------------------------
@router.get('/new_institution')
def new_institution():
	'''新規入力フォームを作って送信する
	- return : 新規入力フォーム HTML形式
	'''
	# <dialog>の中身作成
	template = env_j2.get_template('html04.j2')
	content = template.render()

	# データを返す
	return HTMLResponse(content=content)
# --------------------------------------------------
@router.post('/add_institution')
def add_institution(ID:int=Form() , name:str=Form() , kana:str=Form() , addr:str=Form() , exp:str=Form(None) , url:str=Form(None) , note:str=Form(None) ):
	'''入力されたデータを追加する
	- ID : -1
	- name : 名称
	- kana : ヨミガナ
	- addr : 住所
	- exp : 説明
	- url : URL
	- note : 備考
	- return : 実行結果
	'''
	conn = mydb.connect(**config.database)
	cur = conn.cursor(dictionary=True)
	sql = ("INSERT INTO `sightseeing` "
		   "(`名称` , `名称_カナ` , `住所` , `説明` , `URL` , `備考`) VALUES "
		   "(%s     , %s          , %s     , %s     , %s    , %s    ) ")
	param = (name   , kana        , addr   , exp    , url   , note)
	try:
		cur.execute(sql , param)
		if cur.rowcount == 1:
			# 追加したデータを返す
			ID = cur.lastrowid
			sql = ("SELECT * FROM `sightseeing` WHERE ID = %s ")
			cur.execute(sql , (ID,))
			institution = cur.fetchone()
			template = env_j2.get_template('html00-2.j2')
			ret = template.render(institution=institution)
		else:
			ret = "データを追加できませんでした。"
	except Exception as e:
		ret = "予期しないエラー：" + str(e) + '  が起きました。'
	finally:
		cur.close()
		conn.close()

	return HTMLResponse(ret)
# --------------------------------------------------
