from apistar import typesystem


class UserSchemas(typesystem.Object):

    properties = {
        "id": typesystem.integer(default=None),
        "username": typesystem.string(max_length=32, required=False)
    }