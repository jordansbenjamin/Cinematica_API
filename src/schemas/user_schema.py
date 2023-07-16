from main import ma


class UserSchema(ma.Schema):
    class Meta:
        # Orders the fields in the way they are defined in the schema when serialising or deserialising 
        ordered = True
        # Fields that will be included during serealisation
        fields = [
            'id',
            'email',
            'username',
            'password',
            'join_date'
        ]

# Singular user schema instance for retreiving a single user
user_schema = UserSchema()
# Multiple users schema instance for retreiving multiple users
users_schema = UserSchema(many=True)