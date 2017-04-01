import grpc

import zwaveactions_pb2
import zwaveactions_pb2_grpc

if __name__ == '__main__':
  print ('Client Starting...')
  channel = grpc.insecure_channel('localhost:50054')
  stub = zwaveactions_pb2_grpc.ZWaveActionStub(channel)
  response = stub.TurnOn(zwaveactions_pb2.ToggleRequest())
  print ("Client Received: " + str(response.success))
