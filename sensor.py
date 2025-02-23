import logging
from datetime import datetime
from homeassistant.helpers.entity import Entity
from homeassistant.helpers import config_entry_flow

_LOGGER = logging.getLogger(__name__)

class SymptomDiarySensor(Entity):
    """Representation of a Symptom Diary Sensor."""

    def __init__(self):
        self._state = None
        self._attributes = {}

    @property
    def name(self):
        return "Symptom Diary"

    @property
    def state(self):
        return self._state

    @property
    def extra_state_attributes(self):
        return self._attributes

    def update(self):
        # Logic to update the sensor state and attributes
        # For example, fetching data from a database or API
        pass

    def add_measurement(self, temperature, medication):
        timestamp = datetime.now().isoformat()
        self._attributes[timestamp] = {
            "temperature": temperature,
            "medication": medication
        }
        self._state = temperature  # Update the state to the latest temperature
        _LOGGER.info(f"Added measurement: {timestamp}, Temp: {temperature}, Med: {medication}")
