import pyrow
import queueService
import Orchestrator
import time


if __name__ == '__main__':
    mypyrow = pyrow()
    myqueueService = queueService()
    myOrchestrator = Orchestrator()

    while(1):
        myOrchestrator.orchestrate(mypyrow, myqueueService, time)