 
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

# HTML 페이지 제공
@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <!DOCTYPE html>
    <html lang="ko">
    <head>
        <meta charset="UTF-8">
        <title>FastAPI HTML 서버</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; margin: 50px; }
            h1 { color: blue; }
        </style>
    </head>
    <body>
        <h1>🚀 FastAPI 서버에서 제공하는 HTML 페이지</h1>
        <p>fex.p-e.kr 도메인에서 실행 중</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=80)  # 80번 포트에서 실행
