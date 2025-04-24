from fastapi import FastAPI

from .api.comments_finder_routes.comment_finder_api import router as comment_routers
from .api.file_operations_routes.file_routes import router as file_routers
from .api.class_finder_routes.class_finder import router as class_routers
from .api.function_finder_routes.function_finder import router as function_routers
from .api.login_register_routes.login_api import router as login_routers
from .api.login_register_routes.register_api import router as register_routers
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(file_routers)
app.include_router(class_routers)
app.include_router(function_routers)
app.include_router(comment_routers)
app.include_router(login_routers)
app.include_router(register_routers)

@app.get("/")
async def root():
    return {"message": "Hello World"}
