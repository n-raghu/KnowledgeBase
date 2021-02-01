# Asyncio

The event loop is the core of every asyncio application. Event loops run asynchronous tasks and callbacks, perform network IO operations, and run subprocesses.

Application developers should typically use the high-level asyncio functions, such as asyncio.run(), and should rarely need to reference the loop object or call its methods. This section is intended mostly for authors of lower-level code, libraries, and frameworks, who need finer control over the event loop behavior.

Obtaining the Event Loop

The following low-level functions can be used to get, set, or create an event loop:

### asyncio.get_running_loop()
Return the running event loop in the current OS thread.

If there is no running event loop a RuntimeError is raised. This function can only be called from a coroutine or a callback.

### asyncio.get_event_loop()
Get the current event loop.

If there is no current event loop set in the current OS thread, the OS thread is main, and set_event_loop() has not yet been called, asyncio will create a new event loop and set it as the current one.

Because this function has rather complex behavior (especially when custom event loop policies are in use), using the get_running_loop() function is preferred to get_event_loop() in coroutines and callbacks.

Consider also using the asyncio.run() function instead of using lower level functions to manually create and close an event loop.

### asyncio.set_event_loop(loop)
Set loop as a current event loop for the current OS thread.

### asyncio.new_event_loop()
Create a new event loop object.

_Note that the behaviour of `get_event_loop()`, `set_event_loop()`, and `new_event_loop()` functions can be altered by setting a custom event loop policy_
