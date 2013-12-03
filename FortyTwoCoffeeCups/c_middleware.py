from models import Http_Request_for_DB


class HttpRequestStoringMiddleware(object):

    def process_request(self, request):
        new_req = Http_Request_for_DB()
        new_req.server_name = request.META.get('SERVER_NAME')
        new_req.server_port = request.META.get('SERVER_PORT')
        new_req.other_info = str(request.__dict__)
        new_req.save()
        return
