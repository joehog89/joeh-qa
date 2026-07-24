import logging

from sqlmodel import Session, SQLModel, create_engine

from app.models import Product


logger = logging.getLogger(__name__)

database_url = "sqlite:///pim.db"

engine = create_engine(
    database_url,
    connect_args={"check_same_thread": False},
)


def create_database():
    SQLModel.metadata.create_all(engine)
    logger.info("Database created or checked successfully")


def get_session():
    with Session(engine) as session:
        yield session


def add_sample_products():
    with Session(engine) as session:
        existing_product = session.get(Product, 1)

        if existing_product is not None:
            logger.info("Sample products already exist")
            return

        products = [
            Product(
                sku="PPE-GLOVE-001",
                name="Cut Resistant Safety Gloves",
                price=8.99,
                stock=120,
            ),
            Product(
                sku="PPE-BOOT-001",
                name="Steel Toe Safety Boots",
                price=54.99,
                stock=45,
            ),
            Product(
                sku="PPE-VEST-001",
                name="High Visibility Safety Vest",
                price=7.49,
                stock=80,
            ),
        ]

        session.add_all(products)
        session.commit()

        logger.info("Added %s sample products", len(products))