# -*- coding: utf-8 -*-
"""
Module to report the battery level from my UPS

Dependencies: upsc
And assumes you have named your UPS 'battery'
If you named it something else you can set it below in the command
"""


class Py3status:
    cache_timeout = 600
    format = "🔋: {status}"

    def _get_battery_status(self):
        try:
            status = self.py3.command_output(["upsc", "battery", "ups.status"])
            return {"status": status.strip()}

        except self.py3.CommandError as ce:
            return len(ce.output.splitlines())

    def ups_battery_status(self):

        status = self._get_battery_status()
        full_text = self.py3.safe_format(self.format, status)

        return {
            "full_text": full_text,
            "cached_until": self.py3.time_in(self.cache_timeout),
        }


if __name__ == "__main__":
    from py3status.module_test import module_test
    module_test(Py3status)
