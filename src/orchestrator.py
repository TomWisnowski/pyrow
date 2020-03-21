class Orchestrator:
    def orchestrate(mypyrow, myqueueService):
        monitor = mypyrow.get_monitor()

        myqueueService.send_to_queue(monitor)

        sleep(1000)