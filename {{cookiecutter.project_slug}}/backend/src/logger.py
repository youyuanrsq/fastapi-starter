from loguru import logger

logger.add("/logs/runtime.log", rotation="500 MB", retention="10 days", level="INFO")

__all__ = ["logger"]
