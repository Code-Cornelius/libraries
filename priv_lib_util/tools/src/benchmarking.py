from math import floor
from time import time


def time_convertor_sec2hours_min_sec(seconds, time_format=0):
    """
    SEMANTICS : instead of converting the seconds in minutes outside, one can do it here.

    Args:
        seconds: runtime
        time_format:  0 is in seconds (no change), 1 is in min, 2 is in hour.

    Returns:
        converted time. 2/3/4-tuple s,m,h, seconds_frac

    """
    seconds_int = floor(seconds)
    seconds_frac = seconds - seconds_int
    if time_format == 0:
        return seconds_int, seconds_frac
    else:
        m, s = divmod(seconds_int, 60)
        if time_format == 1:
            return s, m, seconds_frac
        else:
            h, m = divmod(m, 60)
            return s, m, h, seconds_frac


def time_time2text(s, m, h, seconds_frac=0):
    """
    SEMANTICS : writes time as s,m,h into the format of text for printing for example.

    Args:
        s: seconds
        m: minutes
        h: hours
        seconds_frac: lower than a seconds

    Returns: format is ('s+seconds_frac seconds ', 'm minutes ', 'h hours ').
    The plural is changed depending on how many units there are, and if a variable is 0, the string is empty.

    """
    if s == 0:
        ts = ""
    elif s == 1:
        ts = f"{s + seconds_frac:d} second "
    else:
        ts = f"{s:d} seconds "

    if m == 0:
        tm = ""
    elif m == 1:
        tm = f"{m:d} minute "
    else:
        tm = f"{m:d} minutes "

    if h == 0:
        th = ""
    elif h == 1:
        th = f"{h:d} hour "
    else:
        th = f"{h:d} hours "

    if h == s and s == m and m == 0:
        ts = "{} second ".format(seconds_frac)
    return ts, tm, th


def time_print_elapsed_time(start, end, title="no title"):
    """ function that I put at the end of certain functions to know how long they runned.

    Args:
        start: beginning simulation's time.
        end: end simulation's time.
        title: function or bookmark to recognize where from the time.

    Returns:

    """
    seconds = end - start
    beg = " Program : " + title + ", took roughly :"
    print(100 * '~')
    s, m, h, seconds_frac = time_convertor_sec2hours_min_sec(seconds, time_format=2)
    ts, tm, th = time_time2text(s, m, h, seconds_frac)
    print(''.join([beg, th, tm, ts, 'to run.']))
    print(100 * '-')
    print(100 * '-')
    return


def benchmark(function, title ="no title", *args, **kwargs):
    """
    SEMANTICS : helper for benchmarking a function and prints the timing with the name given as title. Extra parameters can be given.
    Args:
        function: function to benchmark
        title: title that is printed as :  " Program : " + title + ", took roughly :"
        *args: extra arguments for the function.
        **kwargs: extra arguments for the function.

    Returns:

    """
    start = time()
    function(*args, **kwargs)
    end = time()
    time_print_elapsed_time(start, end, title=title)