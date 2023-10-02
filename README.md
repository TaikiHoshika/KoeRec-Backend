# KoeRec
## About
KoeRecはシンプな録音サービスです。  
シンプルなデザイン、操作感をコンセプトに開発してます。

## Setup
```
git clone https://github.com/TaikiHoshika/KoeRec-Backend.git
cd KoeRec-Backend
pip install -r requirements.txt
python seeder.py
uvicorn main:app --reload
```

## Dependencies
- [FastAPI](https://github.com/tiangolo/fastapi)
- [Uvicorn](https://github.com/encode/uvicorn)
- [bcrypt](https://github.com/pyca/bcrypt/)
- [SQLModel](https://github.com/tiangolo/sqlmodel)
- [SQLite](https://www.sqlite.org/index.html)

## License
MIT License