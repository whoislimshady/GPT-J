from fastapi import FastAPI
from typing import Optional
app = FastAPI()



@app.get('/genrate') 
def index(context,
          token_max_length: Optional[int] = 50,
          temperature: Optional[float] = 1.0,
          top_p: Optional[float] = 0.9,
          stop_sequence: Optional[str] = None,):
    
    return context

  