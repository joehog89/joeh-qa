from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, HTTPException
from sqlmodel import Session, select

from app.database import add_sample_products, create_database, get_session
from app.models import Product

import logging
from app.logging_config import configure_logging

configure_logging()
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_database()
    add_sample_products()
    yield


app = FastAPI(
    title="Joe's Demo PIM API",
    version="1.0",
    lifespan=lifespan,
)


@app.get("/")
def home():
    return {"message": "PIM API is running"}


@app.get("/products", response_model=list[Product])
def get_products(session: Session = Depends(get_session)):
    products = session.exec(select(Product)).all()
    return products


@app.get("/products/{product_id}", response_model=Product)
def get_product_by_id(
    product_id: int,
    session: Session = Depends(get_session),
):
    product = session.get(Product, product_id)

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found",
        )

    return product


@app.post("/products", response_model=Product, status_code=201)
def add_product(
    product: Product,
    session: Session = Depends(get_session),
):
    
    existing_product = session.exec(
        select(Product).where(Product.sku == product.sku)
    ).first()

    if existing_product:
        raise HTTPException(
            status_code=409,
            detail="A product with this SKU already exists",
        )

    product.id = None

    session.add(product)
    session.commit()
    session.refresh(product)

    return product