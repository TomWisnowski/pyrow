class Orchestrator:
    def orchestrate(self, my_pyrow, my_queue_service, time):
        monitor = my_pyrow.get_monitor()

        my_queue_service.send(monitor)

        time.sleep(1)
