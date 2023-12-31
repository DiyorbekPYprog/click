from typing import Union

import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool


from data import config

class Database:

    def __init__(self):
        self.pool: Union[Pool,None]=None

    async def create(self):
        self.pool= await asyncpg.create_pool(
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            database=config.DB_NAME
            )
    async def execute(self,command, *args,
                      fetch: bool=False,
                      fetchval: bool=False,
                      fetchrow: bool=False,
                      execute: bool=False
                      ):
        async with self.pool.acquire()as connection:
            connection:Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command,*args)
                elif fetchval:
                    result = await connection.fetchval(command,*args)
                elif execute:
                    result = await connection.execute(command,*args)
            return result
        
    async def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users (
        id SERIAL PRIMARY KEY,
        full_name VARCHAR(255) NOT NULL,
        username VARCHAR(255) NULL,
        telegram_id BIGINT NOT NULL UNIQUE
        );
        """
        await self.execute(sql, execute=True)

    @staticmethod
    def format_args(sql, parametrs: dict):
        sql += "AND ".join([
            f"{item} = ${num}" for num, item in enumerate(parametrs.keys(),
                                                          start=1)
        ])
        return sql,tuple(parametrs.values())
    async def add_user(self,full_name,username,telegram_id):
        sql = "INSERT INTO users (full_name,username,telegram_id) VALUES($1, $2, $3 )returning *"
        return await self.execute(sql, fetch=True)