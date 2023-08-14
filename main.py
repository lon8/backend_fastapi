from fastapi import FastAPI
import uvicorn
from handlers import router
from dbfuncs import connect_db


# APP CREATE
def get_application() -> FastAPI:
    application = FastAPI()
    application.include_router(router)
    return application

app = get_application()

if __name__ == '__main__':
    connect_db(app)
    uvicorn.run(app, host='localhost', port=8000, log_level='info')