import sys
from networksecurity.logger.logger import logger

class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_details:sys):
        self.error_message = error_message
        _,_,exc_tb = error_details.exc_info()

        self.lineno = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return (
            f"Error occured in python script [{self.file_name}] " \
            f"line number [{self.self.lineno}] error message [{self.error_message}])"
        )

if __name__ == "__main__":
    try:
        logger.info("Entered the try block..")
        a = 1/0
        print("This will not be printed.")
    except Exception as e:
        logger.error(f"Exception occurred: {str(e)}")
        raise NetworkSecurityException(e, sys)
