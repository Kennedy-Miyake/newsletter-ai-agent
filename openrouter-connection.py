import os
from typing import Optional
from dotenv import load_dotenv
from pydantic import (Field, SecretStr)
from langchain import hub
from langchain_core.utils.utils import secret_from_env
from langchain_openai import ChatOpenAI

load_dotenv()

class OpenRouter(ChatOpenAI):
    openai_api_key: Optional[SecretStr] = Field(
        alias="api_key",
        default_factory=secret_from_env("OPENROUTER_API_KEY", default=None)
    )

    @property
    def lc_secrets(self) -> dict[str, str]:
        return {"openai_api_key": "OPENROUTER_API_KEY"}