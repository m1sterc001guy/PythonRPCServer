from concurrent import futures
import grpc
import actions_pb2
import actions_pb2_grpc
import zwaveactions_pb2
import zwaveactions_pb2_grpc
import time

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class SensorActions(actions_pb2_grpc.PiActionServicer):

  def IsMonitoringHealthy(self, request, context):
    return actions_pb2.MonitoringReply(isHealthy=True)

  def TurnOnLight(self, request, context):

    print ('Redirecting turn on request to zwave pi')
    channel = grpc.insecure_channel('192.168.1.73:50054')
    stub = zwaveactions_pb2_grpc.ZWaveActionStub(channel)
    response = stub.TurnOn(zwaveactions_pb2.ToggleRequest())

    return actions_pb2.ToggleLightReply(success=response.success)

  def TurnOffLight(self, request, context):
    print ('Redirecting turn off request to zwave pi')
    channel = grpc.insecure_channel('192.168.1.73:50054')
    stub = zwaveactions_pb2_grpc.ZWaveActionStub(channel)
    response = stub.TurnOff(zwaveactions_pb2.ToggleRequest())
    return actions_pb2.ToggleLightReply(success=response.success)


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
