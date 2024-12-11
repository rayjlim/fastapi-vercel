# FastAPI on Vercel Example

This is [FastAPI](https://fastapi.tiangolo.com/) example app deployed on [Vercel](https://vercel.com/).

## Requirements

- Vercel account
- [Vercel CLI](https://vercel.com/cli)

### Setup

1. `git clone && cd fastapi-vercel`
2. _(Recommended)_ Create a virtual environment and activate it

    ```bash
    python -m venv env

    source env/bin/activate
    ```

3. Install dependencies

    ```bash
    pip install -r requirements.txt
    ```

4. Deploy to Vercel

    ```bash
    vercel
    ```

---

## Development

1. `pipenv install -r requirements.txt` then `pipenv shell`
2. Run server `uvicorn app:app --reload`
3. Visit `http://localhost:8000/prompt/`

## Status

2023-04-23 Problems setting up virtual env (venv, pipenv) on windows
- try stripping requirements, make sure python version in pipfile matches `python -v`