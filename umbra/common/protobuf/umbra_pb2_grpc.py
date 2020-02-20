# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import umbra_pb2 as umbra__pb2


class BrokerStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Run = channel.unary_unary(
        '/umbra.Broker/Run',
        request_serializer=umbra__pb2.Config.SerializeToString,
        response_deserializer=umbra__pb2.Report.FromString,
        )


class BrokerServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Run(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_BrokerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Run': grpc.unary_unary_rpc_method_handler(
          servicer.Run,
          request_deserializer=umbra__pb2.Config.FromString,
          response_serializer=umbra__pb2.Report.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'umbra.Broker', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class ScenarioStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Run = channel.unary_unary(
        '/umbra.Scenario/Run',
        request_serializer=umbra__pb2.Deploy.SerializeToString,
        response_deserializer=umbra__pb2.Built.FromString,
        )


class ScenarioServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Run(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ScenarioServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Run': grpc.unary_unary_rpc_method_handler(
          servicer.Run,
          request_deserializer=umbra__pb2.Deploy.FromString,
          response_serializer=umbra__pb2.Built.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'umbra.Scenario', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
