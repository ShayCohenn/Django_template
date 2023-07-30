import os
import logging
from datetime import datetime

class RequestLoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

        # Configure the logging settings
        self.configure_logging()

    def configure_logging(self):
        # Create a logger instance
        logger = logging.getLogger("request_logger")
        logger.setLevel(logging.DEBUG)

        # Define the log file path
        log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "request_log.log")

        # Create a file handler for the log file
        file_handler = logging.FileHandler(log_file_path)

        # Create a formatter without color
        log_formatter = logging.Formatter(
            "%(asctime)s %(levelname)-8s %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        # Set the formatter for the file handler
        file_handler.setFormatter(log_formatter)

        # Add the file handler to the logger
        logger.addHandler(file_handler)

        # Save the logger in the instance
        self.logger = logger

    def __call__(self, request):
        # Log the request details
        log_data = {
            'Method': request.method,
            'Path': request.path,
            'Time': datetime.now().isoformat(),  # Get the current timestamp
            'IP Address': request.META['REMOTE_ADDR'],  # Include the IP address
        }

        # Log the request details using the configured logger
        self.logger.info("Request Details: %s", log_data)

        # Call the next middleware or view
        response = self.get_response(request)

        return response
