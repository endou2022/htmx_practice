# -*- coding: utf-8 -*-

#---------------------------------------------------------------------------
# 「削除」ルーチン
#---------------------------------------------------------------------------
from fastapi import APIRouter
from fastapi.responses import PlainTextResponse
import mysql.connector as mydb
from prog import config

router = APIRouter(tags=['削除'])
# --------------------------------------------------
@router.delete('/del_institution/{ID}/{version}')
def del_institution(ID:int , version:int):
	'''指定されたデータを削除する
	- ID : データの番号
	- version : 更新回数
	- return : 処理結果
	'''
	conn = mydb.connect(**config.database)
	cur = conn.cursor(dictionary=True)
	sql = ("DELETE FROM `sightseeing` WHERE (ID = %s ) AND (`更新回数` = %s) ")
	cur.execute(sql , (ID , version))
	if cur.rowcount != 1:
		ret = "データを削除しませんでした。別のＰＣで変更されている可能性があります。"
	else:
		ret = "データを削除しました"

	cur.close()
	conn.close()

	return PlainTextResponse(ret)
# --------------------------------------------------
