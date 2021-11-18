from fastapi                 import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers             import teams, users, auth

api = FastAPI()
# uvicorn src.server:app --reload --reload-dir=src

# CORS
origins = [
    'http://127.0.0.1:8000',
]

api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Route Teams
api.include_router(teams.router)
# Route Users
api.include_router(users.router)
# Route Auth
api.include_router(auth.router)


