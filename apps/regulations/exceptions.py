class NO_ATTENDANCE_DAY(Exception):
    pass


class TIMESLOT_MISSING(Exception):
    pass


class OUT_OF_ATTENDANCE_TIME(Exception):
    pass


class FACE_RECOGNITION_NO_DATASET(Exception):
    pass


class FACE_RECOGNITION_FAILED(Exception):
    pass


class FACE_RECOGNITION_IMEI_NOT_MATCH(Exception):
    pass


class FACE_DETECTION_FAILED(Exception):
    pass
