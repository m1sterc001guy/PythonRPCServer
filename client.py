import grpc

import actions_pb2
import actions_pb2_grpc

if __name__ == '__main__':
  print ('Client Starting...')
  channel = grpc.insecure_channel('localhost:50055')
  stub = actions_pb2_grpc.PiActionStub(channel)
  response = stub.IsMonitoringHealthy(actions_pb2.MonitoringRequest())
  print("Client Received: " + str(response.isHealthy))
