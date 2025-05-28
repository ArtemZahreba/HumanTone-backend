from flask import Blueprint, request, jsonify
from app.services.rewritetext import RewriteService
from app.config import Config

bp = Blueprint('routes', __name__)
cfg = Config()
api_token = cfg.HUGGINGFACE_API_TOKEN


@bp.route('/rewrite', methods=['POST'])
def rewrite_text():
    data = request.get_json()
    input_text = data.get("text", "")

    if not input_text:
        return jsonify({"error": "No text provided"}), 400

    # Перевірка на ліміт довжини
    if len(input_text) > 500:
        return jsonify({"error": "Текст перевищує ліміт у 250 символів."}), 413

    # Ініціалізуємо сервіс
    rewriter = RewriteService(api_token=api_token)

    rewritten = rewriter.rewrite(input_text)

    return jsonify({"rewritten": rewritten})
