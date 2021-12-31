from flask import Blueprint, request
from api.models import *
from api.core import create_response, serialize_list, logger
from sqlalchemy import inspect

main = Blueprint("main", __name__)  # initialize blueprint


# function that is called when you visit /
@main.route("/")
def index():
    # you are now in the current application context with the main.route decorator
    # access the logger with the logger from api.core and uses the standard logging module
    # try using ipdb here :) you can inject yourself
    logger.info("Comcast VCW")
    return "<h1>COMCAST VCW!</h1>"

###### GET REQUESTS ######

# function that is called when you visit /announcements


@main.route("/announcements", methods=["GET"])
def get_announcements():
    print(request.args.get("id"))
    announcements = Announcement.query.all()
    return create_response(data={"announcements": serialize_list(announcements)})

# function that is called when you visit /statuses


@main.route("/statuses", methods=["GET"])
def get_status():
    statuses = Status.query.all()
    return create_response(data={"statuses": serialize_list(statuses)})

# function that is called when you visit /statuses


@main.route("/accounts", methods=["GET"])
def get_account():
    accounts = Account.query.all()
    return create_response(data={"accounts": serialize_list(accounts)})

# function that is called when you visit /channels


@main.route("/channels", methods=["GET"])
def get_channel():
    channels = Channel.query.all()
    return create_response(data={"channels": serialize_list(channels)})

# function that is called when you visit /entitlements


@main.route("/entitlements", methods=["GET"])
def get_entitlement():
    entitlements = Entitlement.query.all()
    return create_response(data={"entitlements": serialize_list(entitlements)})


######## POST REQUESTS ##########

# POST request for /Announcements
@main.route("/announcements", methods=["POST"])
def create_announcement():
    data = request.get_json()

    logger.info("Data recieved: %s", data)
    if "name" not in data:
        msg = "No name provided for Announcement."
        logger.info(msg)
        return create_response(status=422, message=msg)

    # create SQLAlchemy Objects
    new_announcement = Announcement(name=data["name"], id=data["id"], time_of_creation=data["time_of_creation"],
                                    poster=data["poster"], subject=data["subject"], description=data["description"])

    # commit it to database
    db.session.add_all([new_announcement])
    db.session.commit()
    return create_response(
        message=f"Successfully created announcement {new_announcement.name} with id: {new_announcement.id}"
    )

 # POST request for /Statuses


@main.route("/statuses", methods=["POST"])
def create_status():
    data = request.get_json()

    logger.info("Data recieved: %s", data)
    if "name" not in data:
        msg = "No name provided for status."
        logger.info(msg)
        return create_response(status=422, message=msg)

    # create SQLAlchemy Objects
    new_status = Status(name=data["name"], id=data["id"], type=data["type"], load_start=data["load_start"],
                        load_completed=data["load_completed"], merlin_ready=data["merlin_ready"], file=data["file"])

    # commit it to database
    db.session.add_all([new_status])
    db.session.commit()
    return create_response(
        message=f"Successfully created status {new_status.name} with id: {new_status.id}"
    )


# POST request for /Account
@main.route("/accounts", methods=["POST"])
def create_account():
    data = request.get_json()

    logger.info("Data recieved: %s", data)
    if "name" not in data:
        msg = "No name provided for account."
        logger.info(msg)
        return create_response(status=422, message=msg)

    # create SQLAlchemy Objects
    new_account = Account(name=data["name"], id=data["id"], channel_number=data["channel_number"], call_sign=data["call_sign"],
                          full_name=data["full_name"], source_id=data["source_id"], hdtv=data["hgtv"], load_date=data["load_date"])

    # commit it to database
    db.session.add_all([new_account])
    db.session.commit()
    return create_response(
        message=f"Successfully created announcement {new_account.name} with id: {new_account.id}"
    )

# POST request for /Channel


@main.route("/channels", methods=["POST"])
def create_channel():
    data = request.get_json()

    logger.info("Data recieved: %s", data)
    if "name" not in data:
        msg = "No name provided for channel."
        logger.info(msg)
        return create_response(status=422, message=msg)

    # create SQLAlchemy Objects
    new_channel = Channel(name=data["name"], id=data["id"], channel_number=data["channel_number"], call_sign=data["call_sign"],
                          full_name=data["full_name"], source_id=data["source_id"], hdtv=data["hgtv"], load_date=data["load_date"])

    # commit it to database
    db.session.add_all([new_channel])
    db.session.commit()
    return create_response(
        message=f"Successfully created channel {new_channel.name} with id: {new_channel.id}"
    )

# POST request for /Entitlement


@main.route("/entitlements", methods=["POST"])
def create_entitlement():
    data = request.get_json()

    logger.info("Data recieved: %s", data)
    if "name" not in data:
        msg = "No name provided for entitlement."
        logger.info(msg)
        return create_response(status=422, message=msg)

    # create SQLAlchemy Objects
    new_entitlement = Entitlement(name=data["name"], id=data["id"], bsg_handle=data["bsg_handle"], source_id=data["source_id"],
                                  call_letters=data["call_letters"], billing_load_date=data["billing_load_date"], controller_load_date=data["controller_load_date"])

    # commit it to database
    db.session.add_all([new_entitlement])
    db.session.commit()
    return create_response(
        message=f"Successfully created entitlement {new_entitlement.name} with id: {new_entitlement.id}"
    )
