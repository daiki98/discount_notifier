import requests


from src.get_api_token import get_api_token


class Notifier:
    """通知に関連する処理をまとめたクラスです
    """
    def __init__(self):
        pass

    def send_line_notify(self, notification_message):
        """LINEに通知を送信する

        Args:
            notification_message (string): 通知メッセージ
        """
        line_notify_token = get_api_token()
        line_notify_api = 'https://notify-api.line.me/api/notify'
        headers = {'Authorization': f'Bearer {line_notify_token}'}
        data = {'message': f'message: {notification_message}'}
        requests.post(line_notify_api, headers = headers, data = data)