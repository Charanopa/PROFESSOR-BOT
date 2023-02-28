from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response("Megaverse Bot")

async def web_server():
    web_app = web.Application(client_max_size=3000)
    web_app.add_routes(routes)
    return web_app
