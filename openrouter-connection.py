import os
from typing import Optional
from dotenv import load_dotenv
from pydantic import (Field, SecretStr)
from langchain import hub
from langchain_core.utils.utils import secret_from_env
from langchain_openai import ChatOpenAI