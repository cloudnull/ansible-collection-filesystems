#!/usr/bin/python
from os import stat


class FilterModule(object):
    def filters(self):
        return {
            "mirror_chunk": self.mirror_chunk,
            "create_option": self.create_option,
        }

    @staticmethod
    def _chunk(lst, chunk_size):
        """Yield successive n-sized chunks from lst.

        :param lst: List
        :param chunk_size: Integer
        :yield: List
        """
        for i in range(0, len(lst), chunk_size):
            yield lst[i : i + chunk_size]

    def mirror_chunk(self, devices):
        """Return a mirror string from a list of devices.

        :param devices: List
        :returns: String
        """
        return_string = ""
        if (len(devices) % 2) != 0:
            raise TypeError("The device list is not even so it can not be mirrored")

        split_size = len(devices)
        if split_size != 2:
            split_size = split_size / 2

        for chunk in self._chunk(lst=devices, chunk_size=split_size):
            return_string += "mirror {} ".format(" ".join(chunk))

        return return_string

    @staticmethod
    def create_option(options):
        format_options = list()
        for k, v in options.items():
            format_options.append("-o {}={}".format(k, v))

        return " ".join(format_options)
