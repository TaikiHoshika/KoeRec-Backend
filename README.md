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
- FastAPI
- UVCorn
- SQLModel
- SQLite

## License
MIT License