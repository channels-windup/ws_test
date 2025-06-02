# Frontend/Mobile Developer Challenge: Markdown Streaming Viewer

## Overview
Build a React Native/Expo application that connects to a WebSocket endpoint and renders streaming markdown content in real-time. This challenge simulates how AI chat applications display streaming responses from language models.

## The Task
Create an application that:
1. Connects to the provided WebSocket endpoint
2. Receives and displays streaming markdown content as it arrives
3. Renders the markdown with proper formatting and styling
4. Provides a smooth, responsive user experience

## Technical Requirements

### Platform Choice 
- **React Native/Expo** - for mobile app development

### Core Technologies
- TypeScript (required)
- WebSocket client implementation
- Markdown rendering library
- State management (your choice)

### Backend API
A WebSocket server is provided that streams random markdown content:
- **Endpoint**: `ws://localhost:8000/stream`
- **Behavior**: Continuously streams markdown text in chunks with realistic delays
- **Content**: Headers, lists, code blocks, tables, quotes, and formatted text

## Getting Started

### 1. Start the Backend Server
```bash
# Clone this repository and navigate to the project
cd ws_test

# Install dependencies
poetry install

# Start the server
poetry run fastapi dev conf_test_api/main.py
```

The server will be available at `http://localhost:8000` with WebSocket endpoint at `ws://localhost:8000/stream`.

### 2. Test the WebSocket Connection
Verify the server works using wscat:
```bash
npm install -g wscat
wscat -c ws://localhost:8000/stream
```

You should see markdown content streaming to your terminal.

## Implementation Guidelines

### Required Features
1. **WebSocket Connection Management**
   - Connect to `ws://localhost:8000/stream`
   - Handle connection states (connecting, connected, disconnected, error)
   - Implement reconnection logic for connection failures

2. **Real-time Markdown Rendering**
   - Display markdown content as it streams in
   - Proper rendering of all markdown elements (headers, lists, code, tables, etc.)
   - Smooth text appearance without jarring reflows

3. **User Interface**
   - Clean, readable design

### Bonus Features (Optional)
- Auto-scroll to follow new content
- Syntax highlighting for code blocks
- Connection controls (pause/resume/reconnect)
- Performance optimization for large content

## Submission Requirements

1. **Source Code**
   - Complete project with all dependencies
   - Clear project structure
   - TypeScript implementation

2. **Documentation**
   - README with setup instructions
   - Brief explanation of architecture choices
   - Any trade-offs or limitations

3. **Demo**
   - Working application (screenshots or video)
   - Instructions to run the project

## Questions?
If you have any questions about the requirements or need clarification, please don't hesitate to ask.
