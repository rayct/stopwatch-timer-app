# macOS / Linux
python3 -m venv venv
source venv/bin/activate
<<<<<<< HEAD
```

Once activated, your shell prompt usually shows `(venv)`.

---

# 3️⃣ Install Dependencies Inside the venv

```bash
pip install customtkinter pytest
```

* `customtkinter` → modern UI
* `pytest` → unit tests
* Any future packages go here

---

# 4️⃣ Freeze Requirements

```bash
pip freeze > requirements.txt
```

`requirements.txt` now tracks **exact versions**, so others can replicate your environment.

Example:

```
customtkinter>=5.4.1
pytest==8.3.3
```

---

# 5️⃣ Update `.gitignore`

Add `venv/` to `.gitignore` so the virtual environment isn’t committed:

```
venv/
__pycache__/
*.pyc
.env
```

---

# 6️⃣ Run the App Within the venv

```bash
python src/app_modern.py
```

Now **all dependencies are contained**, and the system Python won’t interfere.

--

_**Documentation maintained by:**_ Raymond C. Turner

_**Date:**_ March 12th, 2026
=======
>>>>>>> parent of 6cf0894 (docs: added a venv.md and CONNTRIBUTING.md)

# Windows
python -m venv venv
venv\Scripts\activate
