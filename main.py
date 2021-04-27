from fastapi import FastAPI, Depends
import uvicorn
import models
from database import SessionLocal, engine
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(engine)


def get_db():
	try:
		db = SessionLocal()
		yield db
	finally:
		db.close()


# wyswietl stan magazynu
@app.get("/warehouse")
def showResults(db: Session = Depends(get_db)):
	return db.query(models.Magazyn).offset(0).all()


# usun z magazynu
@app.delete("/removeFromWarehouse")
def removeFromWarehouse(product_id: int, db: Session = Depends(get_db)):
	db.query(models.Magazyn).filter(models.Magazyn.id == product_id).delete()
	db.commit()


# dodaj do magazynu
@app.post("/Warehouse")
def addToWarehouse(id: int, name: str, amount: int, db: Session = Depends(get_db)):
	product = models.Magazyn()
	product.id = id
	product.name = name
	product.amount = amount

	db.add(product)
	db.commit()
	return "Product added"


if __name__ == "__main__":
	uvicorn.run("main:app", host="127.0.0.1", port=8000, log_level="debug", reload=True)
