import logging

def test_loggingDemo():
    #This is To Get The file name
    logger=logging.getLogger(__name__)

    #This is to save the log file
    fileHandler=logging.FileHandler('logfile.log')
    #This is to print the log in one formate
    formatter=logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    #This is to set the formatter in file handler
    fileHandler.setFormatter(formatter)
    #This is to set the file handler and information to the logger
    logger.addHandler(fileHandler)

    #First of all Note the level of logging
      #debug
      #info
      #warning
      #error
      #critical

    logger.setLevel(logging.INFO)
    #If you set from info then only Info,Warning,Error and critical will be printed not Debug

    logger.debug("This is For Debug")
    logger.info("This is For Info")
    logger.warning("This is For Warning")
    logger.error("This is For Error")
    logger.critical("This is For Critical")

