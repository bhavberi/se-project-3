from fastapi import FastAPI
from os import getenv
import listings_router

DEBUG = getenv("BACKEND_DEBUG", "False").lower() in ("true", "1", "t")

# Create a new FastAPI instance
# FastAPI App
if DEBUG:
    app = FastAPI(
        debug=DEBUG,
        title="Listing Management",
        description="Listing Management Backend for SE Project 3 for the Team 12",
        root_path="/api/listings"
    )
else:
    app = FastAPI(
        debug=DEBUG,
        title="Listing Management",
        description="Listing Management Backend for SE Project 3 for the Team 12",
        docs_url=None,
        redoc_url=None,
        root_path="/api/listings"
    )

# Backend Index Page - For checking purposes
@app.get("/ping", tags=["General"])
async def index():
    return {"message": "Backend Running!!"}

# Mount the application router on the "/application" path
app.include_router(listings_router.router, tags=["Listings"])
