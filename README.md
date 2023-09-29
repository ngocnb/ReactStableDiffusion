# Installation

## API

Install python modules

```
pip install uvicorn uvloop fastapi diffusers torch transformers
pip install -U websockets
```

Add `diffusers-cli` to path

```
vi ~/.bashrc

export PATH="$HOME/.local/bin:$PATH"

source ~/.bashrc
```

# Run app

## API

```
uvicorn api:app --reload --port 9113 --root-path "/ai-api"
```

# Deployment

## API

```
pm2 start "uvicorn api:app --reload --port 9113 --root-path /ai-api" --name ai-api
```
