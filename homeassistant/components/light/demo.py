"""
homeassistant.components.light.demo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Demo platform that implements lights.

"""
import random

from homeassistant.components.light import (
    Light, ATTR_BRIGHTNESS, ATTR_XY_COLOR, ATTR_COLOR_TEMP)


LIGHT_COLORS = [
    [0.368, 0.180],
    [0.460, 0.470],
]

LIGHT_TEMPS = [160, 500]


def setup_platform(hass, config, add_devices_callback, discovery_info=None):
    """ Find and return demo lights. """
    add_devices_callback([
        DemoLight("Bed Light", False),
        DemoLight("Ceiling Lights", True, LIGHT_TEMPS[1], LIGHT_COLORS[0]),
        DemoLight("Kitchen Lights", True, LIGHT_TEMPS[0], LIGHT_COLORS[1])
    ])


class DemoLight(Light):
    """ Provides a demo switch. """
    # pylint: disable=too-many-arguments
    def __init__(self, name, state, xy=None, ct=None, brightness=180):
        self._name = name
        self._state = state
        self._xy = xy or random.choice(LIGHT_COLORS)
        self._ct = ct or random.choice(LIGHT_TEMPS)
        self._brightness = brightness

    @property
    def should_poll(self):
        """ No polling needed for a demo light. """
        return False

    @property
    def name(self):
        """ Returns the name of the device if any. """
        return self._name

    @property
    def brightness(self):
        """ Brightness of this light between 0..255. """
        return self._brightness

    @property
    def color_xy(self):
        """ XY color value. """
        return self._xy

    @property
    def color_temp(self):
        """ CT color temperature. """
        return self._ct

    @property
    def is_on(self):
        """ True if device is on. """
        return self._state

    def turn_on(self, **kwargs):
        """ Turn the device on. """
        self._state = True

        if ATTR_XY_COLOR in kwargs:
            self._xy = kwargs[ATTR_XY_COLOR]

        if ATTR_COLOR_TEMP in kwargs:
            self._ct = kwargs[ATTR_COLOR_TEMP]

        if ATTR_BRIGHTNESS in kwargs:
            self._brightness = kwargs[ATTR_BRIGHTNESS]

        self.update_ha_state()

    def turn_off(self, **kwargs):
        """ Turn the device off. """
        self._state = False
        self.update_ha_state()
