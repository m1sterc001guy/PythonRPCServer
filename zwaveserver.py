from concurrent import futures
import grpc
import zwaveactions_pb2
import zwaveactions_pb2_grpc
import time

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class ZWaveActions(zwaveactions_pb2_grpc.ZWaveActionServicer):

  def TurnOn(self, request, context):
    print ('Received TurnOn Request')
    return zwaveactions_pb2.ToggleReply(success=True)

  def TurnOff(self, request, context):
    print ('Received TurnOff Request')
    return zwaveactions_pb2.ToggleReply(success=True)

def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  zwaveactions_pb2_grpc.add_ZWaveActionServicer_to_server(ZWaveActions(), server)
  server.add_insecure_port('[::]:50054')
  server.start()
  try:
    while True:
      time.sleep(_ONE_DAY_IN_SECONDS)
  except KeyboardInterrupt:
    server.stop(0)
  

if __name__ == '__main__':
  print ('Zwave Server Starting...')
  serve()
