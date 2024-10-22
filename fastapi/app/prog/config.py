# -*- coding: utf-8 -*-

#---------------------------------------------------------------------------
# 定数 (python に定数という概念はないが)
#---------------------------------------------------------------------------
__soft_name__   = 'practice'
__version__     = '1.0'
__description__ = 'htmxの練習'
__copyright__   = '(C)Copyright 2024 Y.Endou All rights reserved.'
software        = f"{__soft_name__} {__version__}"
footer_str      = f"{__soft_name__} {__version__} : {__description__} {__copyright__}"
#---------------------------------------------------------------------------
# データベースへの接続パラメータ
# conn = mydb.connect(**config.database) として使う
# STRICT_TRANS_TABLES(厳密モード)をはずして、超過文字を入力したときにエラーを出さない（超過分切り捨て）ようにしている
database = {"host" : 'mariadb' ,	# データベースのアドレス dockerなので、IPアドレスではない
			"port" : '3306' ,
			"user" : 'practice' ,
			"password" : 'practice' ,
			"database" : 'practice',
			"sql_mode" : 'ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION' ,
			"charset" : 'utf8mb4' ,
			"collation" : 'utf8mb4_unicode_ci'}
#---------------------------------------------------------------------------
