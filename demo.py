from fastapi import FastAPI,Depends,Header,HTTPException,APIRouter
from fastapi.param_functions import Body
from starlette.requests import Request
from starlette.templating import Jinja2Templates
from starlette import status
import uvicorn
from deta import Deta
from fastapi.responses import StreamingResponse
from fastapi.responses import JSONResponse

# 实例化路由器
router = APIRouter()
templates = Jinja2Templates('templates')

# 注意，视图这里使用router来声明请求方式&UR@router.get('/info')
def user_list():
    # vue的响应数据
    items = [
        {'id':'1','name':'phyger'},
        {'id':'2','name':'fly'},
        {'id':'3','name':'enheng'},
        ]
    return JSONResponse(content=items)

@router.get('/')
def welcome():
    return "这里是测试路由"

'''
实际上，这里的home.html也是需要前端服务去向用户渲染的，
但是我们为了方便演示，未启动前端服务器，直接将前端代码写在了home.html中，
实际上，当用户请求/check的时候，前端代码会去请求/info接口获取数据，
从而实现前端页面的数据渲染。
'''

@router.get('/check')
def home(request:Request):
    return templates.TemplateResponse(name='home.html',context={'request':request,})
