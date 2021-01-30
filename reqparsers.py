from flask_restful import reqparse

def initializeParsers():
    putreqparser = reqparse.RequestParser()
    putreqparser.add_argument("name", type=str, help="", required = True)
    putreqparser.add_argument("wishlist", type=str)
    putreqparser.add_argument("email", type=str, help="", required = True)

    updatereqparser = reqparse.RequestParser()
    updatereqparser.add_argument("name", type=str, help="")
    updatereqparser.add_argument("wishlist", type=str)
    updatereqparser.add_argument("email", type=str, help="")

    return putreqparser, updatereqparser

if __name__ == "__main__":
    print("Run from main script")
    pass