
## 1. Create Virtual Environment

```bash id="1a2b3c"
python -m venv venv
```

Activate:

```bash id="4d5e6f"
venv\Scripts\activate
```

---

## 2. Install Dependencies

```
pip install -r requirements.txt
```

---

## 3. Setup Environment Variables

Create a `.env` file:

```env id="0j1k2l"
DB_HOST=localhost
DB_PORT=5432
DB_NAME=your_db
DB_USER=your_user
DB_PASSWORD=your_password
```

---

## 4. Run Database DDL

```bash id="3m4n5o"
psql -U your_user -d your_db -f schema.sql
```

---

## 5. Run the App

```bash id="6p7q8r"
uvicorn app.main:app --reload
```

---

## Access

* http://127.0.0.1:8000
* http://127.0.0.1:8000/docs
