# WebSocket Markdown Streaming API

A FastAPI application that provides a WebSocket endpoint for streaming random markdown content, simulating LLM streaming responses.

## Setup

1. Install dependencies:
```bash
poetry install
```

2. Run the server:
```bash
poetry run fastapi dev ws_test_api/main.py
```

## Usage

### WebSocket Endpoint

Connect to `ws://localhost:8000/stream` to receive infinite streaming markdown content.

### Testing Options

**Option 1: Browser Console**
1. Open http://localhost:8000 in your browser
2. Open developer tools and run:
```javascript
const ws = new WebSocket('ws://localhost:8000/stream');
ws.onmessage = (event) => console.log(event.data);
```

**Option 2: Python WebSocket Client**
```python
import asyncio
import websockets

async def test_client():
    uri = "ws://localhost:8000/stream"
    async with websockets.connect(uri) as websocket:
        async for message in websocket:
            print(message, end='', flush=True)

asyncio.run(test_client())
```

**Option 3: wscat**
```bash
# Install wscat if not already installed
npm install -g wscat

# Connect to the WebSocket endpoint
wscat -c ws://localhost:8000/stream
```

## Features

- Streams random markdown content in chunks (1-5 words)
- Realistic delays (100-500ms between chunks) to simulate LLM responses
- Includes various markdown elements: headers, lists, code blocks, tables, quotes
- Infinite streaming until client disconnects
- REST endpoint at `/` provides API information

## API Endpoints

- `GET /` - API information and usage instructions
- `WebSocket /stream` - Infinite markdown streaming endpoint