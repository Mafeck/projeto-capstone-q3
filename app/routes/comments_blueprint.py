from flask import Blueprint

from app.controllers import comments_controllers


bp_comments = Blueprint("comments", __name__, url_prefix="/comments")

bp_comments.patch("/<comment_id>")(comments_controllers.update_comments)
bp_comments.delete("/<comment_id>")(comments_controllers.remove_comment)
bp_comments.post("")(comments_controllers.create_comments)
bp_comments.get("/<cpf>")(comments_controllers.get_comments_by_cpf)
bp_comments.get("")(comments_controllers.get_comment_by_id)
