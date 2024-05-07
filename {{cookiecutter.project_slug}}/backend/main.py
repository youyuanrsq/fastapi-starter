from src.logger import logger
from src.factory import create_app

app = create_app()

if __name__ == "__main__":
    import uvicorn

    logger.info("Starting uvicorn in reload mode")
    uvicorn.run(
        "main:src",
        host="0.0.0.0",
        reload=True,
        port=int("{{ cookiecutter.backend_port }}"),
    )
