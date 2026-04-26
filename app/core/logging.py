from loguru import logger 

def setup_logging(): 
    logger.add("logs/app.log", rotation="1 week", retention="1 month", compression="zip")
