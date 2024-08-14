from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from app import models, schemas, database
from app.database import get_db
from app.utils import generate_short_code


app = FastAPI()

@app.post("/shorten", response_model=schemas.URL)
def create_short_url(url: schemas.URLCreate, db: Session = Depends(get_db)):
    short_code = generate_short_code()
    db_url = models.URL(original_url=url.original_url, short_code=short_code)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url

@app.get("/{short_code}")
def redirect_to_url(short_code: str, db: Session = Depends(get_db)):
    db_url = db.query(models.URL).filter(models.URL.short_code == short_code).first()
    if db_url is None:
        raise HTTPException(status_code=404, detail="URL not found")
    return RedirectResponse(db_url.original_url)
