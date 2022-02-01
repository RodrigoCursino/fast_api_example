from fastapi                 import FastAPI, Request
from fastapi.templating      import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from src.routers             import teams, users, auth
from fastapi.staticfiles     import StaticFiles

api = FastAPI()
# uvicorn src.app:api --reload --reload-dir=src

# CORS
origins = [
    'http://127.0.0.1:8000',
    'http://localhost:8080'
]

api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# arquivos estáticos gerados pelo build
api.mount("/js/", StaticFiles(directory="src/static/js"))
api.mount("/css/", StaticFiles(directory="src/static/css"))
api.mount("/img/", StaticFiles(directory="src/static/img"))   
api.mount("/fonts/", StaticFiles(directory="src/static/fonts"))  
# arquivos estáticos gerados pelo build

# index build files
templates = Jinja2Templates(directory="src/templates") 

# Route Teams
api.include_router(teams.router)
# Route Users
api.include_router(users.router)
# Route Auth
api.include_router(auth.router)

@api.get("/")
async def serve_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


