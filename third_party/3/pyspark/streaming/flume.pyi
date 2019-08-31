# Stubs for pyspark.streaming.flume (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

def utf8_decoder(s): ...

class FlumeUtils:
    @staticmethod
    def createStream(ssc, hostname, port, storageLevel: Any = ..., enableDecompression: bool = ..., bodyDecoder: Any = ...): ...
    @staticmethod
    def createPollingStream(ssc, addresses, storageLevel: Any = ..., maxBatchSize: int = ..., parallelism: int = ..., bodyDecoder: Any = ...): ...