def RunningIntoPythonIDLE():

    import idlelib.PyShell

    def frames(frame = sys._getframe()):
        _frame = frame
        while _frame :
            yield _frame
            _frame = _frame.f_back

    return idlelib.PyShell.main.__code__ in [frame.f_code for frame in frames()]
RunningIntoPythonIDLE()
