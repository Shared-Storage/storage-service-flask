import uuid
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from db import db
from models import LocationModel
from schemas import LocationSchema

blp = Blueprint("locations", __name__, description="Operation on locations")


@blp.route("/location/<string:location_id>")
class Location(MethodView):
    @blp.response(200, LocationSchema)
    def get(self, location_id):
        location = LocationModel.query.get_or_404(location_id)
        return location

    def delete(self, location_id):
        location = LocationModel.query.get_or_404(location_id)
        db.session.delete(location)
        db.session.commit()
        return {"message": "Location deleted."}


@blp.route("/location")
class LocationList(MethodView):
    @blp.response(200, LocationSchema(many=True))
    def get(self):
        return LocationModel.query.all()

    @blp.arguments(LocationSchema)
    @blp.response(201, LocationSchema)
    def post(self, location_data):
        location = LocationModel(**location_data)
        try:
            db.session.add(location)
            db.session.commit()

            return location
        except IntegrityError:
            abort(400, message="A location with that name already exists.")
        except SQLAlchemyError:
            abort(500, message="Error occurred while creating the location.")


@blp.route("/locations/<string:organization_id>")
class LocationByOrganization(MethodView):
    @blp.response(200, LocationSchema(many=True))
    def get(self, organization_id):
        return LocationModel.query.filter_by(organization_id=organization_id).all()
