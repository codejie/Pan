import asyncio
import threading
import time
from typing import Optional

class Task:
  def __init__(self, exit_event: asyncio.Event, name: Optional[str] = None):
    self.name = name
    self.exit_event = exit_event

  async def run(self):
    if self.name:
      print(f"Task {self.name} started.")
    else:
      print("Task started.")

    while not self.exit_event.is_set():
      await asyncio.sleep(1)  # Simulate work
      print(f"Task {self.name} is running...") if self.name else print("Task is running...")

    if self.name:
      print(f"Task {self.name} exiting.")
    else:
      print("Task exiting.")

class TaskManager:
  def __init__(self):
    self._thread: threading.Thread | None = None
    self._thread_ready: threading.Event = threading.Event()

    self._loop: asyncio.AbstractEventLoop | None = None
    self._exit_event: asyncio.Event = asyncio.Event()
    self._task_queue: asyncio.Queue[Task] = asyncio.Queue()

  def _start_loop(self):
    self._loop = asyncio.new_event_loop()
    asyncio.set_event_loop(self._loop)
    self._exit_event.clear()

    async def _loop_run():
      while not self._exit_event.is_set():
        try:
          task = self._task_queue.get_nowait()
          asyncio.create_task(task.run())
        except asyncio.QueueEmpty:
          await asyncio.sleep(0.1)
        except Exception as e:
          print(f"Error in task loop: {e}")
          break

    self._loop.call_soon_threadsafe(asyncio.create_task, _loop_run())
    self._thread_ready.set()

    try:
      self._loop.run_forever()
    except RuntimeError as e:
      if str(e) == "Event loop is closed":
        print("Event loop was closed, exiting task manager.")
      else:
        print(f"Unexpected error in event loop: {e}")
        raise e
    finally:
      # self._exit_event.set()
      pending = asyncio.all_tasks(self._loop)
      if pending:
        self._loop.run_until_complete(asyncio.gather(*pending, return_exceptions=True))
      self._loop.close()
      # self._loop.stop()

  def start(self):
    if self._thread is not None and self._thread.is_alive():
      print("TaskManager is already running.")
      return

    self._exit_event.clear()
    self._loop = asyncio.new_event_loop()
    asyncio.set_event_loop(self._loop)

    self._thread = threading.Thread(target=self._start_loop, name="TaskManagerThread", daemon=True)
    self._thread.start()
    self._thread_ready.wait()

  def stop(self):
    if self._thread is None or not self._thread.is_alive():
      print("TaskManager is not running.")
      return

    self._exit_event.set()
    if self._loop and self._loop.is_running():
      self._loop.call_soon_threadsafe(self._loop.stop)
    self._thread.join(timeout=5)  # Wait for the thread to finish
    if self._thread.is_alive():
      print("TaskManager thread did not stop in time.")

    self._loop = None
    self._thread = None
    self._thread_ready.clear()

  def get_exit_event(self) -> asyncio.Event:
    return self._exit_event
  
  def set_exit_event(self):
    self._exit_event.set()

  def add_task(self, task: type):
    self.add_instance(task(self._exit_event))
  
  def add_instance(self, instance: Task):
    if self._thread is None or not self._thread.is_alive():
      raise RuntimeError("TaskManager is not running. Start it before adding tasks.")
    self._task_queue.put_nowait(instance) 


def main():
  manager = TaskManager()
  manager.start()

  # 添加任务
  manager.add_task(Task)
  manager.add_instance(Task(manager.get_exit_event(),"Task1"))
  manager.add_instance(Task(manager.get_exit_event(), "Task2"))

  time.sleep(5)  # 等待任务执行一段时间
  manager.set_exit_event()  # 设置退出事件
  time.sleep(5)  # 等待任务完成
  print("Stopping TaskManager...")
  manager.stop()

if __name__ == "__main__":
  main()