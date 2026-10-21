from flask import Blueprint, jsonify, request

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

@bp.route("/books", methods=["POST"])
def create_book():
    payload = request.get_json() or {}
    title = payload.get("title")
    if not title:
        return jsonify({"error": "title is required"}), 400
    new_id = max(BOOKS) + 1
    BOOKS[new_id] = {"id": new_id, "title": title}
    return jsonify(BOOKS[new_id]), 201
