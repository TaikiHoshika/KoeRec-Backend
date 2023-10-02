import json
import base64
import hmac
import hashlib

def encodeBase64(data : dict) -> str:
    return base64.urlsafe_b64encode(json.dumps(data).encode()).decode().strip("=")

def generateAccessToken(
    subject : str
    
) -> str:
    header = encodeBase64({
        "alg": "HS256",
        "typ": "JWT"
    })

    payload = encodeBase64({
        "iss": "https://koerec.example.com",  # 発行者
        "sub": 1,

        "iat": 100200,  # 発行時刻
        "exp": 130000,  # 有効期限
    })

    signature = base64.urlsafe_b64encode(
        hmac.new(
            b"21b86b5b5f5b1797622ebe10a2a62e99",
            str(header + "." + payload).encode(),
            hashlib.sha256
        ).digest()
    ).decode().strip("=")

    return(str(header + "." + payload + "." + signature))

if __name__ == "__main__":
    print(generateAccessToken())