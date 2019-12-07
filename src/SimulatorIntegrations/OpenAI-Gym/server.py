import grpc
from concurrent import futures
import numpy as np
import time

import gym

from OpenAIEnv import Envs

import grpc_compiled.services.simulator.response_pb2 as response_pb2
import grpc_compiled.system.base_response_pb2 as base_response_pb2
import grpc_compiled.system.space_pb2 as space_pb2
import grpc_compiled.services.simulator.service_pb2 as simulator_pb2
import grpc_compiled.services.simulator.service_pb2_grpc as simulator_pb2_grpc

import logging
logger = logging.getLogger('werkzeug')
logger.setLevel(logging.ERROR)

# Our environments being used
envs = Envs()

class SimulatorServicer(simulator_pb2_grpc.SimulatorServicer):
    def Create(self, request, context):
        logger.info("Creating environment %s" % (request.envId))
        response = response_pb2.CreateResponse()
        response.instanceId = envs.create(request.envId)
        return response

    # def step(self, instance_id, action, render):
    def Step(self, request, context):
        logger.info("Stepping through instance %s" % (request.instanceId))
        response = response_pb2.StepResponse()

        # Returns obs_jsonable, reward, done, info
        result = envs.step(request.instanceId, request.action, request.render)
        
        response.reward = result[1]
        response.isDone = result[2]
        # response.info = result[3]

        # Get the ObservationSpace metadata
        osi = envs.get_observation_space_info(request.instanceId)

        spaceWrapper = space_pb2.SpaceWrapper()

        if osi.HasField('discrete'):
            discreteSpace = space_pb2.SpaceDiscrete()
            discreteSpace.observation = result[0]
            spaceWrapper.discrete.CopyFrom(discreteSpace)
        elif osi.HasField('box'):
            boxSpace = space_pb2.SpaceBox()
            boxSpace.observation.extend(result[0])
            spaceWrapper.box.CopyFrom(boxSpace)
        else:
            logger.error("Unsupported Space Type: %s" % info['name'])
            logger.error(info)

        response.observation.CopyFrom(spaceWrapper)

        logger.info("Step returned %s" % (response))

        return response

    def Reset(self, request, context):
        logger.info("Resetting instance %s" % (request.instanceId))
        response = response_pb2.ResetResponse()

        envObservation = envs.reset(request.instanceId)
        response.observation.extend(envObservation)

        return response

    def Close(self, request, context):
        logger.info("Closing instance %s" % (request.instanceId))
        envs.env_close(request.instanceId)
        return response_pb2.CloseResponse() # Empty response

    def MonitorStart(self, request, context):
        logger.info("Monitor Start for instance %s" % (request.instanceId))
        envs.monitor_start(request.instanceId, './monitor', True, False, 10)
        return base_response_pb2.BaseResponse() # Empty response

    def MonitorStop(self, request, context):
        logger.info("Monitor Stop for instance %s" % (request.instanceId))
        envs.monitor_close(request.instanceId)
        return base_response_pb2.BaseResponse() # Empty response

    def ActionSpaceSample(self, request, context):
        response = response_pb2.ActionSpaceSampleResponse()
        action = envs.get_action_space_sample(request.instanceId)
        response.action = action
        logger.info("Sampled Action Space %s" % (response))
        return response
        
    def ActionSpaceInfo(self, request, context):
        response = response_pb2.ActionSpaceInfoResponse()
        response.result.CopyFrom(envs.get_action_space_info(request.instanceId))
        return response
    
    def ObservationSpaceInfo(self, request, context):
        response = response_pb2.ObservationSpaceInfoResponse()
        response.result.CopyFrom(envs.get_observation_space_info(request.instanceId))
        print(response)
        return response
        

# Create the gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# use the generated function `add_SimulatorServicer_to_server` to add the defined class to the server
simulator_pb2_grpc.add_SimulatorServicer_to_server(SimulatorServicer(), server)

# listen on port 50051
print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)