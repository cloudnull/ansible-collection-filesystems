#!/usr/bin/python
class FilterModule(object):
    def filters(self):
        return {
            'mirror_chunk': self.mirror_chunk,
        }

    @staticmethod
    def _chunk(lst):
        """Yield successive n-sized chunks from lst.

        :param lst: List
        :yield: List
        """
        for i in range(0, len(lst), 2):
            yield lst[i:i + 2]

    def mirror_chunk(self, devices):
        """Return a mirror string from a list of devices.

        :param devices: List
        :returns: String
        """
        return_string = ""
        for chunk in self._chunk(lst=devices):
            return_string += "mirror {} ".format(" ".join(chunk))

        return return_string
