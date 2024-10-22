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

router = APIRouter(tags=['一覧表示'])
# --------------------------------------------------
@router.get('/')
def root_function():
	'''ルート関数。データの一覧表を出力する
	'''
	conn = mydb.connect(**config.database)
	cur = conn.cursor(dictionary=True)
	sql = ("SELECT * FROM `sightseeing` ORDER BY `名称_カナ` ")
	cur.execute(sql)
	institutions = cur.fetchall()
	cur.close()
	conn.close()

	# テンプレートに入れる 引数が多くなったので、テンプレートをいくつかに分けた
	# <head> 作成
	template = env_j2.get_template('html90.j2')
	head = template.render(description=config.__description__ , page_title="観光施設案内")

	# <main>作成
	template = env_j2.get_template('html00.j2')
	main = template.render(table_caption='観光施設一覧' , institutions=institutions)

	# <footer>作成
	template = env_j2.get_template('html99.j2')
	footer = template.render(footer_str=config.footer_str)

	# データを返す
	return HTMLResponse(content=head + main + footer + "\n</body>\n</html>\n")
# --------------------------------------------------
@router.get('/reload_institution')
def reload_institution():
	'''データを再表示する。

	最下行(追加ボタンの上)にデータが追加されるので、ソートして表示し直す。

	<body>の中身だけ出力
	'''
	conn = mydb.connect(**config.database)
	cur = conn.cursor(dictionary=True)
	sql = ("SELECT * FROM `sightseeing` ORDER BY `名称_カナ` ")
	cur.execute(sql)
	institutions = cur.fetchall()
	cur.close()
	conn.close()

	template = env_j2.get_template('html00.j2')
	main = template.render(table_caption='観光施設一覧' , institutions=institutions)
	template = env_j2.get_template('html99.j2')
	footer = template.render(footer_str=config.footer_str)

	return HTMLResponse(content=main + footer)
# --------------------------------------------------
