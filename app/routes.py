from app import app

from flask import request, jsonify

from backend.scrapers import Asura, AsyncAsura

from aiohttp import ClientSession
import asyncio

async def get(sess, url):
    response = await sess.get(url)
    return response

@app.route("/fetch/asura", methods=["POST"])
async def fetch_asura():
    rjson = request.json
    async with ClientSession() as session:
        target = rjson['url']
        asura = AsyncAsura(target)
        task = asyncio.create_task(asura.get(session))
        result = await asyncio.gather(task)

    return jsonify({"results": result})