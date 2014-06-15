from datetime import timedelta, datetime, tzinfo


class UTCConverter(tzinfo):
    '''
    Subclassing the tzinfo class, for the sake of converting
    local time zone times into UTC. Feeds directly into the
    is new function.
    '''

    # Offset hours between local timezone and utc.
    # Then use the offset in the timedelta.
    def utcoffset(self, dt):
        offset = datetime.utcnow().hour -\
                 datetime.now().hour
        return timedelta(hours=offset) + self.dst(dt)

    # Method to account for dst in calculations.
    # The rest is adapted directly from the python
    # documentation example.
    # https://docs.python.org/2/library/datetime.html
    def dst(self, dt):
        d = datetime(dt.year, 4, 1)
        self.dston = d - timedelta(days=d.weekday() + 1)
        d = datetime(dt.year, 11, 1)
        self.dstoff = d - timedelta(days=d.weekday() +1)
        if self.dston <= dt.replace(tzinfo=None) < self.dstoff:
            return timedelta(hours=1)
        else:
            return timedelta(0)

    # Return timezone name
    def tzname(self, dt):
        return "UTC"
