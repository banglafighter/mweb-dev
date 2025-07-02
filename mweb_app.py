from mweb.mweb_engine import MWebEngine

mweb_engine = MWebEngine.bstart("MWeb Dev", __file__)
mweb_engine.version = "0.0.1"

cli = mweb_engine.cli
asgi = mweb_engine.get_app()

if __name__ == '__main__':
    mweb_engine.run()
