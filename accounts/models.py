from django.db import models
# AbstractUserクラス(抽象クラス：継承することを前提としている)をインポート
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    '''
    Userモデルを継承したカスタムユーザーモデル
    '''
    pass
    