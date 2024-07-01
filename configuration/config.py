from pydantic import BaseSettings
from datetime import date
import os

class FacultySettings(BaseSettings):

    application:str='Faculty Management System'
    webmaster:str='test@university.com'
    created:date='2024-06-29'

class LibrarySettings(BaseSettings):
    application:str='library Management System'
    webmaster:str='test@university.com'
    created:date='2024-06-29'

class StudentSettings(BaseSettings):
    application:str='Student Management System'
    webmaster:str='test@university.com'
    created:date='2024-06-29'


class ServerSettings(BaseSettings):
    production_server:str
    prod_port:int
    development:int
    dev_port:int

    class Config:

        env_file=os.getcwd()+'/configuration/erp_settings.properties'