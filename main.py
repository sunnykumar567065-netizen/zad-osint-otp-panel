from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, PlainTextResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Agar aapki website me CSS/JS ki alag files hain, toh unhe static folder me rakh sakte hain
# app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def serve_home(request: Request):
    try:
        # Templates folder se index.html read karna
        with open("templates/index.html", "r", encoding="utf-8") as f:
            html_content = f.read()
        return HTMLResponse(content=html_content, status_code=200)
    except Exception:
        return PlainTextResponse(
            "KYA HUA BETA ZAD OSINT KA WEB CODE NIKALGA KYA LAGTA HA TU BHUL GAYA KI YE WEB MAFIA NE BANYA HA",
            status_code=403
        )

# Agar koi unauthorized route ya direct hidden file access karne ki koshish kare
@app.get("/{full_path:path}", response_class=PlainTextResponse)
async def catch_all(full_path: str):
    return "KYA HUA BETA ZAD OSINT KA WEB CODE NIKALGA KYA LAGTA HA TU BHUL GAYA KI YE WEB MAFIA NE BANYA HA"
