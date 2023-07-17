from main import ma


class WatchlistSchema(ma.Schema):
    class Meta:
        # Orders the fields in the way they are defined in the schema when serialising or deserialising 
        ordered = True
        # Fields that will be included during serealisation
        fields = [
            'id',
            'date_added',
        ]

# Singular watchlist schema instance for retreiving a single watchlist
watchlist_schema = WatchlistSchema()
# COMMENTED OUT BECAUSE TECHNICALLY A USER ONLY HAS ONE WATCHLIST
# WILL DELETE IN THE FUTURE, KEEPING IT JUST IN CASE
# # Multiple watchlists schema instance for retreiving multiple watchlists
# watchlists_schema = WatchlistSchema(many=True)