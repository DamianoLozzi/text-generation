from datetime import datetime
import languagemodels as lm
from typing import Literal
from threading import Lock
import re

SUMMARIZE_PROMPT = "Summarize the following text:"
GENERATE_TITLE_PROMPT = "Generate a short title for this text:"

class TextGen:
    def __init__(self, device : str = "512MB"):
        self.lm = lm
        self.lm.config["max_ram"] = device
        self.lock= Lock()
        
    async def summarize(self, text : str):
        try:
            with self.lock:
                return self.lm.do(f"{SUMMARIZE_PROMPT} {text}")
        except Exception as e:
            raise RuntimeError(f"Error summarizing text: {e}")
    
    async def generate_name(self,text : str, type: Literal['filename','title']) -> str:
        try:
            with self.lock:
                name = lm.do(f"{GENERATE_TITLE_PROMPT} {text}")
            name : str = re.sub(r"[^ a-zA-Z0-9]+",'',name).strip()
            if type == 'filename':
                name :str =name.replace(" ", "_").lower() + "_" + str(datetime.now().strftime("%Y%m%d%H%M%S"))
                
            return name
        except Exception as e:
            raise RuntimeError(f"Error generating name: {e}")
            
    async def generate_summary(self,text :str) -> str:
        try:
            with self.lock:
                summary = lm.do(f"generate a summary for this text: {text}")
            return summary
        except Exception as e:
            raise RuntimeError(f"Error generating summary: {e}")
        
    async def ask_boolean(self,text : str) -> bool:
        try:
            with self.lock:
                response :str = lm.do(f"Do: {text}", choices=["True", "False"])
            return response == "True"
        except Exception as e:
            raise RuntimeError(f"Error asking boolean: {e}")