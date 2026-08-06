from fastapi import HTTPException

from app.models.user import User

from app.security.hashing import hash_password

from app.repositories.user_repository import (

    create_user,

    get_user_by_email,

    get_user_by_username

)


def register_user(

    db,

    data

):

    existing_email = get_user_by_email(

        db,

        data.email

    )

    if existing_email:

        raise HTTPException(

            status_code=400,

            detail="Email already exists"

        )

    existing_username = get_user_by_username(

        db,

        data.username

    )

    if existing_username:

        raise HTTPException(

            status_code=400,

            detail="Username already exists"

        )

    user = User(

        username=data.username,

        email=data.email,

        password=hash_password(

            data.password

        )

    )

    return create_user(

        db,

        user

    )