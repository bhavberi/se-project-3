from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
from os import getenv
import users_router

DEBUG = getenv("BACKEND_DEBUG", "False").lower() in ("true", "1", "t")
SESSION_SECRET_KEY = getenv("SESSION_SECRET_KEY", "this_is_my_very_secretive_secret")

# Create a new FastAPI instance
# FastAPI App
if DEBUG:
    app = FastAPI(
        debug=DEBUG,
        title="User Management",
        description="User Management Backend for SE Project 3 for the Team 12",
        root_path="/api/applications"
    )
else:
    app = FastAPI(
        debug=DEBUG,
        title="User Management",
        description="User Management Backend for SE Project 3 for the Team 12",
        docs_url=None,
        redoc_url=None,
        root_path="/api/applications"
    )

# Backend Index Page - For checking purposes
@app.get("/ping", tags=["General"])
async def index():
    return {"message": "Backend Running!!"}

# Add Session Middleware
app.add_middleware(SessionMiddleware, secret_key=SESSION_SECRET_KEY)

# Mount the user router on the "/user" path
app.include_router(users_router.router, tags=["User"])
