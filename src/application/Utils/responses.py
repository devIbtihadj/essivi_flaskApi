from flask import jsonify


class Response():
    @staticmethod
    def success_response(http_code, http_message, message, data):
        response = {
            'code': http_code,
            'httpMessage': http_message,
            'message': message,
            'data': data
        }
        return jsonify(response)

    @staticmethod
    def error_response(http_code, http_message, message):
        response = {
            'httpCode': http_code,
            'httpMessage': http_message,
            'message': message
        }
        return jsonify(response)
