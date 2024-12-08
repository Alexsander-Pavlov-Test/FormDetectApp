from typing import TypeAlias
from bson.objectid import ObjectId


MongoType: TypeAlias = dict[str, str | ObjectId]
