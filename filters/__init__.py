from aiogram import Dispatcher
from .admin import AdminFilter
from loader import dp
from .lichka import IsPrivate
from .group import IsGroup
# from .is_admin import AdminFilter


if __name__ == "filters":
  dp.filters_factory.bind(AdminFilter)
  dp.filters_factory.bind(IsPrivate)
  dp.filters_factory.bind(IsGroup)
