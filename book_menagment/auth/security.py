from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import APIKeyHeader
from dotenv import load_dotenv
import os

load_dotenv()
API_KEYS = os.getenv("API_KEYS")
API_KEYS_NAME = "api-key"
api_key_header = APIKeyHeader(name=API_KEYS_NAME, auto_error=False) 

def get_api_key(api_key: str = Depends(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail = "invalid API Key"
        )
    return api_key