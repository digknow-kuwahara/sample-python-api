from flask import Blueprint, jsonify

bp = Blueprint("bf_check", __name__)

BOOKS = {1: {"id": 1, "title": "Clean Architecture"}}


@bp.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


@bp.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = BOOKS.get(book_id)
    if book is None:
        return jsonify({"error": "not found"}), 404
    return jsonify(book)
