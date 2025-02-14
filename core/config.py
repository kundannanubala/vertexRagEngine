from pydantic_settings import BaseSettings
import os
from pathlib import Path
from typing import ClassVar

class Settings(BaseSettings):
    # Root directory of the project
    ROOT_DIR: ClassVar[Path] = Path(__file__).parent.parent

    # Path to the application credentials file
    GOOGLE_APPLICATION_CREDENTIALS:str = str(ROOT_DIR / "ragEnginecreds.json")
    GOOGLE_CLOUD_PROJECT: str = os.getenv("GOOGLE_CLOUD_PROJECT","")
    GOOGLE_CLOUD_REGION: str = os.getenv("GOOGLE_CLOUD_REGION","")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set the environment variable for the application credentials
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = self.GOOGLE_APPLICATION_CREDENTIALS
    

    class Config:
        env_file = ".env"
        
settings = Settings()
