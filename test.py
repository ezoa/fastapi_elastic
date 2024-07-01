

import sys
from loguru import logger

# logger.debug("Happy logging with Loguru!")



# logger.trace("A trace message.")
# logger.debug("A debug message.")
# logger.info("An info message.")
# logger.success("A success message.")
# logger.warning("A warning message.")
# logger.error("An error message.")
# logger.critical("A critical message.")

# logger.remove(0)

logger.add(sys.stderr, level="INFO")
logger.level("FATAL", no=60, color="<red>", icon="!!!")

logger.log("FATAL", "A user updated some information.")

