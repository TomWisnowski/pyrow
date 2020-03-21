import pyrow
import queueService
import Orchestrator


if __name__ == '__main__':
    mypyrow = new pyrow()
    myqueueService = new queueService()
    myOrchestrator = new Orchestrator()

    while(1):
        myOrchestrator.orchestrate(mypyrow, myqueueService)