# -*- coding: utf-8 -*-

#---------------------------------------------------------------------------
# メインルーチン
#---------------------------------------------------------------------------
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from prog import p00 , p01 , p02 , p03 , p04
from prog import config

# --------------------------------------------------
# https://fastapi.tiangolo.com/ja/tutorial/metadata/ (2024/10/01)
app = FastAPI(title = config.__soft_name__ ,
			  description = f"<h1>{config.__description__}</h1>" ,
			  version = config.__version__ ,
			  license_info = {"name": "BSD"})

app.mount(path="/static", app=StaticFiles(directory="static"), name="static")
app.include_router(p00.router)
app.include_router(p01.router)
app.include_router(p02.router)
app.include_router(p03.router)
app.include_router(p04.router)
# --------------------------------------------------
