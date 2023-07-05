from cli_processor import get_cli_args
from config_processor import get_cfg_args


cli_args = get_cli_args()

cfg_args = get_cfg_args(cli_args.configpath)
