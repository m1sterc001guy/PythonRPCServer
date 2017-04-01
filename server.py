from concurrent import futures
import grpc
import actions_pb2
import actions_pb2_grpc
import time

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class SensorActions(actions_pb2_grpc.PiActionServicer):

  def IsMonitoringHealthy(self, request, context):
    return actions_pb2.MonitoringReply(isHealthy=True)


def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  actions_pb2_grpc.add_PiActionServicer_to_server(SensorActions(), server)
  server.add_insecure_port('[::]:50055')
  server.start()
  try:
    while True:
      time.sleep(_ONE_DAY_IN_SECONDS)
  except KeyboardInterrupt:
    server.stop(0)

if __name__ == '__main__':
  print ('Server Starting...')
  serve()
