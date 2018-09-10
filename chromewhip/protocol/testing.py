# noinspection PyPep8
# noinspection PyArgumentList

"""
AUTO-GENERATED BY `scripts/generate_protocol.py` using `data/browser_protocol.json`
and `data/js_protocol.json` as inputs! Please do not modify this file.
"""

import logging
from typing import Any, Optional, Union

from chromewhip.helpers import PayloadMixin, BaseEvent, ChromeTypeBase

log = logging.getLogger(__name__)
from chromewhip.protocol import page as Page

class Testing(PayloadMixin):
    """ Testing domain is a dumping ground for the capabilities requires for browser or app testing that do not fit other
domains.
    """
    @classmethod
    def generateTestReport(cls,
                           message: Union['str'],
                           group: Optional['str'] = None,
                           ):
        """Generates a report for testing.
        :param message: Message to be displayed in the report.
        :type message: str
        :param group: Specifies the endpoint group to deliver the report to.
        :type group: str
        """
        return (
            cls.build_send_payload("generateTestReport", {
                "message": message,
                "group": group,
            }),
            None
        )

