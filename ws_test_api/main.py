import asyncio
import random
from typing import AsyncGenerator

from fastapi import FastAPI, WebSocket, WebSocketDisconnect


app = FastAPI()


async def generate_random_markdown() -> AsyncGenerator[str, None]:
    """Generate random markdown content to simulate LLM streaming response."""
    
    markdown_templates = [
        "# {title}\n\nThis is a **bold** statement about {topic}.\n\n",
        "## {subtitle}\n\n*Italic text* describing {concept} in detail.\n\n",
        "### Key Points\n\n- Point one about {item}\n- Point two with `code snippet`\n- Point three with [link](https://example.com)\n\n",
        "```python\n# Sample code block\ndef {function_name}():\n    return \"{return_value}\"\n```\n\n",
        "> This is a blockquote about {quote_topic}.\n> It spans multiple lines.\n\n",
        "| Column 1 | Column 2 |\n|----------|----------|\n| {data1} | {data2} |\n| {data3} | {data4} |\n\n",
        "1. First numbered item about {list_item1}\n2. Second numbered item about {list_item2}\n3. Third numbered item about {list_item3}\n\n"
    ]
    
    placeholders = {
        'title': ['Advanced Concepts', 'Technical Overview', 'Implementation Guide', 'Best Practices'],
        'topic': ['performance', 'scalability', 'security', 'optimization'],
        'subtitle': ['Implementation Details', 'Configuration', 'Usage Examples'],
        'concept': ['architecture', 'design patterns', 'algorithms', 'data structures'],
        'item': ['caching strategies', 'error handling', 'logging', 'monitoring'],
        'function_name': ['process_data', 'validate_input', 'format_output', 'handle_request'],
        'return_value': ['success', 'processed_data', 'valid_response', 'formatted_result'],
        'quote_topic': ['software engineering', 'code quality', 'team collaboration', 'continuous improvement'],
        'data1': ['Value A', 'Item 1', 'Result X'],
        'data2': ['Value B', 'Item 2', 'Result Y'],
        'data3': ['Value C', 'Item 3', 'Result Z'],
        'data4': ['Value D', 'Item 4', 'Result W'],
        'list_item1': ['setup configuration', 'initial planning', 'requirement analysis'],
        'list_item2': ['implementation phase', 'testing strategy', 'deployment process'],
        'list_item3': ['maintenance tasks', 'monitoring setup', 'performance tuning']
    }
    
    while True:
        template = random.choice(markdown_templates)
        
        # Fill in placeholders
        filled_template = template
        for placeholder, options in placeholders.items():
            if f'{{{placeholder}}}' in filled_template:
                filled_template = filled_template.replace(f'{{{placeholder}}}', random.choice(options))
        
        # Stream in random chunks with delay
        words = filled_template.split()
        current_chunk = ""
        
        for word in words:
            current_chunk += word + " "
            
            # Randomly decide when to send a chunk (1-5 words)
            if random.randint(1, 5) == 1 or len(current_chunk.split()) >= 5:
                yield current_chunk
                current_chunk = ""
                # Random delay between chunks to simulate LLM response timing
                await asyncio.sleep(random.uniform(0.1, 0.5))
        
        # Send any remaining chunk
        if current_chunk.strip():
            yield current_chunk
        
        # Longer pause between sections
        await asyncio.sleep(random.uniform(0.5, 2.0))


@app.websocket("/stream")
async def websocket_endpoint(websocket: WebSocket):
    """WebSocket endpoint that streams random markdown content."""
    await websocket.accept()
    
    try:
        async for chunk in generate_random_markdown():
            await websocket.send_text(chunk)
    except WebSocketDisconnect:
        print("Client disconnected")
    except Exception as e:
        print(f"Error in WebSocket connection: {e}")
        await websocket.close()


@app.get("/")
async def root():
    """Root endpoint with basic info."""
    return {
        "message": "WebSocket Markdown Streaming API",
        "websocket_url": "ws://localhost:8000/stream",
        "description": "Connect to /stream endpoint via WebSocket to receive infinite streaming markdown content"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)