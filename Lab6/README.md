Notes:

On MacOS you may run into issues with threading that throw errors like this:

    Traceback (most recent call last):
    File "<string>", line 1, in <module>
    File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/multiprocessing/spawn.py", line 116, in spawn_main
    exitcode = _main(fd, parent_sentinel)
    ...
In this case, you may need to explicitly set the multiprocessing unit to use "fork" instead of "spawn" in the first line of the "__main__" block:

    multiprocessing.set_start_method("fork")
 

Make sure you use "except Empty:" as the exception handler in teller_job

    teller_line.get() requires "timeout=" to assign value to correct parameter.

Please DO NOT forget to use bankprint() in the thread methods.  Otherwise the output will be all over the place.

