""" a minimal static server, primarily for performing audits
    this is not meant to be used in production, and some settings are insecure
    to game auditing metrics which will vary substantially by deployment
"""
from pathlib import Path
from tornado import ioloop, web, options

options.define("port", default=8000, help="port to listen on")
options.define(
    "host", default="127.0.0.1", help="host interface to connect on (0.0.0.0 is all)"
)
options.define("static_path", default="_build", help="static directory to serve")

SETTINGS = dict(  # noqa: C408
    # enabling compression can have security impacts if not done correctly
    compress_response=True,
    # not really useful for production
    autoreload=True,
    debug=True,
)


class CacheStaticHandler(web.StaticFileHandler):
    def get_cache_time(self, *args, **kwargs):
        """Don't cache; for testing only"""
        return 0


def make_app(static_path):
    """create and return (but do not start) a tornado app"""
    app = web.Application(
        [(r"^/(.*)", CacheStaticHandler, {"path": static_path})], **SETTINGS
    )
    return app


def main(port, host, static_path):
    """start a tornado app on the desired port"""
    static_path = Path(static_path).resolve()
    app = make_app(static_path)
    app.listen(port, host)
    url = "http://{}:{}/index.html".format(host, port)
    print("Watching files: \t\t{}".format(static_path))
    print("Hosting site on:\t\t{}".format(url))
    print("\nPress `Ctrl+C` to stop")
    try:
        ioloop.IOLoop.current().start()
    except KeyboardInterrupt:
        ioloop.IOLoop.current().stop()
        print("The server was stopped")


if __name__ == "__main__":
    options.parse_command_line()
    main(
        port=options.options.port,
        host=options.options.host,
        static_path=options.options.static_path,
    )
