import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", 6088962718:AAFqdoJFm-egJzzx_XEVFflKPqOl3EfixqM)
    STRING_SESSION = os.environ.get("STRING_SESSION", 1BVtsOHUBuxa7f_WCpIjYn2dL8_9Km9dNM3nTLXownIza9Bs2J5ntDtmkctkSWvpc5oSZFkAKVg9XpSsxFhP4CLXEUXuakiGHn_H2lCL2WxiAz7LFKjcZv8e6aT4YqERWt6UBk7k6-5OiuHL19rSLdaouGmmyPxw1N72T-krIQ53lWbLvNRIwfMH_1IurEao1ZaCVbe7lycz5RVafEytAAWNe_PnaUq5rurwE2G5ym40fUPMDgqT71nfe_zcuTsTGgtecBMXL2KBVvKVpD5eiXszQSsdxHsaF1Ye5abm_C2ZPKM0VSBh2vtCkF82DMfkPyJ4hk_SmdUH_l-6kaZ7cb45nghUdlqI=)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "1755920808")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True"
