import environ

env = environ.Env()
# APP_CONFIG_PATH = env("APP_CONFIG_PATH", default="./configs/local.env")
# env.read_env(APP_CONFIG_PATH)

TELEGRAM_CHANNEL_TOKEN = env("TELEGRAM_CHANNEL_TOKEN")
