from aiogram import Dispatcher
from . import ChatDetection, Language

def register_middleware(dp: Dispatcher):
    dp.setup_middleware(Language.Middleware())
    dp.setup_middleware(ChatDetection.Middleware())