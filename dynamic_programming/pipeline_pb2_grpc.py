# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import pipeline_pb2 as pipeline__pb2


class StreamingPipelineStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Stream1 = channel.unary_stream(
                '/pipeline.StreamingPipeline/Stream1',
                request_serializer=pipeline__pb2.StreamRequest.SerializeToString,
                response_deserializer=pipeline__pb2.StreamResponse1.FromString,
                )
        self.Stream2 = channel.unary_stream(
                '/pipeline.StreamingPipeline/Stream2',
                request_serializer=pipeline__pb2.StreamRequest.SerializeToString,
                response_deserializer=pipeline__pb2.StreamResponse2.FromString,
                )
        self.Stream3 = channel.unary_stream(
                '/pipeline.StreamingPipeline/Stream3',
                request_serializer=pipeline__pb2.StreamRequest.SerializeToString,
                response_deserializer=pipeline__pb2.StreamResponse3.FromString,
                )
        self.Stream4 = channel.unary_stream(
                '/pipeline.StreamingPipeline/Stream4',
                request_serializer=pipeline__pb2.StreamRequest.SerializeToString,
                response_deserializer=pipeline__pb2.StreamResponse4.FromString,
                )
        self.Stream5 = channel.unary_stream(
                '/pipeline.StreamingPipeline/Stream5',
                request_serializer=pipeline__pb2.StreamRequest.SerializeToString,
                response_deserializer=pipeline__pb2.StreamResponse5.FromString,
                )
        self.Stream6 = channel.unary_stream(
                '/pipeline.StreamingPipeline/Stream6',
                request_serializer=pipeline__pb2.StreamRequest.SerializeToString,
                response_deserializer=pipeline__pb2.StreamResponse6.FromString,
                )
        self.Stream7 = channel.unary_stream(
                '/pipeline.StreamingPipeline/Stream7',
                request_serializer=pipeline__pb2.StreamRequest.SerializeToString,
                response_deserializer=pipeline__pb2.StreamResponse7.FromString,
                )
        self.Stream8 = channel.unary_stream(
                '/pipeline.StreamingPipeline/Stream8',
                request_serializer=pipeline__pb2.StreamRequest.SerializeToString,
                response_deserializer=pipeline__pb2.StreamResponse8.FromString,
                )
        self.Stream9 = channel.unary_stream(
                '/pipeline.StreamingPipeline/Stream9',
                request_serializer=pipeline__pb2.StreamRequest.SerializeToString,
                response_deserializer=pipeline__pb2.StreamResponse9.FromString,
                )
        self.Stream10 = channel.unary_stream(
                '/pipeline.StreamingPipeline/Stream10',
                request_serializer=pipeline__pb2.StreamRequest.SerializeToString,
                response_deserializer=pipeline__pb2.StreamResponse10.FromString,
                )
        self.Stream11 = channel.unary_stream(
                '/pipeline.StreamingPipeline/Stream11',
                request_serializer=pipeline__pb2.StreamRequest.SerializeToString,
                response_deserializer=pipeline__pb2.StreamResponse11.FromString,
                )
        self.Stream12 = channel.unary_stream(
                '/pipeline.StreamingPipeline/Stream12',
                request_serializer=pipeline__pb2.StreamRequest.SerializeToString,
                response_deserializer=pipeline__pb2.StreamResponse12.FromString,
                )
        self.Stream13 = channel.unary_stream(
                '/pipeline.StreamingPipeline/Stream13',
                request_serializer=pipeline__pb2.StreamRequest.SerializeToString,
                response_deserializer=pipeline__pb2.StreamResponse13.FromString,
                )
        self.Stream14 = channel.unary_stream(
                '/pipeline.StreamingPipeline/Stream14',
                request_serializer=pipeline__pb2.StreamRequest.SerializeToString,
                response_deserializer=pipeline__pb2.StreamResponse14.FromString,
                )
        self.Stream15 = channel.unary_stream(
                '/pipeline.StreamingPipeline/Stream15',
                request_serializer=pipeline__pb2.StreamRequest.SerializeToString,
                response_deserializer=pipeline__pb2.StreamResponse15.FromString,
                )
        self.Stream16 = channel.unary_stream(
                '/pipeline.StreamingPipeline/Stream16',
                request_serializer=pipeline__pb2.StreamRequest.SerializeToString,
                response_deserializer=pipeline__pb2.StreamResponse16.FromString,
                )
        self.Stream17 = channel.unary_stream(
                '/pipeline.StreamingPipeline/Stream17',
                request_serializer=pipeline__pb2.StreamRequest.SerializeToString,
                response_deserializer=pipeline__pb2.StreamResponse17.FromString,
                )
        self.Stream18 = channel.unary_stream(
                '/pipeline.StreamingPipeline/Stream18',
                request_serializer=pipeline__pb2.StreamRequest.SerializeToString,
                response_deserializer=pipeline__pb2.StreamResponse18.FromString,
                )
        self.Stream19 = channel.unary_stream(
                '/pipeline.StreamingPipeline/Stream19',
                request_serializer=pipeline__pb2.StreamRequest.SerializeToString,
                response_deserializer=pipeline__pb2.StreamResponse19.FromString,
                )
        self.Stream20 = channel.unary_stream(
                '/pipeline.StreamingPipeline/Stream20',
                request_serializer=pipeline__pb2.StreamRequest.SerializeToString,
                response_deserializer=pipeline__pb2.StreamResponse20.FromString,
                )
        self.Stream21 = channel.unary_stream(
                '/pipeline.StreamingPipeline/Stream21',
                request_serializer=pipeline__pb2.StreamRequest.SerializeToString,
                response_deserializer=pipeline__pb2.StreamResponse21.FromString,
                )
        self.Stream22 = channel.unary_stream(
                '/pipeline.StreamingPipeline/Stream22',
                request_serializer=pipeline__pb2.StreamRequest.SerializeToString,
                response_deserializer=pipeline__pb2.StreamResponse22.FromString,
                )
        self.Stream23 = channel.unary_stream(
                '/pipeline.StreamingPipeline/Stream23',
                request_serializer=pipeline__pb2.StreamRequest.SerializeToString,
                response_deserializer=pipeline__pb2.StreamResponse23.FromString,
                )
        self.Stream24 = channel.unary_stream(
                '/pipeline.StreamingPipeline/Stream24',
                request_serializer=pipeline__pb2.StreamRequest.SerializeToString,
                response_deserializer=pipeline__pb2.StreamResponse24.FromString,
                )


class StreamingPipelineServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Stream1(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Stream2(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Stream3(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Stream4(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Stream5(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Stream6(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Stream7(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Stream8(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Stream9(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Stream10(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Stream11(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Stream12(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Stream13(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Stream14(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Stream15(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Stream16(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Stream17(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Stream18(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Stream19(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Stream20(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Stream21(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Stream22(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Stream23(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Stream24(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StreamingPipelineServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Stream1': grpc.unary_stream_rpc_method_handler(
                    servicer.Stream1,
                    request_deserializer=pipeline__pb2.StreamRequest.FromString,
                    response_serializer=pipeline__pb2.StreamResponse1.SerializeToString,
            ),
            'Stream2': grpc.unary_stream_rpc_method_handler(
                    servicer.Stream2,
                    request_deserializer=pipeline__pb2.StreamRequest.FromString,
                    response_serializer=pipeline__pb2.StreamResponse2.SerializeToString,
            ),
            'Stream3': grpc.unary_stream_rpc_method_handler(
                    servicer.Stream3,
                    request_deserializer=pipeline__pb2.StreamRequest.FromString,
                    response_serializer=pipeline__pb2.StreamResponse3.SerializeToString,
            ),
            'Stream4': grpc.unary_stream_rpc_method_handler(
                    servicer.Stream4,
                    request_deserializer=pipeline__pb2.StreamRequest.FromString,
                    response_serializer=pipeline__pb2.StreamResponse4.SerializeToString,
            ),
            'Stream5': grpc.unary_stream_rpc_method_handler(
                    servicer.Stream5,
                    request_deserializer=pipeline__pb2.StreamRequest.FromString,
                    response_serializer=pipeline__pb2.StreamResponse5.SerializeToString,
            ),
            'Stream6': grpc.unary_stream_rpc_method_handler(
                    servicer.Stream6,
                    request_deserializer=pipeline__pb2.StreamRequest.FromString,
                    response_serializer=pipeline__pb2.StreamResponse6.SerializeToString,
            ),
            'Stream7': grpc.unary_stream_rpc_method_handler(
                    servicer.Stream7,
                    request_deserializer=pipeline__pb2.StreamRequest.FromString,
                    response_serializer=pipeline__pb2.StreamResponse7.SerializeToString,
            ),
            'Stream8': grpc.unary_stream_rpc_method_handler(
                    servicer.Stream8,
                    request_deserializer=pipeline__pb2.StreamRequest.FromString,
                    response_serializer=pipeline__pb2.StreamResponse8.SerializeToString,
            ),
            'Stream9': grpc.unary_stream_rpc_method_handler(
                    servicer.Stream9,
                    request_deserializer=pipeline__pb2.StreamRequest.FromString,
                    response_serializer=pipeline__pb2.StreamResponse9.SerializeToString,
            ),
            'Stream10': grpc.unary_stream_rpc_method_handler(
                    servicer.Stream10,
                    request_deserializer=pipeline__pb2.StreamRequest.FromString,
                    response_serializer=pipeline__pb2.StreamResponse10.SerializeToString,
            ),
            'Stream11': grpc.unary_stream_rpc_method_handler(
                    servicer.Stream11,
                    request_deserializer=pipeline__pb2.StreamRequest.FromString,
                    response_serializer=pipeline__pb2.StreamResponse11.SerializeToString,
            ),
            'Stream12': grpc.unary_stream_rpc_method_handler(
                    servicer.Stream12,
                    request_deserializer=pipeline__pb2.StreamRequest.FromString,
                    response_serializer=pipeline__pb2.StreamResponse12.SerializeToString,
            ),
            'Stream13': grpc.unary_stream_rpc_method_handler(
                    servicer.Stream13,
                    request_deserializer=pipeline__pb2.StreamRequest.FromString,
                    response_serializer=pipeline__pb2.StreamResponse13.SerializeToString,
            ),
            'Stream14': grpc.unary_stream_rpc_method_handler(
                    servicer.Stream14,
                    request_deserializer=pipeline__pb2.StreamRequest.FromString,
                    response_serializer=pipeline__pb2.StreamResponse14.SerializeToString,
            ),
            'Stream15': grpc.unary_stream_rpc_method_handler(
                    servicer.Stream15,
                    request_deserializer=pipeline__pb2.StreamRequest.FromString,
                    response_serializer=pipeline__pb2.StreamResponse15.SerializeToString,
            ),
            'Stream16': grpc.unary_stream_rpc_method_handler(
                    servicer.Stream16,
                    request_deserializer=pipeline__pb2.StreamRequest.FromString,
                    response_serializer=pipeline__pb2.StreamResponse16.SerializeToString,
            ),
            'Stream17': grpc.unary_stream_rpc_method_handler(
                    servicer.Stream17,
                    request_deserializer=pipeline__pb2.StreamRequest.FromString,
                    response_serializer=pipeline__pb2.StreamResponse17.SerializeToString,
            ),
            'Stream18': grpc.unary_stream_rpc_method_handler(
                    servicer.Stream18,
                    request_deserializer=pipeline__pb2.StreamRequest.FromString,
                    response_serializer=pipeline__pb2.StreamResponse18.SerializeToString,
            ),
            'Stream19': grpc.unary_stream_rpc_method_handler(
                    servicer.Stream19,
                    request_deserializer=pipeline__pb2.StreamRequest.FromString,
                    response_serializer=pipeline__pb2.StreamResponse19.SerializeToString,
            ),
            'Stream20': grpc.unary_stream_rpc_method_handler(
                    servicer.Stream20,
                    request_deserializer=pipeline__pb2.StreamRequest.FromString,
                    response_serializer=pipeline__pb2.StreamResponse20.SerializeToString,
            ),
            'Stream21': grpc.unary_stream_rpc_method_handler(
                    servicer.Stream21,
                    request_deserializer=pipeline__pb2.StreamRequest.FromString,
                    response_serializer=pipeline__pb2.StreamResponse21.SerializeToString,
            ),
            'Stream22': grpc.unary_stream_rpc_method_handler(
                    servicer.Stream22,
                    request_deserializer=pipeline__pb2.StreamRequest.FromString,
                    response_serializer=pipeline__pb2.StreamResponse22.SerializeToString,
            ),
            'Stream23': grpc.unary_stream_rpc_method_handler(
                    servicer.Stream23,
                    request_deserializer=pipeline__pb2.StreamRequest.FromString,
                    response_serializer=pipeline__pb2.StreamResponse23.SerializeToString,
            ),
            'Stream24': grpc.unary_stream_rpc_method_handler(
                    servicer.Stream24,
                    request_deserializer=pipeline__pb2.StreamRequest.FromString,
                    response_serializer=pipeline__pb2.StreamResponse24.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'pipeline.StreamingPipeline', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class StreamingPipeline(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Stream1(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/pipeline.StreamingPipeline/Stream1',
            pipeline__pb2.StreamRequest.SerializeToString,
            pipeline__pb2.StreamResponse1.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Stream2(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/pipeline.StreamingPipeline/Stream2',
            pipeline__pb2.StreamRequest.SerializeToString,
            pipeline__pb2.StreamResponse2.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Stream3(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/pipeline.StreamingPipeline/Stream3',
            pipeline__pb2.StreamRequest.SerializeToString,
            pipeline__pb2.StreamResponse3.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Stream4(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/pipeline.StreamingPipeline/Stream4',
            pipeline__pb2.StreamRequest.SerializeToString,
            pipeline__pb2.StreamResponse4.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Stream5(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/pipeline.StreamingPipeline/Stream5',
            pipeline__pb2.StreamRequest.SerializeToString,
            pipeline__pb2.StreamResponse5.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Stream6(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/pipeline.StreamingPipeline/Stream6',
            pipeline__pb2.StreamRequest.SerializeToString,
            pipeline__pb2.StreamResponse6.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Stream7(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/pipeline.StreamingPipeline/Stream7',
            pipeline__pb2.StreamRequest.SerializeToString,
            pipeline__pb2.StreamResponse7.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Stream8(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/pipeline.StreamingPipeline/Stream8',
            pipeline__pb2.StreamRequest.SerializeToString,
            pipeline__pb2.StreamResponse8.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Stream9(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/pipeline.StreamingPipeline/Stream9',
            pipeline__pb2.StreamRequest.SerializeToString,
            pipeline__pb2.StreamResponse9.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Stream10(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/pipeline.StreamingPipeline/Stream10',
            pipeline__pb2.StreamRequest.SerializeToString,
            pipeline__pb2.StreamResponse10.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Stream11(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/pipeline.StreamingPipeline/Stream11',
            pipeline__pb2.StreamRequest.SerializeToString,
            pipeline__pb2.StreamResponse11.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Stream12(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/pipeline.StreamingPipeline/Stream12',
            pipeline__pb2.StreamRequest.SerializeToString,
            pipeline__pb2.StreamResponse12.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Stream13(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/pipeline.StreamingPipeline/Stream13',
            pipeline__pb2.StreamRequest.SerializeToString,
            pipeline__pb2.StreamResponse13.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Stream14(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/pipeline.StreamingPipeline/Stream14',
            pipeline__pb2.StreamRequest.SerializeToString,
            pipeline__pb2.StreamResponse14.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Stream15(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/pipeline.StreamingPipeline/Stream15',
            pipeline__pb2.StreamRequest.SerializeToString,
            pipeline__pb2.StreamResponse15.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Stream16(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/pipeline.StreamingPipeline/Stream16',
            pipeline__pb2.StreamRequest.SerializeToString,
            pipeline__pb2.StreamResponse16.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Stream17(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/pipeline.StreamingPipeline/Stream17',
            pipeline__pb2.StreamRequest.SerializeToString,
            pipeline__pb2.StreamResponse17.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Stream18(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/pipeline.StreamingPipeline/Stream18',
            pipeline__pb2.StreamRequest.SerializeToString,
            pipeline__pb2.StreamResponse18.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Stream19(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/pipeline.StreamingPipeline/Stream19',
            pipeline__pb2.StreamRequest.SerializeToString,
            pipeline__pb2.StreamResponse19.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Stream20(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/pipeline.StreamingPipeline/Stream20',
            pipeline__pb2.StreamRequest.SerializeToString,
            pipeline__pb2.StreamResponse20.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Stream21(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/pipeline.StreamingPipeline/Stream21',
            pipeline__pb2.StreamRequest.SerializeToString,
            pipeline__pb2.StreamResponse21.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Stream22(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/pipeline.StreamingPipeline/Stream22',
            pipeline__pb2.StreamRequest.SerializeToString,
            pipeline__pb2.StreamResponse22.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Stream23(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/pipeline.StreamingPipeline/Stream23',
            pipeline__pb2.StreamRequest.SerializeToString,
            pipeline__pb2.StreamResponse23.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Stream24(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/pipeline.StreamingPipeline/Stream24',
            pipeline__pb2.StreamRequest.SerializeToString,
            pipeline__pb2.StreamResponse24.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
