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

# WindowID: 
WindowID = int

# WindowState: The state of the browser window.
WindowState = str

# Bounds: Browser window bounds information
class Bounds(ChromeTypeBase):
    def __init__(self,
                 left: Optional['int'] = None,
                 top: Optional['int'] = None,
                 width: Optional['int'] = None,
                 height: Optional['int'] = None,
                 windowState: Optional['WindowState'] = None,
                 ):

        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.windowState = windowState


# Bucket: Chrome histogram bucket.
class Bucket(ChromeTypeBase):
    def __init__(self,
                 low: Union['int'],
                 high: Union['int'],
                 count: Union['int'],
                 ):

        self.low = low
        self.high = high
        self.count = count


# Histogram: Chrome histogram.
class Histogram(ChromeTypeBase):
    def __init__(self,
                 name: Union['str'],
                 sum: Union['int'],
                 count: Union['int'],
                 buckets: Union['[Bucket]'],
                 ):

        self.name = name
        self.sum = sum
        self.count = count
        self.buckets = buckets


class Browser(PayloadMixin):
    """ The Browser domain defines methods and events for browser managing.
    """
    @classmethod
    def close(cls):
        """Close browser gracefully.
        """
        return (
            cls.build_send_payload("close", {
            }),
            None
        )

    @classmethod
    def getVersion(cls):
        """Returns version information.
        """
        return (
            cls.build_send_payload("getVersion", {
            }),
            cls.convert_payload({
                "protocolVersion": {
                    "class": str,
                    "optional": False
                },
                "product": {
                    "class": str,
                    "optional": False
                },
                "revision": {
                    "class": str,
                    "optional": False
                },
                "userAgent": {
                    "class": str,
                    "optional": False
                },
                "jsVersion": {
                    "class": str,
                    "optional": False
                },
            })
        )

    @classmethod
    def getBrowserCommandLine(cls):
        """Returns the command line switches for the browser process if, and only if
--enable-automation is on the commandline.
        """
        return (
            cls.build_send_payload("getBrowserCommandLine", {
            }),
            cls.convert_payload({
                "arguments": {
                    "class": [],
                    "optional": False
                },
            })
        )

    @classmethod
    def getHistograms(cls,
                      query: Optional['str'] = None,
                      delta: Optional['bool'] = None,
                      ):
        """Get Chrome histograms.
        :param query: Requested substring in name. Only histograms which have query as a
substring in their name are extracted. An empty or absent query returns
all histograms.
        :type query: str
        :param delta: If true, retrieve delta since last call.
        :type delta: bool
        """
        return (
            cls.build_send_payload("getHistograms", {
                "query": query,
                "delta": delta,
            }),
            cls.convert_payload({
                "histograms": {
                    "class": [Histogram],
                    "optional": False
                },
            })
        )

    @classmethod
    def getHistogram(cls,
                     name: Union['str'],
                     delta: Optional['bool'] = None,
                     ):
        """Get a Chrome histogram by name.
        :param name: Requested histogram name.
        :type name: str
        :param delta: If true, retrieve delta since last call.
        :type delta: bool
        """
        return (
            cls.build_send_payload("getHistogram", {
                "name": name,
                "delta": delta,
            }),
            cls.convert_payload({
                "histogram": {
                    "class": Histogram,
                    "optional": False
                },
            })
        )

    @classmethod
    def getWindowBounds(cls,
                        windowId: Union['WindowID'],
                        ):
        """Get position and size of the browser window.
        :param windowId: Browser window id.
        :type windowId: WindowID
        """
        return (
            cls.build_send_payload("getWindowBounds", {
                "windowId": windowId,
            }),
            cls.convert_payload({
                "bounds": {
                    "class": Bounds,
                    "optional": False
                },
            })
        )

    @classmethod
    def getWindowForTarget(cls,
                           targetId: Union['Target.TargetID'],
                           ):
        """Get the browser window that contains the devtools target.
        :param targetId: Devtools agent host id.
        :type targetId: Target.TargetID
        """
        return (
            cls.build_send_payload("getWindowForTarget", {
                "targetId": targetId,
            }),
            cls.convert_payload({
                "windowId": {
                    "class": WindowID,
                    "optional": False
                },
                "bounds": {
                    "class": Bounds,
                    "optional": False
                },
            })
        )

    @classmethod
    def setWindowBounds(cls,
                        windowId: Union['WindowID'],
                        bounds: Union['Bounds'],
                        ):
        """Set position and/or size of the browser window.
        :param windowId: Browser window id.
        :type windowId: WindowID
        :param bounds: New window bounds. The 'minimized', 'maximized' and 'fullscreen' states cannot be combined
with 'left', 'top', 'width' or 'height'. Leaves unspecified fields unchanged.
        :type bounds: Bounds
        """
        return (
            cls.build_send_payload("setWindowBounds", {
                "windowId": windowId,
                "bounds": bounds,
            }),
            None
        )

