"""The Symptom Diary integration."""

DOMAIN = "symptom_diary"

from homeassistant import config_entries
from homeassistant.core import HomeAssistant
from homeassistant.helpers import discovery

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the Symptom Diary integration asynchronously."""
    # Register the sensor with Home Assistant
    hass.data[DOMAIN] = {}

    # You can also set up any necessary services or configurations here

    return True

async def async_setup_entry(hass: HomeAssistant, entry: config_entries.ConfigEntry):
    """Set up a config entry for the Symptom Diary integration."""
    # Create an instance of the sensor
    sensor = SymptomDiarySensor()

    # Add the sensor to Home Assistant
    hass.data[DOMAIN][entry.entry_id] = sensor

    # Register the sensor with Home Assistant
    async_add_entities([sensor])

    return True

# You can also include any necessary imports or setup code here
