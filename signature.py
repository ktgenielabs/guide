import argparse
from datetime import datetime
from pytz import timezone
import hmac
import hashlib


def getTimestamp():
    return datetime.now(timezone("Asia/Seoul")).strftime("%Y%m%d%H%M%S%f")[:-3]


def getHmac(keyname, message, encode_mode="UTF-8"):
    signature = hmac.new(
        key=keyname.encode(encode_mode), msg=message.encode(encode_mode), digestmod=hashlib.sha256
    ).hexdigest()
    return signature


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="generate signature")
    parser.add_argument("-i", "--id", type=str, help="enter your client_id", required=True)
    parser.add_argument("-s", "--secret", type=str, help="enter your secret", required=True)
    parser.add_argument(
        "-t",
        "--timestamp",
        type=str,
        help="If this timestamp value is received, then it replaces the timestamp of current time. It will be used for test.",
    )
    args = parser.parse_args()

    timestamp = args.timestamp if args.timestamp else getTimestamp()
    client_id = args.id
    client_secret = args.secret
    signature = getHmac(client_secret, f"{client_id}:{timestamp}")
    print(
        f"""
    timestamp: {timestamp}
    signature: {signature}
    """
    )
