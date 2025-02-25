"""The Symptom Diary integration."""

DOMAIN = "symptom_diary"

from homeassistant import config_entries
from homeassistant.core import HomeAssistant
from homeassistant.helpers import discovery
from .sensor import SymptomDiarySensor  # Import your sensor class

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the Symptom Diary integration asynchronously."""
    # Store data related to the integration
    hass.data[DOMAIN] = {}

    # Optionally, you can set up services or other initializations here

    return True

async def async_setup_entry(hass: HomeAssistant, entry: config_entries.ConfigEntry):
    """Set up a config entry for the Symptom Diary integration."""
    # Create an instance of the sensor
    sensor = SymptomDiarySensor()

    # Store the sensor instance in hass.data
    hass.data[DOMAIN][entry.entry_id] = sensor

    # Register the sensor with Home Assistant
    # This assumes you have a method to add entities
    from homeassistant.helpers.entity_platform import async_add_entities
    async_add_entities([sensor])

    return True

