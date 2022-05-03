
class DataModel:
    def __init__(self, request) -> None:
        self.IP=request.remote_addr
        self.user_agent=str(request.user_agent)