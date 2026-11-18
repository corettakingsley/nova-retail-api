
from sqlalchemy.orm import Session
from app.models.category import Category
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate


def get_products(db: Session):
    return db.query(Product).filter(
        Product.is_active == True
    ).all()


def get_product(db: Session, product_id: int):
    return db.query(Product).filter(
        Product.id == product_id,
        Product.is_active == True
    ).first()

def create_product(db: Session, product: ProductCreate):
    if product.category_id is not None:
        category = db.query(Category).filter(
            Category.id == product.category_id
        ).first()

        if category is None:
            raise ValueError("Category not found")

    db_product = Product(**product.model_dump())

    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return db_product

    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return db_product


def update_product(
    db: Session,
    product_id: int,
    product: ProductUpdate,
):
    db_product = get_product(db, product_id)

    if db_product is None:
        return None

    for key, value in product.model_dump().items():
        setattr(db_product, key, value)

    db.commit()
    db.refresh(db_product)

    return db_product


def delete_product(db: Session, product_id: int):
    db_product = get_product(db, product_id)

    if db_product is None:
        return None

    db_product.is_active = False

    db.commit()
    db.refresh(db_product)

    return db_product