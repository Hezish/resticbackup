from datetime import datetime
import os
import sys
from dotenv import load_dotenv
import restic
from utils.logging_module import Logger
from utils import telegram_msg
from utils.myip import get_local_ip_address
from utils.verify_ssh import check_ssh_responsive

# Load environment variables
load_dotenv('/Users/hezi.shviro/MyHome/.env')

# Setup script directory and module path
script_dir = os.path.dirname(os.path.abspath(__file__))
module_dir = os.path.join(script_dir, "utils")
sys.path.append(module_dir)

# Get environment variables
os.getenv('RESTIC_PASSWORD')

# Setup logging
file_path = "/tmp/logs"
file_name = datetime.now().strftime('restic_%H_%M_%d_%m_%Y.log')
logger_instance = Logger(__name__, file_path=file_path, file_name=file_name)
logger = logger_instance.get_logger()

logger.info('============================== Start ============================================')
logger.info(f'log file name:  {file_path}/{file_name}')
logger.info(f'local ip address:  {get_local_ip_address()}')


def create_backup(paths: list, exclude_patterns: list, snpapshot: bool = False):
    """Create backup with specified paths and exclude patterns."""
    logger.info('===============================  Creating backup ===============================')
    logger.info(f'Creating backup {paths} to {restic.repository}, excluding {exclude_patterns}')
    logger.info(restic.backup(paths=paths, exclude_patterns=exclude_patterns))
    if snpapshot:
        snapshot_maintenance(5, prune=True)


def snapshot_maintenance(keep_last: int = 5, prune: bool = True):
    """Perform snapshot maintenance operations."""
    logger.info('===============================  Getting snapshots ===============================')
    logger.debug(restic.snapshots())
    logger.info('===============================  snapshots maintenance after backup ===============================')
    logger.info(f'keeping last {keep_last} snapshots')
    restic.forget(keep_last=keep_last, prune=prune)


def show_stats():
"~/MyWork/g_sync/Scripts/restictest.py" [noeol] 73L, 3360B
from datetime import datetime
import os
import sys
from dotenv import load_dotenv
import restic
from utils.logging_module import Logger
from utils import telegram_msg
from utils.myip import get_local_ip_address
from utils.verify_ssh import check_ssh_responsive

# Load environment variables
load_dotenv('/Users/hezi.shviro/MyHome/.env')

# Setup script directory and module path
script_dir = os.path.dirname(os.path.abspath(__file__))
module_dir = os.path.join(script_dir, "utils")
sys.path.append(module_dir)

# Get environment variables
os.getenv('RESTIC_PASSWORD')

# Setup logging
file_path = "/tmp/logs"
file_name = datetime.now().strftime('restic_%H_%M_%d_%m_%Y.log')
logger_instance = Logger(__name__, file_path=file_path, file_name=file_name)
logger = logger_instance.get_logger()

logger.info('============================== Start ============================================')
logger.info(f'log file name:  {file_path}/{file_name}')
logger.info(f'local ip address:  {get_local_ip_address()}')


def create_backup(paths: list, exclude_patterns: list, snpapshot: bool = False):
    """Create backup with specified paths and exclude patterns."""
    logger.info('===============================  Creating backup ===============================')
    logger.info(f'Creating backup {paths} to {restic.repository}, excluding {exclude_patterns}')
    logger.info(restic.backup(paths=paths, exclude_patterns=exclude_patterns))
    if snpapshot:
        snapshot_maintenance(5, prune=True)


def snapshot_maintenance(keep_last: int = 5, prune: bool = True):
    """Perform snapshot maintenance operations."""
    logger.info('===============================  Getting snapshots ===============================')
    logger.debug(restic.snapshots())
    logger.info('===============================  snapshots maintenance after backup ===============================')
    logger.info(f'keeping last {keep_last} snapshots')
    restic.forget(keep_last=keep_last, prune=prune)

