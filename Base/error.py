""" 180222 Adel Liu

错误表，在编码时不断添加
"""


class E:
    _error_id = 0

    def __init__(self, msg, release_e=None):
        self.eid = E._error_id
        self.msg = msg
        self.release = release_e if isinstance(release_e, E) else None
        E._error_id += 1


class Error:
    OK = E("没有错误")
    ERROR_NOT_FOUND = E("不存在的错误")
    REQUIRE_PARAM = E("缺少参数")
    REQUIRE_JSON = E("需要JSON数据")
    REQUIRE_LOGIN = E("需要登录")
    STRANGE = E("未知错误")
    ERROR_METHOD = E("错误的HTTP请求方法")
    REQUIRE_BASE64 = E("参数需要base64编码")
    ERROR_PARAM_FORMAT = E("错误的参数格式")
    ERROR_VALIDATION_FUNC = E("错误的参数验证函数")
    REQUIRE_ROOT = E("需要管理员登录")

    ERROR_TUPLE_FORMAT = E("属性元组格式错误")
    ERROR_PROCESS_FUNC = E("参数预处理函数错误")
    JWT_PARAM_INCOMPLETE = E("身份认证token缺少参数")
    ERROR_JWT_FORMAT = E("身份认证token错误")
    JWT_EXPIRED = E("身份认证过期")
    ERROR_CREATE_USER = E("创建用户失败")
    NOT_FOUND_USER = E("不存在的用户")
    NOT_FOUND_CONFIG = E("不存在的配置")

    QTB_AUTH_FAIL = E("齐天簿身份认证失败")
    QTB_GET_INFO_FAIL = E("齐天簿获取用户信息失败")
    SS_OPERATION_FAST = E("对VPN帐号操作频率过快，请间隔五分钟")

    @classmethod
    def get_error_dict(cls):
        error_dict = dict()
        for k in cls.__dict__:
            if k[0] != '_':
                e = getattr(cls, k)
                if isinstance(e, E):
                    error_dict[k] = dict(eid=e.eid, msg=e.msg)
        return error_dict

