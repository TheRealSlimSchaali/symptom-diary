"""The Symptom Diary integration."""

DOMAIN = "symptom_diary"

from homeassistant import config_entries
from homeassistant.core import HomeAssistant
from homeassistant.helpers import discovery

async def async_setup(hass, config):
    hass.states.async_set("symptom_diary.world", "Some Symptom")

    # Return boolean to indicate that initialization was successful.
    return True

