import asyncio
import grpc
import cv2
import numpy as np
import pipeline_pb2 as pb2
import pipeline_pb2_grpc as pb2_grpc


async def stream_video(stub):
    async for response in stub.Stream2(pb2.StreamRequest()):
        frame_data = response.frame
        frame_array = np.frombuffer(frame_data, dtype=np.uint8)
        frame = cv2.imdecode(frame_array, flags=cv2.IMREAD_COLOR)
        cv2.imshow("Stream2", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


async def main():
    async with grpc.aio.insecure_channel('localhost:50053') as channel:
        stub = pb2_grpc.StreamingPipelineStub(channel)

        await stream_video(stub)

    cv2.destroyAllWindows()


if __name__ == '__main__':
    asyncio.run(main())



