# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from bot.utils.yandex.cloud.ai.stt.v2 import stt_service_pb2 as yandex_dot_cloud_dot_ai_dot_stt_dot_v2_dot_stt__service__pb2
from bot.utils.yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2


class SttServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.LongRunningRecognize = channel.unary_unary(
                '/yandex.cloud.ai.stt.v2.SttService/LongRunningRecognize',
                request_serializer=yandex_dot_cloud_dot_ai_dot_stt_dot_v2_dot_stt__service__pb2.LongRunningRecognitionRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                )
        self.StreamingRecognize = channel.stream_stream(
                '/yandex.cloud.ai.stt.v2.SttService/StreamingRecognize',
                request_serializer=yandex_dot_cloud_dot_ai_dot_stt_dot_v2_dot_stt__service__pb2.StreamingRecognitionRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_ai_dot_stt_dot_v2_dot_stt__service__pb2.StreamingRecognitionResponse.FromString,
                )


class SttServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def LongRunningRecognize(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StreamingRecognize(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SttServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'LongRunningRecognize': grpc.unary_unary_rpc_method_handler(
                    servicer.LongRunningRecognize,
                    request_deserializer=yandex_dot_cloud_dot_ai_dot_stt_dot_v2_dot_stt__service__pb2.LongRunningRecognitionRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'StreamingRecognize': grpc.stream_stream_rpc_method_handler(
                    servicer.StreamingRecognize,
                    request_deserializer=yandex_dot_cloud_dot_ai_dot_stt_dot_v2_dot_stt__service__pb2.StreamingRecognitionRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_ai_dot_stt_dot_v2_dot_stt__service__pb2.StreamingRecognitionResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.ai.stt.v2.SttService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SttService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def LongRunningRecognize(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.ai.stt.v2.SttService/LongRunningRecognize',
            yandex_dot_cloud_dot_ai_dot_stt_dot_v2_dot_stt__service__pb2.LongRunningRecognitionRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def StreamingRecognize(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/yandex.cloud.ai.stt.v2.SttService/StreamingRecognize',
            yandex_dot_cloud_dot_ai_dot_stt_dot_v2_dot_stt__service__pb2.StreamingRecognitionRequest.SerializeToString,
            yandex_dot_cloud_dot_ai_dot_stt_dot_v2_dot_stt__service__pb2.StreamingRecognitionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
