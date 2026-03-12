## 1️⃣ CONTRIBUTING.md

````markdown
# Contributing to Stopwatch & Timer App

Thank you for considering contributing! This guide will help you set up your development environment and follow our workflow.

---

## 1. Setup

1. Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/stopwatch-timer-app.git
cd stopwatch-timer-app
````

2. Create and activate a virtual environment:

```bash
# macOS / Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 2. Branching Workflow

* Use **feature branches** for new work:

  ```bash
  git checkout -b feature/<short-description>
  ```

* Example:

  * `feature/roller-animation`
  * `feature/alarm-notification`
  * `feature/lap-tracking`

* Make incremental commits with clear messages:

```
feat: add roller-style timer picker
fix: correct timer reset behavior
refactor: split stopwatch logic into class
```

* Push branch to GitHub:

```bash
git push origin feature/<short-description>
```

* Open a Pull Request (PR) linking to the relevant issue.

---

## 3. Issues

* Each new feature or bug should have a **GitHub issue**.
* Reference issues in PRs:

  ```
  Closes #<issue_number>
  ```

---

## 4. Testing

* Unit tests are in `tests/`.
* Run all tests with `pytest`:

```bash
pytest
```

* Ensure all tests pass before submitting a PR.

---

## 5. Code Style

* Follow PEP 8 for Python code.
* Keep UI modular: separate logic and interface.
* Comment complex sections for clarity.

---

## 6. Suggestions & Feedback

* Open an issue for any bug, improvement, or new feature request.
* Use discussion threads for larger design proposals.

```

---

## 2️⃣ Example GitHub Issues

### Issue 1: Animate Timer Roller
**Title:** Animate timer roller like iOS  
**Description:**  
- Implement smooth scrolling for hours/minutes/seconds selectors.  
- Mimic Apple-style roller animation for timer digits.  
- Should work in **CustomTkinter**.  
- Include touch or mouse wheel scrolling if possible.  

**Labels:** `enhancement`, `UI`, `feature`

---

### Issue 2: Alarm / Notification
**Title:** Alarm/Notification when timer ends  
**Description:**  
- Trigger a sound or system notification when timer reaches zero.  
- Cross-platform support (Windows, macOS, Linux).  
- Optionally, allow users to customize alarm sound.  

**Labels:** `enhancement`, `feature`, `notification`

---

### Issue 3: Stopwatch Lap Tracking
**Title:** Add lap tracking for stopwatch  
**Description:**  
- Record lap times while stopwatch is running.  
- Display laps in a scrollable list below the timer.  
- Include options: reset laps, save laps.  

**Labels:** `enhancement`, `feature`, `stopwatch`

---

✅ **Workflow Suggestion**

1. Create an **issue for each feature** (like above).  
2. Create a **feature branch**: `feature/roller-animation`, etc.  
3. Implement + test the feature in that branch.  
4. Open a **Pull Request** linking the issue.  
5. Merge into `main` and close the issue automatically.

---

_**Documentation maintained by:**_ Raymond C. Turner

_**Date:**_ March 11th, 2026
