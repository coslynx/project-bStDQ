import os

# Discord Bot Settings
TOKEN = os.getenv('DISCORD_TOKEN')
PREFIX = '!'
MODERATOR_ROLE = 'Moderator'
ADMIN_ROLE = 'Admin'

# Dashboard Settings
DASHBOARD_URL = 'http://localhost:5000/dashboard'
DASHBOARD_PORT = 5000
SECRET_KEY = os.getenv('SECRET_KEY')

# Webhook Settings
WEBHOOK_URL = 'https://discord.com/api/webhooks/1234567890/ABCDEFGHIJKLMN'
WEBHOOK_CHANNEL = 'webhook-channel'
WEBHOOK_USERNAME = 'Bot Webhook'

# Database Settings
DATABASE_NAME = 'discord_bot_db'
DATABASE_USER = 'admin'
DATABASE_PASSWORD = 'password'
DATABASE_HOST = 'localhost'
DATABASE_PORT = 5432

# API Settings
DISCORD_API_BASE_URL = 'https://discord.com/api/v8'
DISCORD_API_TOKEN = os.getenv('DISCORD_API_TOKEN')

# Logging Settings
LOG_FILE = 'discord_bot.log'
LOG_LEVEL = 'INFO'
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

# Ticketing System Settings
TICKET_CATEGORY = 'Tickets'
TICKET_SUPPORT_CHANNEL = 'support'
TICKET_CLOSED_CHANNEL = 'closed-tickets'
TICKET_LOG_CHANNEL = 'ticket-logs'

# Automated Moderation Settings
ANTI_SPAM_THRESHOLD = 5
ANTI_RAID_THRESHOLD = 10
PROFANITY_LIST = ['profanity1', 'profanity2', 'profanity3']

# AI Settings
AI_ENABLED = True
AI_MODULE = 'content_filtering'
AI_THRESHOLD = 0.8

# Reporting System Settings
REPORT_CHANNEL = 'reports'
REPORT_COMMAND = '!report'

# User Behavior Analysis Settings
BEHAVIOR_MODULE = 'user_behavior_analysis'
BEHAVIOR_THRESHOLD = 0.7

# Other Settings
MAX_MESSAGE_LENGTH = 2000
RETRY_INTERVAL = 5
MAX_RETRIES = 3